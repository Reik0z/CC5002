#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi 
import json 
import logging
from db import DB

print('Access-Control-Allow-Origin: *')
print("Content-type:  application/json; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'ejercicio6')

form = cgi.FieldStorage()
info = form.getvalue('info')


if info == 'region':
    results = db.get_regiones()
    print(json.dumps(results))    

if info == 'comuna':
    region_id = form.getvalue('region_id')
    if (region_id != None):
        results = db.get_comunas(region_id)
        print(json.dumps(results))

# IMPORTANTE: se entrega Nombre, Latitud y Longitud.
if info == 'cordenada':
    comuna_id = form.getvalue('comuna_id')
    if (comuna_id != None):
        results = db.get_comuna_latlong(comuna_id)
        print(json.dumps(results))
