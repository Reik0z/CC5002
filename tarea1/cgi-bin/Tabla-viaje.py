# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

sql_total = '''
            SELECT COUNT(id)
            FROM viaje
            '''

db.cursor.execute(sql_total)
total = db.cursor.fetchall()[0][0]

if total > 5:
    total = 5

def elementos_actuales(actual):
    sql_elementos = '''
                    SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero 
                    FROM viaje ORDER BY id ASC LIMIT {}, 5
                    '''.format(actual)
    db.cursor.execute(sql_elementos)
    return db.cursor.fetchall()

head = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Ver Viajes</title>

    <link
      href="style/bootstrap.css"
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
      src="style/bootstrap.js"
    ></script>
  </head>
    <body class="bg-light">
    <div class="container">
      <main>
        <div class="py-5 text-center">
          <h2>Ver Viajes</h2>
        </div>
        <div>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Origen</th>
                <th scope="col">Destino</th>
                <th scope="col">Fecha ida</th>
                <th scope="col">Fecha llegada</th>
                <th scope="col">Espacio</th>
                <th scope="col">Kilos</th>
                <th scope="col">Email</th>
              </tr>
            </thead>
            <tbody>
            '''

body = '''
            </tbody>
            </table>
            <nav aria-label="...">
                <ul class="pagination">
                    <li class="page-item disabled">
                    <a class="page-link">Previous</a>
                    </li>
                    <li class="page-item active" aria-current="page">
                    <a class="page-link" href="#">{}</a>
                    </li>
                    <li class="page-item">
                    <a class="page-link" href="#">Next</a>
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
</html>'''.format(0)

print(head)

for i in range(0, total): # falta arreglar para muchos casos
    datos = elementos_actuales(i)
    datos = datos[0][1:8]

    sql_origen = '''
                SELECT nombre
                FROM ciudad
                WHERE id = {}
                '''.format(datos[0])
    db.cursor.execute(sql_origen)
    origen = db.cursor.fetchall()[0][0]

    sql_destino = '''
                SELECT nombre
                FROM ciudad
                WHERE id = {}
                '''.format(datos[1])
    db.cursor.execute(sql_destino)
    destino = db.cursor.fetchall()[0][0]

    sql_espacio = '''
                SELECT valor
                FROM espacio_encargo
                WHERE id = {}
                '''.format(datos[4])
    db.cursor.execute(sql_espacio)
    espacio = db.cursor.fetchall()[0][0]

    sql_kilos = '''
                SELECT valor
                FROM kilos_encargo
                WHERE id = {}
                '''.format(datos[5])
    db.cursor.execute(sql_kilos)
    kilos = db.cursor.fetchall()[0][0]

    fecha_ida = datos[2]
    fecha_regreso = datos[3]


    tabla = '''
        <tr onclick="location.href='../informacion-viaje.html#viaje-1'">
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>
        '''.format(origen, destino, fecha_ida, fecha_regreso, espacio, kilos, datos[6])
    print(tabla)

print(body)