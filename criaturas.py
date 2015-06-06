# -*- coding: utf-8 -*-

import MySQLdb
from gi.repository import Gtk

class Criaturas_GUI:
    def __init__(self):
        self.tabla_bd = Criaturas_BD()

class Criaturas_BD:
    host = 'localhost'
    usuario = 'conan'
    password = 'crom'
    base_datos = 'DBdeConan'
    nombre_tabla = 'Criaturas'
    
    def __init__(self):
        self.conexion = MySQLdb.connect(host = self.host, user = self.usuario, passwd = self.password, db = self.base_datos)
        self.cursor = self.conexion.cursor(MySQLdb.cursors.DictCursor)
        
        if not self.existe_tabla():
            self.crear_tabla()
            self.id = 1
        else:
            self.id = self.obtener_siguiente_id()
        
    
    def existe_tabla(self):
        self.cursor.execute("SHOW TABLES LIKE " + self.nombre_tabla)
        
        return (self.cursor.rowcount > 0)
    
    def crear_tabla(self):
        consulta = "CREATE TABLE " + self.nombre_tabla
        consulta += "(ID INT PRIMARY KEY, Nombre VARCHAR(100), Elemento VARCHAR(10), "
        consulta += "Ataque INT, Defensa INT, Velocidad INT)"
        
        self.cursor.execute()
        self.conexion.commit()
    
    def obtener_siguiente_id(self):
        self.cursor.execute("SELECT id FROM " + self.nombre_tabla)
        num_tuplas = len(self.cursor.fetchall())
        
        return num_tuplas + 1
    
    def insertar_criatura(self, nombre, elemento, ataque, defensa, velocidad):
        consulta = "INSERT INTO " + self.nombre_tabla + " VALUES(" + self.id + ",'" + nombre + "', '"
        consulta += elemento + "', " + ataque + ", " + defensa + ", " + velocidad + ")"
        self.cursor.execute(consulta)
        
        if self.cursor.rowcount == 1:
            self.id += 1
            exito = True
        else:
            exito = False
        
        return exito
    
    def seleccionar_criatura(self, id):
        self.cursor.execute("SELECT FROM " + self.nombre_tabla + " WHERE ID = " + str(id))
        
        return self.cursor.fetchone()
    
    def actualizar_criatura(self, id, nombre, elemento, ataque, defensa, velocidad):
        consulta = "UPDATE " + self.nombre_tabla + " SET Nombre = '" + nombre + "', "
        consulta += "Elemento = '" + elemento + "', Ataque = " + ataque + ", "
        consulta += "Defensa = " + defensa + ", Velocidad = " + velocidad + " "
        consulta += "WHERE ID = " + id
        
        self.cursor.execute(consulta)
        
        return (self.cursor.rowcount == 1)
    
    def eliminar_criatura(self, id)
        consulta = "DELETE FROM " + self.nombre_tabla + " WHERE ID = " + id
        
        return (self.cursor.rowcount == 1)
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

if __name__ == '__main__':
	criaturas = Criaturas_GUI()
    
