# -*- coding: utf-8 -*-

import MySQLdb
from gi.repository import Gtk

class Criaturas_BD:
    host = 'localhost'
    usuario = 'conan'
    password = 'crom'
    base_datos = 'DBdeConan'
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
        id = self.cursor.fetchone()
        
        return id["ID"] + 1
    
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

class Criaturas_GUI:
    def __init__(self):
        # Conexion al modelo de datos
        self.tabla_bd = Criaturas_BD()
        
        # Conexion a la interfaz
        self.builder = Gtk.Builder()
        self.builder.add_from_file("critaturas.glade")
        self.handlers = {"onExit": Gtk.main_quit,
                        "onMenuCreate": self.onMenuCreate,
						"onMenuSelect": self.onMenuSelect,
                        "onMenuUpdate": self.onMenuUpdate,
                        "onMenuDelete": self.onMenuDelete,
                        "onActionButton": self.onActionButton,
                        "onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout}
        
        self.inicializar_combo_boxes()
        self.actualizar_combo_box_id()
        
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("windowCriaturas")
        self.window.show_all()
        
        # Menu inicial
        self.menu = "Crear"
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(False)
    
    def inicializar_combo_boxes(self):
        renderer_text = Gtk.CellRendererText()
        combobox = self.builder.get_object("comboBoxId")
        combobox.pack_start(renderer_text, True)
        combobox.add_attribute(renderer_text, "text", 0)
        print combobox.get_entry_text_column()
        
        renderer_text = Gtk.CellRendererText()
        combobox = self.builder.get_object("comboBoxElemento")
        combobox.pack_start(renderer_text, True)
        combobox.add_attribute(renderer_text, "text", 0)
        print combobox.get_entry_text_column()
    
    def actualizar_combo_box_id(self):
        combobox = self.builder.get_object("comboBoxId")
        combobox.remove_all()
        
        ids = self.tabla_bd.seleccionar_ids_criaturas()
        
        if len(ids) > 0:
            for id in ids:
                combobox.append(str(id["ID"]), str(id["ID"]))
            
    
    def onMenuCreate(self, menu):
        self.limpiar_campos()
        self.menu = menu.get_label()
        
        campo = self.builder.get_object("labelTitulo")
        campo.set_text("Creación de criatura")
        campo = self.builder.get_object("labelDescripcion")
        campo.set_text("Introduzca los datos para crear una nueva criatura.")
        campo = self.builder.get_object("buttonAccion")
        campo.set_label(menu.get_label())
        
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(False)
        campo = self.builder.get_object("entryNombre")
        campo.set_property('editable', True)
        campo = self.builder.get_object("comboBoxElemento")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonAtaque")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_sensitive(True)
        
    def onMenuSelect(self, menu):
        self.limpiar_campos()
        self.menu = menu.get_label()
        
        campo = self.builder.get_object("labelTitulo")
        campo.set_text("Obtención de criatura")
        campo = self.builder.get_object("labelDescripcion")
        campo.set_text("Seleccione el identificador para consultar los datos de la criatura.")
        campo = self.builder.get_object("buttonAccion")
        campo.set_label(menu.get_label())
        
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(True)
        campo = self.builder.get_object("entryNombre")
        campo.set_property('editable', False)
        campo = self.builder.get_object("comboBoxElemento")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonAtaque")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_sensitive(False)
        
    def onMenuUpdate(self, menu):
        self.limpiar_campos()
        self.menu = menu.get_label()
        
        campo = self.builder.get_object("labelTitulo")
        campo.set_text("Actualización de criatura")
        campo = self.builder.get_object("labelDescripcion")
        campo.set_text("Seleccione el identificador de la criatura e introduzca los datos para actualizar la criatura.")
        campo = self.builder.get_object("buttonAccion")
        campo.set_label(menu.get_label())
        
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(True)
        campo = self.builder.get_object("entryNombre")
        campo.set_property('editable', True)
        campo = self.builder.get_object("comboBoxElemento")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonAtaque")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_sensitive(True)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_sensitive(True)
        
    def onMenuDelete(self, menu):
        self.limpiar_campos()
        self.menu = menu.get_label()
        
        campo = self.builder.get_object("labelTitulo")
        campo.set_text("Eliminación de criatura")
        campo = self.builder.get_object("labelDescripcion")
        campo.set_text("Introduzca el identificador para eliminar los datos de la criatura.")
        campo = self.builder.get_object("buttonAccion")
        campo.set_label(menu.get_label())
        
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(True)
        campo = self.builder.get_object("entryNombre")
        campo.set_property('editable', False)
        campo = self.builder.get_object("comboBoxElemento")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonAtaque")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_sensitive(False)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_sensitive(False)
        
    def onActionButton(self, boton):
        if self.menu == "Crear":
            nombre = self.builder.get_object("entryNombre")
            elemento = self.builder.get_object("comboBoxElemento")
            ataque = self.builder.get_object("spinButtonAtaque")
            defensa = self.builder.get_object("spinButtonDefensa")
            velocidad = self.builder.get_object("spinButtonVelocidad")
            
            self.tabla_bd.insertar_criatura(nombre.get_text(), elemento.get_active_text(), ataque.get_value_as_int(), defensa.get_value_as_int(), velocidad.get_value_as_int())
            
            self.limpiar_campos()
            self.actualizar_combo_box_id()
        elif self.menu == "Obtener":
            id = self.builder.get_object("comboBoxId")
            
            criatura = self.tabla_bd.seleccionar_criatura(id.get_active_text())
            nombre = self.builder.get_object("entryNombre")
            nombre.set_text(criatura["Nombre"])
            elemento = self.builder.get_object("comboBoxElemento")
            elemento.set_active_id(self.obtener_indice_elemento_combo_box(criatura["Elemento"]))
            ataque = self.builder.get_object("spinButtonAtaque")
            ataque.set_value(criatura["Ataque"])
            defensa = self.builder.get_object("spinButtonDefensa")
            defensa.set_value(criatura["Defensa"])
            velocidad = self.builder.get_object("spinButtonVelocidad")
            velocidad.set_value(criatura["Velocidad"])
        elif self.menu == "Actualizar":
            id = self.builder.get_object("comboBoxId")
            nombre = self.builder.get_object("entryNombre")
            elemento = self.builder.get_object("comboBoxElemento")
            ataque = self.builder.get_object("spinButtonAtaque")
            defensa = self.builder.get_object("spinButtonDefensa")
            velocidad = self.builder.get_object("spinButtonVelocidad")
            
            self.tabla_bd.actualizar_criatura(id.get_active_text(), nombre.get_text(), elemento.get_active_text(), ataque.get_value_as_int(), defensa.get_value_as_int(), velocidad.get_value_as_int())
        elif self.menu == "Eliminar":
            id = self.builder.get_object("comboBoxId")
            
            self.tabla_bd.eliminar_criatura(id.get_active_text())
            
            self.actualizar_combo_box_id()
    
    def obtener_indice_elemento_combo_box(self, elemento):
        if elemento == "Aire":
            return "0"
        elif elemento == "Agua":
            return "1"
        elif elemento == "Fuego":
            return "2"
        elif elemento == "Tierra":
            return "3"
    
    def limpiar_campos(self):
        campo = self.builder.get_object("comboBoxId")
        campo.set_active(-1)
        campo = self.builder.get_object("entryNombre")
        campo.set_text("")
        campo = self.builder.get_object("comboBoxElemento")
        campo.set_active(-1)
        campo = self.builder.get_object("spinButtonAtaque")
        campo.set_value(-1)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_value(-1)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_value(-1)
    
    def onAboutDialog(self, *args):
        self.acerca_de = self.builder.get_object("acercaDe")
        self.acerca_de.show_all()
    def onCloseAbout(self, *args):
        self.acerca_de = self.builder.get_object("acercaDe")
        self.acerca_de.hide()

def main():
    ventana_criaturas = Criaturas_GUI()
    Gtk.main()
    
    return 0

if __name__ == '__main__':
    #criaturas = Criaturas_BD()
    #criaturas.insertar_criatura("nombre", "elemento", 0, 0, 0)
    #criaturas.actualizar_criatura(1, "Laura", "Agua", 1, 2, 3)
    #criaturas.seleccionar_criatura(1)
    #criaturas.eliminar_criatura(1)
    #criaturas.seleccionar_criatura(1)
    #criaturas.cerrar_conexion()
    
    main()
