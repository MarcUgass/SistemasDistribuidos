import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.*;
import java.rmi.registry.Registry;
import java.rmi.NotBoundException;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.rmi.registry.LocateRegistry;
import java.util.Scanner;

public class contador extends UnicastRemoteObject implements icontador, contador_I {
    private int suma;
    private int indice;
    Map<String,Integer> clientes;
    private String ID;
    Registry reg;
    contador_I replica;



    //Funcion inicializadora
    public contador(String id) throws RemoteException {
    	this.clientes = new HashMap<>();
        this.suma = 0;
        this.indice = 0;
        this.ID = id;
        this.reg = LocateRegistry.getRegistry();
    }
    
    public void setreplica(String id) throws RemoteException {
    try {
    	replica = (contador_I) reg.lookup(id);
    }
    catch (Exception e){
    	System.err.println("Error al establecer conexon " + e.getMessage());
    }
    }
    
    //Funcion para saber si el cliente esta en el registro
    public boolean existeCliente(String dni) throws RemoteException {
    return clientes.containsKey(dni);
    }
    
    public void imprimir() throws RemoteException {
    for (Map.Entry<String,Integer>entry: clientes.entrySet()){
    System.out.println("Cliente " + entry.getKey() + ": Cantidad donada: " + entry.getValue());
    	}
    }

    public int registrar(String dni, Registry r) throws RemoteException, NotBoundException {
    	    int indice = clientes.size();
    	    clientes.put(dni, indice);
	    System.out.println("Cliente " + dni + " anadido con exito!");
	    return indice;
    }

    public int InicioSesion(String dni, Registry r) throws RemoteException, NotBoundException {
    Scanner scanner = new Scanner(System.in);
    if (!clientes.isEmpty()){
	    if (existeCliente(dni) == false){
	    indice = registrar(dni, r);

	    }
	    else{
	    	System.out.println("Bienvenido cliente " + dni);
	    	//indice = clientes.indexOf(dni);
	    }
	 } else {
	 System.out.println("No hay clientes registrados");
	 }
    return indice;
    }

    public void donar(String dni, int valor) throws RemoteException {
     //int dni = clientes.get(indice);
     if (existeCliente(dni)){
     int valorActual = clientes.get(dni);
     clientes.put(dni, valorActual + valor);
     System.out.println("El cliente " + dni + " ha donado " + valor + "$");
     } else {
     System.out.println("El cliente " + dni  + " no esta registrado");
     }
    }
    
    public String getID() throws RemoteException {
    return this.ID;
    }

}
