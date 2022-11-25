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

    def get_regiones(self):
        
        sql = f'''

        SELECT * FROM region;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comunas(self, id):
        
        sql = f'''

        SELECT comuna_id, nombre FROM comuna WHERE region_id = {id};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_comuna_latlong(self, id):
        sql = f'''

        SELECT nombre, latitud, longitud FROM comuna WHERE comuna_id = {id};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    

        