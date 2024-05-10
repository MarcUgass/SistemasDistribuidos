#!/bin/sh -e
# ejecutar = Macro para compilacion y ejecucion del programa con objeto remoto
# en una sola maquina Unix de nombre localhost.

echo
echo "Lanzando el cliente"
java -cp . -Djava.rmi.server.codebase=file:./ -Djava.security.policy=server.policy cliente
