# -*- coding: utf-8 -*-

import MySQLdb

class Criaturas_BD:
    host = 'localhost'
    usuario = 'usuario'
    password = 'contra'
    base_datos = 'Criaturas'
    nombre_tabla = 'Criatura'
    
    def __init__(self):
        self.conexion = MySQLdb.connect(host = self.host, user = self.usuario, passwd = self.password, db = self.base_datos)
        self.cursor = self.conexion.cursor(MySQLdb.cursors.DictCursor)
        
        if not self.existe_tabla():
            self.crear_tabla()
            self.id = 1
        else:
            self.id = self.obtener_siguiente_id()
        
    
    def existe_tabla(self):
        self.cursor.execute("SHOW TABLES LIKE '" + self.nombre_tabla + "'")
        
        return (self.cursor.rowcount > 0)
    
    def crear_tabla(self):
        consulta = "CREATE TABLE " + self.nombre_tabla
        consulta += "(ID INT PRIMARY KEY, Nombre VARCHAR(100), Elemento VARCHAR(10), "
        consulta += "Ataque INT, Defensa INT, Velocidad INT)"
        self.cursor.execute(consulta)
        
        self.conexion.commit()
    
    def obtener_siguiente_id(self):
        self.cursor.execute("SELECT MAX(ID) AS ID FROM " + self.nombre_tabla)
        tupla = self.cursor.fetchone()
        
        if tupla["ID"] != None:
            return tupla["ID"] + 1
        else:
            return 1
    
    def insertar_criatura(self, nombre, elemento, ataque, defensa, velocidad):
        consulta = "INSERT INTO " + self.nombre_tabla + " VALUES(" + str(self.id) + ",'" + nombre + "', "
        consulta += "'" + elemento + "', " + str(ataque) + ", " + str(defensa) + ", " + str(velocidad) + ")"
        self.cursor.execute(consulta)
        
        self.conexion.commit()
        
        if self.cursor.rowcount == 1:
            self.id += 1
            exito = True
        else:
            exito = False
        
        return exito
    
    def seleccionar_criatura(self, id):
        self.cursor.execute("SELECT * FROM " + self.nombre_tabla + " WHERE ID = " + str(id))
        
        return self.cursor.fetchone()
        
    def seleccionar_ids_criaturas(self):
        self.cursor.execute("SELECT ID FROM " + self.nombre_tabla)
        
        return self.cursor.fetchall()
    
    def actualizar_criatura(self, id, nombre, elemento, ataque, defensa, velocidad):
        consulta = "UPDATE " + self.nombre_tabla + " SET Nombre = '" + nombre + "', "
        consulta += "Elemento = '" + elemento + "', Ataque = " + str(ataque) + ", "
        consulta += "Defensa = " + str(defensa) + ", Velocidad = " + str(velocidad) + " "
        consulta += "WHERE ID = " + str(id)
        self.cursor.execute(consulta)
        
        self.conexion.commit()
        
        return (self.cursor.rowcount == 1)
    
    def eliminar_criatura(self, id):
        self.cursor.execute("DELETE FROM " + self.nombre_tabla + " WHERE ID = " + str(id))
        
        self.conexion.commit()
        
        return (self.cursor.rowcount == 1)
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
