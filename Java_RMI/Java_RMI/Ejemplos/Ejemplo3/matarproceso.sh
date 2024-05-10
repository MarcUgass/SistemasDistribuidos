#!/bin/bash

# Verificar si se proporciona un número de puerto como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <puerto>"
    exit 1
fi

puerto=$1

# Buscar el PID del proceso que está escuchando en el puerto especificado
pid=$(lsof -ti :$puerto)

# Verificar si se encontró algún proceso escuchando en el puerto
if [ -z "$pid" ]; then
    echo "No se encontró ningún proceso escuchando en el puerto $puerto."
    exit 1
fi

# Matar el proceso encontrado
kill $pid

echo "El proceso con PID $pid que escuchaba en el puerto $puerto ha sido terminado."
