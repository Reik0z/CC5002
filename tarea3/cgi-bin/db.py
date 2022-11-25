#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_order(self, data):

        # Guardar archivo
        try:
            # guardar encargo
            sql ='''
                INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data[:7])  # ejecuto la consulta
            encargo_id = self.cursor.getlastrowid() # recupera el último id ingresado

            for i in data[7]:
                # Procesar archivo
                fileobj = i
                filename = fileobj.filename

                sql = "SELECT COUNT(id) FROM foto" # Cuenta los archivos que hay en la base de datos
                self.cursor.execute(sql)
                total = self.cursor.fetchall()[0][0] + 1
                filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
                filename_hash += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
                # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
                #       Lo que se conoce como un datarace

                open(f"../media/{filename_hash}", "wb").write(fileobj.file.read()) # guarda el archivo localmente

                sql_file = '''
                    INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id)
                    VALUES (%s, %s, %s)
                    '''
                self.cursor.execute(sql_file, (filename_hash, filename, encargo_id))  # ejecuta la query que guarda el archivo en base de datos
                self.db.commit()                # modifico la base de datos
            
        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def save_travel(self, data):
        try:
            sql = '''
                INSERT INTO  viaje (origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
            # guardar viaje
            self.cursor.execute(sql, data)  # ejecuto la consulta
            self.db.commit()                # modifico la base de datos
            
        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def get_data(self, columna, tabla, parametro, dato):
        sql = '''
            SELECT {} 
            FROM {}
            WHERE {} = '{}'
            '''.format(columna, tabla, parametro, dato)
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def nombreCity(self, ciudad):
        sql = '''
            SELECT nombre
            FROM ciudad
            WHERE id = {}
            '''.format(ciudad)
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def ultimos_viajes(self):
        sql = '''
            SELECT origen, destino, email_viajero, id, fecha_ida, fecha_regreso
            FROM viaje ORDER BY id DESC LIMIT 5
            '''
        self.cursor.execute(sql)
        viajes = self.cursor.fetchall() # son los 5 viajes c/tupla
        lista = []
        for i in viajes:
            tupla = ()
            tupla += (self.nombreCity(i[0]),)
            tupla += (self.nombreCity(i[1]),)
            tupla += i[2:4]
            tupla += (str(i[4]),)
            tupla += (str(i[5]),)
            lista.append(tupla)
        return lista
    
    def ultimos_encargos(self):
        sql = '''
            SELECT origen, destino, id, email_encargador, descripcion
            FROM encargo ORDER BY id DESC LIMIT 5
            '''
        self.cursor.execute(sql)
        encargos = self.cursor.fetchall()
        lista = []
        for i in encargos:
            tupla = ()
            tupla += (self.nombreCity(i[0]),)
            tupla += (self.nombreCity(i[1]),)
            tupla += i[2:]
            lista.append(tupla)
        return lista

    def grafico1(self, tabla, parametro):
        res = []
        sql1 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 1
            '''.format(tabla, parametro)
        self.cursor.execute(sql1)
        res += self.cursor.fetchall()[0]

        sql2 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 2
            '''.format(tabla, parametro)
        self.cursor.execute(sql2)
        res += self.cursor.fetchall()[0]

        sql3 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 3
            '''.format(tabla, parametro)
        self.cursor.execute(sql3)
        res += self.cursor.fetchall()[0]

        return res

    def grafico2(self, tabla, parametro):
        res = []
        sql1 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 1
            '''.format(tabla, parametro)
        self.cursor.execute(sql1)
        res += self.cursor.fetchall()[0]

        sql2 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 2
            '''.format(tabla, parametro)
        self.cursor.execute(sql2)
        res += self.cursor.fetchall()[0]

        sql3 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 3
            '''.format(tabla, parametro)
        self.cursor.execute(sql3)
        res += self.cursor.fetchall()[0]

        sql4 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 4
            '''.format(tabla, parametro)
        self.cursor.execute(sql4)
        res += self.cursor.fetchall()[0]

        sql5 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 5
            '''.format(tabla, parametro)
        self.cursor.execute(sql5)
        res += self.cursor.fetchall()[0]

        sql6 = '''
            SELECT COUNT(*)
            FROM {}
            WHERE {} = 6
            '''.format(tabla, parametro)
        self.cursor.execute(sql6)
        res += self.cursor.fetchall()[0]

        return res