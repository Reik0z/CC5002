#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
cgitb.enable(display=0, logdir="path/to/logdir")

form = cgi.FieldStorage()
if 'nombreUsuario' not in form:
    print('<h1> Error en el nombre <h1>')
else:
    user = form.getvalue('nombreUsuario')
    print('<p>Nombre:', user, '<p>')

if 'exampleFormControlSelect1' not in form:
    print('<h1> Error en seleccion de pizza <h1>')
else:
    select = form.getvalue('exampleFormControlSelect1')
    print('<p>Pizza:', select, '<p>')

if 'comentarios' not in form:
    print('<h1> Error en comentarios <h1>')
else:
    com = form.getvalue('comentarios')
    print('<p>Comentarios:', com, '<p>')

if 'telefono' not in form:
    print('<h1> Error en el numero de telefono <h1>')
else:
    tel = form.getvalue('telefono')
    print('<p>Telefono:', tel, '<p>')

if 'direccion' not in form:
    print('<h1> Error en la direccion <h1>')
else:
    addr = form.getvalue('direccion')
    print('<p>Direccion:', addr, '<p>')