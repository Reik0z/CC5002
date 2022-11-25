#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
import json
from db import DB

print('Access-Control-Allow-Origin: *')
print("Content-type:  application/json; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')

form = cgi.FieldStorage()
necesitamos = form.getvalue('necesitamos')

# Obtenemos los 5 ultimos viajes
if necesitamos == 'v':
    viajes = db.ultimos_viajes() # tenemos los 5 viajes en una tupla
    print(json.dumps(viajes))

# Obtenemos los ultimos 5 encargos
if necesitamos == 'e':
    encargos = db.ultimos_encargos()
    print(json.dumps(encargos))

# Obtenemos datos graficos 1
if necesitamos == 'g1':
    grafico = db.grafico1('viaje', 'espacio_disponible')
    print(json.dumps(grafico))

# Obtenemos datos graficos 2
if necesitamos == 'g2':
    grafico = db.grafico2('viaje', 'kilos_disponible')
    print(json.dumps(grafico))

# Obtenemos datos graficos 3
if necesitamos == 'g3':
    grafico = db.grafico1('encargo', 'espacio')
    print(json.dumps(grafico))

# Obtenemos datos graficos 4
if necesitamos == 'g4':
    grafico = db.grafico2('encargo', 'kilos')
    print(json.dumps(grafico))