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
        # Procesar archivo
        fileobj = data[7]
        filename = fileobj.value

        sql = "SELECT COUNT(id) FROM foto" # Cuenta los archivos que hay en la base de datos
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1
        filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
        filename_hash += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
        # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
        #       Lo que se conoce como un datarace

        # Guardar archivo
        try:
            # guardar encargo
            sql ='''
                INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data[:7])  # ejecuto la consulta
            encargo_id = self.cursor.getlastrowid() # recupera el último id ingresado

            open(f"media/{filename_hash}", "wb").write(fileobj.file.read()) # guarda el archivo localmente

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