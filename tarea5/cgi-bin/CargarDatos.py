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
    viajes = db.ultimos_viajes()
    print(json.dumps(viajes))

# Obtenemos los ultimos 5 encargos
if necesitamos == 'e':
    encargos = db.ultimos_encargos()
    print(json.dumps(encargos))