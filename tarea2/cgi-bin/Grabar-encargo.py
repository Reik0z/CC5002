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

db = DB('localhost', 'root', '', 'tarea2')

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

telefono = form.getvalue('celular')
if telefono != '':
    patron_celular = "^\\+?\d{7,15}$"
    if not re.match(patron_celular, telefono):
        errores.append('<p> Error, en el formato del telefono </p>'.format(telefono))

# Revisamos archivos subidos
if 'foto-encargo-0' not in form:
    errores.append('<p>Error, falta adjuntar foto.<p>')
else:
    fileobj = (form['foto-encargo-0'],)
    fileobj += (form['foto-encargo-1'],)
    fileobj += (form['foto-encargo-2'],)
    tipos_soportados = ['image/jpeg', 'image/jpg', 'image/png']

    for j in range(0,3):
        if fileobj[j] == None:
            fileobj = fileobj[:j]
            break
        elif fileobj[j].filename:
            tipo = fileobj[j].type
            if tipo not in tipos_soportados:
                errores.append('Error, formato no valido. {}'.format(tipo))
                sys.exit()
        else:
            errores.append("Error, archivo no subido.")

head = """
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Tarea 1</title>

    <link rel="icon" type="image/x-icon" href="favicon.ico">

    <!-- CSS bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" crossorigin="anonymous">

    <!-- JS bootstrap -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>

    <style>
      .bd-placeholder-/img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-/img-lg {
          font-size: 3.5rem;
        }
      }
      .b-example-divider {
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .feature-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 4rem;
        height: 4rem;
        margin-bottom: 1rem;
        font-size: 2rem;
        color: #fff;
        border-radius: .75rem;
      }

      .icon-link {
        display: inline-flex;
        align-items: center;
      }
      .icon-link > .bi {
        margin-top: .125rem;
        margin-left: .125rem;
        transition: transform .25s ease-in-out;
        fill: currentColor;
      }
      .icon-link:hover > .bi {
        transform: translate(.25rem);
      }

      .icon-square {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 3rem;
        height: 3rem;
        font-size: 1.5rem;
        border-radius: .75rem;
      }

      .rounded-4 { border-radius: .5rem; }
      .rounded-5 { border-radius: 1rem; }

      .text-shadow-1 { text-shadow: 0 .125rem .25rem rgba(0, 0, 0, .25); }
      .text-shadow-2 { text-shadow: 0 .25rem .5rem rgba(0, 0, 0, .25); }
      .text-shadow-3 { text-shadow: 0 .5rem 1.5rem rgba(0, 0, 0, .25); }

      .card-cover {
        background-repeat: no-repeat;
        background-position: center center;
        background-size: cover;
      }

    </style>

  </head>
"""

if (errores == []):
    origen = db.get_data('id', 'ciudad', 'nombre', ciudadOrigen)
    destino = db.get_data('id', 'ciudad', 'nombre', ciudadDestino)

    data = (desc, int(espacioDisponible), int(kilosDisponibles), origen, destino, correo, telefono, fileobj)
    print(head)
    print("""
    <body>
    <main>
      <div class="b-example-divider"></div>

      <div class="container px-4 py-5" id="custom-cards">
        <h2 class="pb-2 border-bottom" style="text-align:center;">Inicio</h2>
    """)
    print("""<div class="bg-success p-2 text-white">Encargo agregado correctamente!</div>""")
    db.save_order(data)
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
              onclick="location.href='/cgi-bin/Tabla-viaje.py?page=0'"
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
              onclick="location.href='/cgi-bin/Tabla-encargo.py?page=0'"
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
