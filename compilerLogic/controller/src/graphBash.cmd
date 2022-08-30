@ECHO OFF
Param(
  [string]$file
)

PowerShell.exe -Command "dot -Tpng .\$file.vz -o ../../static/graphs/$file.png"

ECHO "Imagen Creada"