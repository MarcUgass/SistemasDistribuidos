#!/bin/sh -e
# ejecutar = Macro para compilacion y ejecucion del programa con objeto remoto
# en una sola maquina Unix de nombre localhost.

echo
echo "Lanzando el ligador de RMI … "
rmiregistry &

echo
echo "Compilando con javac ..."
javac *.java
sleep 2
