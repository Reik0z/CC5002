#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

form = cgi.FieldStorage()
id_encargo = form.getvalue('id_encargo')

print("Content-type: text/html; charset=UTF-8")
print()

head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Ver Encargos</title>

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

# Obtenemos datos
sql_dato = '''
          SELECT id, descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador 
          FROM encargo 
          WHERE id = {}
           '''.format(id_encargo)
db.cursor.execute(sql_dato)
dato_encargo = db.cursor.fetchall()[0]

if dato_encargo[7] == '':
    tel = "No registrado"
else:
    tel = dato_encargo[7]

origen = db.get_data('nombre', 'ciudad', 'id', dato_encargo[4])
destino = db.get_data('nombre', 'ciudad', 'id', dato_encargo[5])
espacio = db.get_data('valor', 'espacio_encargo', 'id', dato_encargo[2])
kilos = db.get_data('valor', 'kilos_encargo', 'id', dato_encargo[3])

sql_id = '''
        SELECT (id)
        FROM foto
        WHERE encargo_id = '{}'
        '''.format(id_encargo)
db.cursor.execute(sql_id)
foto_id = db.cursor.fetchall() # contiene los id de las 3 fotos

sql_ruta = '''
        SELECT (ruta_archivo)
        FROM foto
        WHERE encargo_id = '{}'
        '''.format(id_encargo)
db.cursor.execute(sql_ruta)
foto_ruta = db.cursor.fetchall() # contiene las rutas de las 3 fotos


body = '''
  <body class="bg-light">
    <div class="container">
      <main>
        <h2 class="mt-4">Información Encargos</h2>
        <button
          type="button"
          class="btn btn-outline-dark"
          onclick="location.href='Tabla-encargo.py?page=0'"
        >
          Ver encargos
        </button>
        <div class="p-4" id="encargo-{}">
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
        <div class="col-md-6 themed-grid-col">Fotos</div>
        '''.format(id_encargo, origen, destino)

print(body)

for i in range(0,len(foto_id)):
    foto = '''
        <div class="col-md-4 themed-grid-col">
          <img
            src="../media/{}"
            width="640"
            height="480"
            id="foto-{}"
            alt="foto del encargo {}"
            onclick="resizeimagen('foto-{}')"
          />
        </div>
      </div>
      '''.format(foto_ruta[i][0], foto_id[i][0], foto_id[i][0], foto_id[i][0])
    print(foto)

body_ext = '''  
          </div>
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
                <div class="col-md-6 themed-grid-col">Descripcion</div>
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
'''.format(espacio, kilos, dato_encargo[6], dato_encargo[1], tel)

print(body_ext)
print('''
      <script>
        var grande = false;
        function resizeimagen(imagen){
          let foto = document.getElementById(imagen);
          if (grande){
            foto.width = "640";
            foto.height = "480";
            grande = false;
          } else{
            foto.width = "1280";
            foto.height = "1024";
            grande = true;
          }
        }
      </script>

      <footer class="my-5 pt-5 text-muted text-center text-small">
        <p class="mb-1">CC5002</p>
      </footer>
    </div>
  </body>
</html>
''')
