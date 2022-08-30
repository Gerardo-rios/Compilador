#!/bin/bash

#no se como hacer que se ejecuten comandos con sh xD --Pero creo que es así
dot -Tpng ./$1.vz -o compilerLogic/static/assets/img/$2.png

echo “Imagen Creada”