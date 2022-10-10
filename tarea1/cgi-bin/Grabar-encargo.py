#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys
import html
import re
from db import DB

cgitb.enable()

form = cgi.FieldStorage()

db = DB('localhost', 'root', '', 'tarea2') #base de datos que tengo yo ej: tarea 2

errores = []

# Revisamos los select ingresados
if 'pais-origen' not in form:
    errores.append('<p> Error, seleccione un pais de origen valido </p>')
else:
    paisOrigen = form.getvalue('pais-origen')

if 'ciudad-origen' not in form:
    errores.append('<p> Error, seleccione una ciudad de origen valida </p>')
else:
    ciudadOrigen = form.getvalue('ciudad-origen')

if 'pais-destino' not in form:
    errores.append('<p> Error, seleccione un pais de destino valido </p>')
else:
    paisDestino = form.getvalue('pais-destino')

if 'ciudad-destino' not in form:
    errores.append('<p> Error, seleccione una ciudad de destino valida </p>')
else:
    ciudadDestino = form.getvalue('ciudad-destino')

# Revisamos que las ciudades y paises sean distintas
if (errores == []):
    if paisOrigen == paisDestino:
        errores.append('<p> Error, envio al mismo pais</p>')
    if ciudadOrigen == ciudadDestino:
        errores.append('<p> Error, envio a la misma ciudad</p>')

# Seguimos revisando select
if 'espacio-solicitado' not in form:
    errores.append('<p> Error, seleccione espacio disponible </p>')
else:
    espacioDisponible = form.getvalue('espacio-solicitado')

if 'kilos-solicitados' not in form:
    errores.append('<p> Error, seleccione kilos solicitados </p>')
else:
    kilosDisponibles = form.getvalue('kilos-solicitados')

# Revisamos ingreso sin select
if 'descripcion' not in form:
    errores.append('<p> Error, ingrese una descripcion </p>')
else:
    desc = form.getvalue('descripcion')
    if len(desc) > 250:
        errores.append('<p> Error, descripcion muy larga </p>')

if 'email' not in form:
    errores.append('<p> Error, ingrese un email valido </p>')
else:
    correo = form.getvalue('email')
    patron_email = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not (re.match(patron_email, correo)):
        errores.append('<p>Error, formato del email.</p>')

if 'celular' in form:
    telefono = form.getvalue('celular')
    patron_numero = "^\\+?\d{7,15}$"
    if not (re.match(patron_numero, telefono)):
        errores.append('<p>Error, formato del numero de telefono.</p>')
telefono = ''

# Revisamos archivos subidos
if 'foto-encargo-0' not in form:
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

if (errores == []):
    origen = db.get_data('id', 'ciudad', 'nombre', ciudadOrigen)
    destino = db.get_data('id', 'ciudad', 'nombre', ciudadDestino)

    data = (desc, int(espacioDisponible), int(kilosDisponibles), origen, destino, correo, telefono, fileobj)
    db.save_order(data)
    print(head)
    print("""
    <body>
    <main>
      <div class="b-example-divider"></div>

      <div class="container px-4 py-5" id="custom-cards">
        <h2 class="pb-2 border-bottom" style="text-align:center;">Inicio</h2>
    """)
    print("""<div class="bg-success p-2 text-white">Encargo agregado correctamente!</div>""")
    print("<h3>" + str(data[:7]) + (data[7].value) + "<h3>")
    print("""
            <div class="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
          <div class="col">
            <div
              class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg"
              style="background-image: url('/img/foto1.jpg');"
              onclick="location.href='../agregar-viaje.html'"
            >
              <div
                class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1"
              >
                <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                  Agregar Viaje
                </h2>
              </div>
            </div>
          </div>

          <div class="col">
            <div
              class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg"
              style="background-image: url('/img/foto2.jpg');"
              onclick="location.href='../agregar-encargo.html'"
            >
              <div
                class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1"
              >
                <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                  Agregar Encargo
                </h2>
              </div>
            </div>
          </div>

          <div class="col">
            <div
              class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg"
              style="background-image: url('/img/foto3.jpg');"
              onclick="location.href='../ver-viajes.html'"
            >
              <div class="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                  Ver Viajes
                </h2>
              </div>
            </div>
          </div>

          <div class="col">
            <div
              class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg"
              style="background-image: url('/img/foto4.jpg');"
              onclick="location.href='../ver-encargos.html'"
            >
              <div class="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                  Ver Encargos
                </h2>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </body>
</html>
    """)
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
