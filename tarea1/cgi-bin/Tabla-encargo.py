# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

form = cgi.FieldStorage()
pag = int(form.getvalue('page'))

sql_total = '''
            SELECT COUNT(id)
            FROM encargo
            '''

db.cursor.execute(sql_total)
total = db.cursor.fetchall()[0][0]

if pag < 0:
    pag = 0

if total/((pag+1)*5) >= 1:
    total = 5
else:
    total = total%5

if pag <= 0:
    pag = 0

def tabla(actual):
    if actual <= 0:
        actual = 0
    else:
        actual*5 - 1

    sql_elementos = '''
                    SELECT id, descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador 
                    FROM encargo 
                    ORDER BY id ASC LIMIT {}, 5
                    '''.format(actual)
    db.cursor.execute(sql_elementos)
    datos_total = db.cursor.fetchall()

    for i in range(0, total):
        datos = datos_total[i]

        encargo_id = datos[0]
        foto = db.get_data('ruta_archivo', 'foto', 'encargo_id', encargo_id)[i]
        origen = db.get_data('nombre', 'ciudad', 'id', datos[4])
        destino = db.get_data('nombre', 'ciudad', 'id', datos[5])
        espacio = db.get_data('valor', 'espacio_encargo', 'id', datos[2])
        kilos = db.get_data('valor', 'kilos_encargo', 'id', datos[3])


        tabla = '''
          <tr onclick="location.href='Mostrar-encargo.py?id_encargo={}'">
            <td>{}</td>
            <td>{}</td>
            <td><img src="../media/{}" height="120" width="120" alt="foto del encargo {}"></td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
          </tr>
            '''.format(encargo_id, origen, destino, foto, encargo_id, espacio, kilos, datos[6])
        print(tabla)


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
  </head>
  <body class="bg-light">
    <div class="container">
      <main>
        <div class="py-5 text-center">
          <h2>Ver Encargos</h2>
        </div>
        <div>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Origen</th>
                <th scope="col">Destino</th>
                <th scope="col">Fotos</th>
                <th scope="col">Espacio</th>
                <th scope="col">Kilos</th>
                <th scope="col">Email</th>
              </tr>
            </thead>
            <tbody>
            '''

pag_v = pag+1

body = '''
            </tbody>
          </table>
            <nav aria-label="...">
                <ul class="pagination">
                    <li class="page-item">
                    <a class="page-link" href="?page={}">Anterior</a>
                    </li>
                    <li class="page-item active" aria-current="page">
                    <a class="page-link">{}</a>
                    </li>
                    <li class="page-item">
                    <a class="page-link" href="?page={}">Siguiente</a>
                    </li>
                </ul>
            </nav>
        </div>
      </main>

      <footer class="my-5 pt-5 text-muted text-center text-small">
        <p class="mb-1">CC5002</p>
      </footer>
    </div>
  </body>
</html>
'''.format(pag-1, pag_v, pag+1)

print(head)
tabla(pag)
print(body)