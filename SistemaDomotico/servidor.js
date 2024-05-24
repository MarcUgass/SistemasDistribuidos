import http          from 'node:http';
import {join}        from 'node:path';
import {readFile}    from 'node:fs';
import {Server}      from 'socket.io';
import {MongoClient} from 'mongodb';


const httpServer = http
    .createServer((request, response) => {
        let {url} = request;
        if(url == '/') {
            url = '/interfaz_cliente.html';
            const filename = join(process.cwd(), url);

            readFile(filename, (err, data) => {
                if(!err) {
                    response.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
                    response.write(data);
                } else {
                    response.writeHead(500, {"Content-Type": "text/plain"});
                    response.write(`Error en la lectura del fichero: ${url}`);
                }
                response.end();
            });
        }
        else {
            console.log('Peticion invalida: ' + url);
            response.writeHead(404, {'Content-Type': 'text/plain'});
            response.write('404 Not Found\n');
            response.end();
        }
    });


MongoClient.connect("mongodb://localhost:27017/").then((db) => {
    httpServer.listen(8080);
    const dbo = db.db("SistemaDomotico");
    const collection = dbo.collection("Informacion");

    let Persiana = false, AireC = false;
    var iluminacion = 50, temperatura = 29;
    
    const io = new Server(httpServer);

    io.sockets.on('connection', function(client) {
        client.on('sensores', function(data){
            var datos_sensores = {ilum: data.ilum, temp: data.temp, fecha: new Date()}
            collection.insertOne(datos_sensores).then(function(result) {});
            temperatura = data.temp;
            iluminacion = data.ilum;
            console.log("Iluminación: " + data.ilum + "%, Temperatura: " + temperatura + "º");
            Agente(iluminacion, temperatura, Persiana, AireC, client);
        })
        client.on('actuadores', function(data){
            Persiana = data.Ventana;
            AireC = data.AireAC;
            console.log("Ventana: " + Persiana + ", Aire AC: " + AireC);
            Agente(iluminacion, temperatura, Persiana, AireC, client);

        })

    });
}).catch((err) => {console.error(err);});

console.log('Servicio MongoDB iniciado');

function Agente(ilum, temp, Persiana, AireC, client) {
    if (Persiana &&  AireC){
        client.emit('alertas', {
            mensajeSalida: 'El aire acondicionado y la ventana están abiertas', 
        });
    }else if (ilum < 20 && temp > 35 && !Persiana && !AireC) {
        client.emit('alerta', { 
            mensajeSalida: "Cuidado! Te recomiendo que abras una ventana.",
        });
    } else if (ilum > 40 && temp > 35 && Persiana && !AireC) {
        client.emit('alerta', { 
            mensajeSalida: "Alerta! Te recomiendo que enciendes el aire, y cierres la ventana.",
        });
    } else if(ilum < 20 && temp < 35 && !Persiana && AireC) {
        client.emit('alerta', { 
            mensajeSalida: "Cuidado! Te recomiendo que apagues el aire y abres la ventana.",
        });
    } else if (temp > 35 && !AireC && ilum >= 20) {
        client.emit('alerta', { 
            mensajeSalida: "Cuidado! Te recomiendo que apagues el aire y abras la ventana.",
        });
    } else if ((temp <= 35 && AireC && ilum >= 20) || (temp <= 35 && !AireC && ilum >= 20)) {
        client.emit('alerta', { 
            mensajeSalida: "No hay de que preocuparse!",
        });
    }

}