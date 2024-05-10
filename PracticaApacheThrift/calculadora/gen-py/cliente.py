from calculadora import Calculadora
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def menu_calculadora_basica(client):
    print("\n--- Calculadora Básica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Seleccione una opción: "))        
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    if opcion == 1:
        resultado = client.suma(a, b)
        print(f"{a} + {b} = {resultado}")
    elif opcion == 2:
        resultado = client.resta(a, b)
        print(f"{a} - {b} = {resultado}")
    elif opcion == 3:
        resultado = client.multiplicacion(a, b)
        print(f"{a} * {b} = {resultado}")
    elif opcion == 4:
    	if b == 0:
    		print("Error: el denominador no peudo ser 0")
    	else:
        	resultado = client.division(a, b)
        	print(f"{a} / {b} = {resultado}")

def menu_calculadora_grados_radianes(client):
    print("\n--- Calculadora de Grados y Radianes ---")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Grados a Radianes")
    print("5. Radianes a Grados")
    opcion = int(input("Seleccione una opción: "))
    grados = float(input("Introduce los grados o radianes (recuerda que se calcula a partir de los grados):"))
    
    if opcion == 1:
        resultado = client.seno(grados)
        print(f"El seno de {grados} es {resultado}")

    elif opcion == 2:
    	resultado = client.coseno(grados)
        #print(f"El coseno de {grados} es {resultado}")
    elif opcion == 3:
    	resultado = client.tangente(grados)
        #print(f"La tangente de {grados} es {resultado}")
    elif opcion == 4:
    	resultado = client.gradosradianes(grados)
        #print(f"El valor de {grados} grados es {resultado} radianes")
    elif opcion == 5:
    	resultado = client.radianesgrados(grados)
        #print(f"El valor de {grados} radianes es {reusltado} grados")

def menu_calculadora_compleja(client):
    while True:
        print("\n--- Calculadora Compleja ---")
        print("1. Potencia")
        print("2. Raiz cuadrada")
        print("3. Modulo")
        print("4. Logaritmo")
        opcion = int(input("Selecciona una opcion: "))
        a = float(input("Ingrese el numero: "))
        if opcion == 1:
            b = float(input("Ingrese el valor de la potencia: "))
            resultado = client.potencia(a,b)
            print(f"La potencia de {a} elevado a {b} es {resultado}")
        elif opcion == 2:
            resutlado = client.raiz_cuadrada(a)
            print(f"La raiz cuadrada de {a} es {resultado}")
        elif opcion == 3:
            b = float(input("Ingrese el valor del modulo: "))
            resultado = client.modulo(a,b)
            print(f"El valor de {a} sobre el modulo de {b} es {resultado}")
        elif opcion == 4:
            resultado = client.logaritmo(a)
            print(f"El logaritmo de {a} es {resultado}")

def menu_calculadora_vectores(client):
    while True:
        print("\n--- Calculadora de vectores ---")
        print("1. Suma de vectores")
        print("2. Resta de vectores")
        print("3. Producto de vectores")

        opcion = int(input("Selecciona la opcion: "))
        inp1 = input("Ingrese los elementos de vector 1 (separado por comas): ")
        inp2 = input("Ingrese los elementos de vector 2 (separado por comas): ")
        el1 = inp1.split(',')
        el2 = inp2.split(',')
        v1 = [float(elemento) for elemento in el1]
        v2 = [float(elemento) for elemento in el2]
        if opcion == 1:
            resultado = client.suma_vector(v1,v2)
            print(f"La suma del vector {v1} y {v2} es {resultado}")
        elif opcion == 2:
            resultado = client.resta_vector(v1,v2)
            print(f"La resta del vector {v1} y {v2} es {resultado}")
        elif opcion == 3:
            resultado = client.producto_vector(v1,v2)
            print(f"El producto del vector {v1} y {v2} es {resultado}")
def menu_principal(client):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Calculadora Básica")
        print("2. Calculadora de Grados y Radianes")
        print("3. Calculadora Compleja")
        print("4. Calculadora de vectores")
        print("5. Salir")
        opcion = float(input("Seleccione una opción: "))
        if opcion == 1:
            menu_calculadora_basica(client)
        elif opcion == 2:
            menu_calculadora_grados_radianes(client)
        elif opcion == 3:
            menu_calculadora_compleja(client)
        elif opcion == 4:
            menu_calculadora_vectores(client)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Calculadora.Client(protocol)
transport.open()

menu_principal(client)

transport.close()
