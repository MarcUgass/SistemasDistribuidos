#!/bin/sh -e
# ejecutar = Macro para compilacion y ejecucion del programa con objeto remoto
# en una sola maquina Unix de nombre localhost.

echo
echo "Lanzando el ligador de RMI … "
rmiregistry 1234 &

echo
echo "Compilando con javac ..."
javac *.java
sleep 2

echo
echo "Lanzando el servidor"
java -cp . -Djava.rmi.server.codebase=file:./ -Djava.rmi.server.hostname=localhost -Djava.security.policy=server.policy servidor &
sleep 2

echo
echo "Lanzando el cliente"
java -cp . -Djava.rmi.server.codebase=file:./ -Djava.security.policy=server.policy cliente localhost

