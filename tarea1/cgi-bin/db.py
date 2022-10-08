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
        fileobj = data[2]
        filename = fileobj.filename
        
        sql = "SELECT COUNT(id) FROM foto" # Cuenta los archivos que hay en la base de datos
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1
        filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
        filename_hash += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
        # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
        #       Lo que se conoce como un datarace

        # Guardar archivo
        
        try:
            open(f"media/{filename_hash}", "wb").write(fileobj.file.read()) # guarda el archivo localmente
            sql_file = '''
                INSERT INTO foto (nombre, path) 
                VALUES (%s, %s)
                '''
            self.cursor.execute(sql_file, (filename, filename_hash))  # ejecuta la query que guarda el archivo en base de datos
           
            # guardar pedido
            id_foto = self.cursor.getlastrowid() # recupera el último id ingresado
            sql ='''
                INSERT INTO pedidos (nombre, email, comentarios, foto) 
                VALUES (%s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data[:3]+ (id_foto,))  # ejecuto la consulta
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

    def get_data(self):
        
        sql = '''
            SELECT p.nombre, p.email, p.comentarios, c.path FROM pedidos p
            LEFT JOIN foto c
            ON p.foto = c.id
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()