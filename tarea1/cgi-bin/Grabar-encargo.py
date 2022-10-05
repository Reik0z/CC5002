#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys
import html
import re
import db

cgitb.enable(display=0, logdir="/path/to/logdir")  

form = cgi.FieldStorage()

# db = db.DB(host, user, password, database)

valido = True
errores = []

# Revisamos los select ingresados
if 'pais-origen' not in form:
    valido = False
    errores.append('<p> Error, seleccione un pais de origen valido </p>')
else:
    paisOrigen = form.getvalue('pais-origen')

if 'ciudad-origen' not in form:
    valido = False
    errores.append('<p> Error, seleccione una ciudad de origen valida </p>')
else:
    ciudadOrigen = form.getvalue('ciudad-origen')

if 'pais-destino' not in form:
    valido = False
    errores.append('<p> Error, seleccione un pais de destino valido </p>')
else:
    paisDestino = form.getvalue('pais-destino')

if 'ciudad-destino' not in form:
    valido = False
    errores.append('<p> Error, seleccione una ciudad de destino valida </p>')
else:
    ciudadDestino = form.getvalue('ciudad-destino')

# Revisamos que las ciudades y paises sean distintas
if (valido):
    if paisOrigen == paisDestino:
        valido = False
        errores.append('<p> Error, envio al mismo pais</p>')
    if ciudadOrigen == ciudadDestino:
        valido = False
        errores.append('<p> Error, envio a la misma ciudad</p>')

# Seguimos revisando select
if 'espacio-solicitado' not in form:
    valido = False
    errores.append('<p> Error, seleccione espacio disponible </p>')
else:
    espacioDisponible = form.getvalue('espacio-solicitado')

if 'kilos-solicitados' not in form:
    valido = False
    errores.append('<p> Error, seleccione kilos solicitados </p>')
else:
    kilosDisponibles = form.getvalue('kilos-solicitados')

# Revisamos ingreso sin select
if 'descripcion' not in form:
    valido = False
    errores.append('<p> Error, ingrese una descripcion </p>')
else:
    desc = form.getvalue('descripcion')

if 'email' not in form:
    valido = False
    errores.append('<p> Error, ingrese un email valido </p>')
else:
    correo = form.getvalue('email')
    if re.search(r"^([A-Z,a-z,0-9_\-\.])+\@([A-Z,a-z,0-9_\-\.])+\.([A-Z,a-z]{2,4})$/", correo):
        valido = False
        erroes.append('<p>Error, formato del email.</p>')

if 'celular' in form:
    telefono = form.getvalue('celular')
    if re.search(r"^\+\d{11}$/", telefono):
        valido = False
        errores.append('<p>Error, formato del numero de telefono.</p>')

# Revisamos archivos subidos
if 'foto-encargo-0' not in form:
    valido = False
    errores.append('<p>Error, falta adjuntar foto.<p>')
else:
    fileobj = form['foto-encargo-0']
    tipos_soportados = ['image/jpeg', 'image/jpg', 'image/png']
    if fileobj.filename:
        tipo = fileobj.type
        if tipo not in tipos_soportados:
            print('Error, formato no valido. {}'.format(tipo))
            sys.exit()
    else:
        print("Error, archivo no subido.")

head = """
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Agregar Viaje</title>

    <!-- CSS bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" crossorigin="anonymous">

    <!-- JS bootstrap -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>

  </head>
"""

if (valido):
    data = (paisDestino, paisOrigen, ciudadDestino, ciudadOrigen, )
    db.save_order(data)
else:
    print(head)
    print("""
    <body>
    <section class="jumbotron text-center">
        <div class= "container">
            <h1 class="jumbotron-heading">Error en los Datos Ingresados</h1>
            <p class="lead ">ERRORES</p>
        </div>
    </section>

    <div class="container p-3 my-3 border bg-light">""")
    for i in range(0, len(errores)):
        print(errores[i])

    print("""</div>

    </body>""")
