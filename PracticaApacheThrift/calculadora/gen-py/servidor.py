import glob
import sys
import math
import socket

from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def suma(self, n1, n2):
        print("sumando " + str(n1) + " con " + str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print("restando " + str(n1) + " con " + str(n2))
        return n1 - n2
        
    def multiplicacion(self, n1, n2):
    	print("multiplicando " + str(n1) + " con " + str(n2))
    	return n1*n2
        
    def division(self, n1, n2):
    	if n2 == 0:
    		print("Error: El denominador tiene que ser diferente a 0")
    		return 0
    	else:
    		print("dividiendo " + str(n1) + " con " + str(n2))
    		return n1/n2
        	
    def gradosradianes(self,n1):
    	print("Calculando los radianes de " + str(n1))
    	return math.radians(n1)

    	
    def radianesgrados(self, n1):
    	print("Calculando los grados de " + str(n1))    
    	return math.degrees(n1)
    	
    def seno(self, n1):
        radianes = math.radians(n1)
        print("Calculando el seno de " + str(n1))
        return math.sin(radianes)

    def coseno(self, n1):
        print("Calculando el coseno de " + str(n1))    
        n = gradosradianes(n1)    	
        return math.cos(n)
    	    
    def tangente(self, n1):
        print("Calculando la tangente de " + str(n1))   
        n = gradosradianes(n1) 
        return math.tan(n)
        
    def potencia(self, n1, n2):
    	print("Calculando la potencia de " + str(n1) + "^" + str(n2))
    	return n1 ** n2
    	
    def raiz_cuadrada(self, n1):
    	print("Calculando la raiz cuadrada de " + str(n1))
    	return math.sqrt(n1)
    	
    def modulo(self, n1, n2):
    	print("Calculando el modulo de " + str(n1) + " sobre " + str(n2))
    	return n1 % n2
    
    def logaritmo(self, n1):
    	print("Calculando el logaritmo de " + str(n1))
    	return math.log(n1, 10)
    
    def suma_vector(self, v1, v2):
        for i in range(len(v1)):
            v1[i] +=v2[i]
        return v1
    
    def resta_vector(self, v1, v2):
        for i in range(len(v1)):
            v1[i] -=v2[i]
        return v1

    def producto_vector(self, v1, v2):
        for i in range(len(v1)):
            v1[i] *=v2[i]
        return v1

if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
