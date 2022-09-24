#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys
import html

cgitb.enable()

form = cgi.FieldStorage()
html.escape(form)
if 'nombreUsuario' not in form:
    print('<h1> Error en el nombre <h1>')
else:
    user = form.getvalue('nombreUsuario')
    print('<div>Nombre:', user, '<div>')

if 'pizzafavorita' not in form:
    print('<h1> Error en seleccion de pizza <h1>')
else:
    select = form.getvalue('pizzafavorita')
    print('<div>Pizza:', select, '<div>')

if 'comentarios' not in form:
    print('<h1> Error en comentarios <h1>')
else:
    com = form.getvalue('comentarios')
    print('<div>Comentarios:', com, '<div>')

if 'telefono' not in form:
    print('<h1> Error en el numero de telefono <h1>')
else:
    tel = form.getvalue('telefono')
    print('<div>Telefono:', tel, '<div>')

if 'direccion' not in form:
    print('<h1> Error en la direccion <h1>')
else:
    addr = form.getvalue('direccion')
    print('<div>Direccion:', addr, '<div>')

head = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- CSS bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" crossorigin="anonymous">

    <!-- JS bootstrap -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
    
</head>
"""
body = """

<body>
    <section class="jumbotron text-center">
        <div class= "container">
            <h1 class="jumbotron-heading">Datos Ingresados</h1>
            <p class="lead ">Mostramos los datos que se recibieron en el formulario</p>
        </div>
    </section>

    <div class="container p-3 my-3 border bg-light">
        <div class="mb-3">
            <label for="nombre" class="form-label">Nombre Ingresado: {}</label>
        </div>
        <div class="mb-3">
            <label for="pizzafavorita" class="form-label">Pizza Favorita Ingresado: {}</label>
        </div>
        <div class="mb-3">
            <label for="comentario" class="form-label">Comentario Ingresado: {}</label>
        </div>
        <div class="mb-3">
            <label for="telefono" class="form-label">Telefono Ingresado: {}</label>
        </div>
        <div class="mb-3">
            <label for="direccion" class="form-label">Direccion Ingresada: {}</label>
        </div>
    </div>

</body>
""".format(user, select, com, tel, addr)

print(head+body)