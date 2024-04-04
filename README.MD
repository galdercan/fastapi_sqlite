# FASTAPI - APP

Requisitos:

python3 -m pip install --upgrade pip
pip3 install virtualenv


### Ejecutar aplicación manualmente

1. Iniciar entorno virtual en linux `python3 -m venv venv` desde la raiz. 
   (En la carpeta /venv ya estan todas las dependencias pre instaladas)

2. Ejecutar la aplicacion: `uvicorn src:main:app --reload`

### Ejecutar con Makefile

Ejecutar `make all` en la raiz del proyecto.

Esto iniciara el entorno virtual, instalará las dependencias en caso de no tenerlas y lanzará la aplicación.



### API Swagger: `http://127.0.0.1:8000/docs`

Una vez iniciada la API

- Crear un candidato:

 1. POST a http://127.0.0.1:8000/candidato con el siguiente curl y formato
   
    curl -X 'POST' \
    'http://127.0.0.1:8000/candidato/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "dni": "DNI",
    "nombre": "nombre",
    "apellido": "apellido"
    }'

 2. Usando el swagger directamente en /candidatos/


- Ver candidatos creados:

 1. GET a http://127.0.0.1:8000/candidatos
   <br>
    curl -X 'GET' \
    'http://127.0.0.1:8000/candidatos/' \
    -H 'accept: application/json'

 2. Usando el swagger en /candidato

