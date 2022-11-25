#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

form = cgi.FieldStorage()
id_viaje = form.getvalue('id_viaje')

print("Content-type: text/html; charset=UTF-8")
print()

head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Ver Viajes</title>

    <link
      href="../style/bootstrap.css"
      rel="stylesheet"
    />
    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
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

      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }

      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }
    </style>

    <script
      src="../style/bootstrap.js"
    ></script>
  </head>'''
print(head)

# Obtenemos los datos de id
sql_dato = '''
           SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero 
           FROM viaje 
           WHERE id = {}
           '''.format(id_viaje)
db.cursor.execute(sql_dato)
dato_viaje = db.cursor.fetchall()[0]

if dato_viaje[8] == '':
    tel = "No registrado"
else:
    tel = dato_viaje[8]

origen = db.get_data('nombre', 'ciudad', 'id', dato_viaje[1])
destino = db.get_data('nombre', 'ciudad', 'id', dato_viaje[2])
kilos = db.get_data('valor', 'kilos_encargo', 'id', dato_viaje[5])
espacio = db.get_data('valor', 'espacio_encargo', 'id', dato_viaje[6])


body = '''
  <body class="bg-light">
    <div class="container">
      <main>
        <h2 class="mt-4">Información Viajes</h2>
        <button
          type="button"
          class="btn btn-outline-dark"
          onclick="location.href='Tabla-viaje.py?page=0'"
        >
          Ver viajes
        </button>
        <div class="p-4" id="viaje-{}">
          <div class="border border-dark">
            <div class="p-2">
              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Origen</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Destino</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Fecha ida</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Fecha llegada</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Espacio</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Kilos</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>

              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Email</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>
              <div class="row mb-3 text-center">
                <div class="col-md-6 themed-grid-col">Telefono</div>
                <div class="col-md-4 themed-grid-col">{}</div>
              </div>
            </div>
          </div>
        </div>
      </main>

      <footer class="my-5 pt-5 text-muted text-center text-small">
        <p class="mb-1">CC5002</p>
      </footer>
    </div>
  </body>
</html>
'''.format(id_viaje, origen, destino, dato_viaje[3].date(), dato_viaje[4].date(), espacio, kilos, dato_viaje[7], tel)

print(body)