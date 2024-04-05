# FASTAPI - APP

<h4>Requisitos</h4>

<b>python3.8+</b>
<b>pip:</b> python3 -m pip install --upgrade pip
<b>virtualenv:</b> pip3 install virtualenv

<h4>Dependencias</h4>

En la carpeta `/venv` ya estan todas las dependencias preinstaladas del archivo <b>requiremens.txt</b>

Si queremos instalarlas manualmente o añadir nuevas, una vez dentro del entorrno virtual ejecutar:

```
(venv) ~/FastAPI_Sqlite$ pip3 install -r requirements.txt
```
<hr>

### Ejecutar aplicación manualmente

1. Desde terminal, iniciar entorno virtual en linux `python3 -m venv venv` desde la raiz.

2. Ejecutar la aplicacion: `(venv) uvicorn src:main:app --reload`

### Ejecutar con Makefile

Desde terminal, ejecutar `make all` en la raiz del proyecto.

Esta ejecuccion iniciara el entorno virtual, instalará las dependencias en caso de no tenerlas (siempre actualizará nuevas liberias que añadamos a posterior) y lanzará la aplicación.

```
~/FastAPI_Sqlite$ make all
venv/bin/uvicorn src.main:app --reload
INFO:     Will watch for changes in these directories: ['/home/galder/FastAPI_Sqlite']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [219704] using StatReload
INFO:     Started server process [219706]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
<hr>

### API Swagger | http://127.0.0.1:8000

Una vez iniciada la API , la url de inicio `/` nos redireccionara al swagger `/docs`

<h4>Crear un candidato</h4>

 1. POST a http://127.0.0.1:8000/candidato con el siguiente curl y formato

   ```
    curl -X 'POST' \
    'http://127.0.0.1:8000/candidato/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "dni": "DNI",
    "nombre": "nombre",
    "apellido": "apellido"
    }'
   ```


 2. Usando el endpoint mediante el swagger o el navegadir web en `/candidatos/ `


<h4>Ver candidatos creados</h4>

Por defecto tiene ya mis datos como candidato,

 1. Desde terminal GET a http://127.0.0.1:8000/candidatos
   ```
    curl \
    'http://127.0.0.1:8000/candidatos/' \
    -H 'accept: application/json'
   ```

 2. Usando el endpoint mediante el swagger o navegador en `/candidatos`


<h4>Encontrar un candidato creado a través del DNI</h4>

 1. GET a http://127.0.0.1:8000/candidato/{dni}

   ```
      curl \
      'http://127.0.0.1:8000/candidato/16088405C' \
      -H 'accept: application/json'
   ```
 2. Usando el endpoint mediante el swagger o navegador en  `/candidato/{dni} `
