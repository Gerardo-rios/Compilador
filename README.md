# Compilador
Compilador que realiza el análisis léxico, sintáctico y semántico.

# Variables de entorno
Crear un archivo `.env` usando la siguiente estructura

```bash
DJANGO_SECRET_KEY=..........
```

# Requerimientos
Instalar los respectivos requerimientos, utilizando el siguiente comando: `pip install requeriments.txt`

# Uso de los métodos

# doAnalysis(number, string):

Para el análizador sintáctico, funciona como sigue:
```python

from .controller.src import analizadorSintactico 

#Si se tiene un texto (Código.pl0), utilizar de la siguiente forma

#ejemplo de cadena de código
cadena = "CONST\nm=7,\nn=85;\n#flgmsdglsm .,,sdf'\nVAR\n  x, y, z, q, r;\nPROCEDURE multiply;\nVAR a, b;\nBEGIN\n  a := x;\n  b := y;\n  z := 0;\nEND;"

analizadorSintactico.doAnalysis(0, cadena)

#Si se eligió un archivo de los predeterminados para prueba, utilizar así:

analizadorSintactico.doAnalysis(fileNumber)

```
