# -*- coding: utf-8 -*-

from clases.criaturas_bd import Criaturas_BD
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Criaturas_GUI:
    def __init__(self):
        # Conexion al modelo de datos
        self.tabla_bd = Criaturas_BD()
        
        # Conexion a la interfaz
        self.builder = Gtk.Builder()
        self.builder.add_from_file("critaturas.glade")
        self.handlers = { "onExit": Gtk.main_quit,
                        "onMenuCreate": self.onMenuCreate,
						"onMenuSelect": self.onMenuSelect,
                        "onMenuUpdate": self.onMenuUpdate,
                        "onMenuDelete": self.onMenuDelete,
                        "onActionButton": self.onActionButton,
                        "onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout,
                        "onClosePopUp": self.onClosePopUp,
                        "onIdChanged": self.onIdChanged
                        }
        
        self.actualizar_combo_box_id()
        
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("windowCriaturas")
        self.window.show_all()
        
        # Menu inicial
        self.menu = "Crear"
        campo = self.builder.get_object("comboBoxId")
        campo.set_sensitive(False)
    
    def actualizar_combo_box_id(self):
        combobox = self.builder.get_object("comboBoxId")
        combobox.remove_all()
        
        ids = self.tabla_bd.seleccionar_ids_criaturas()
        
        if len(ids) > 0:
            for id in ids:
                combobox.append(str(id["ID"]), str(id["ID"]))
            
    
    def onMenuCreate(self, menu):
        self.limpiar_datos_criatura()
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
        campo.set_property('editable', True)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_property('editable', True)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_property('editable', True)
        
    def onMenuSelect(self, menu):
        self.limpiar_datos_criatura()
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
        campo.set_property('editable', False)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_property('editable', False)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_property('editable', False)
        
    def onMenuUpdate(self, menu):
        self.limpiar_datos_criatura()
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
        campo.set_property('editable', True)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_property('editable', True)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_property('editable', True)
        
    def onMenuDelete(self, menu):
        self.limpiar_datos_criatura()
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
        campo.set_property('editable', False)
        campo = self.builder.get_object("spinButtonDefensa")
        campo.set_property('editable', False)
        campo = self.builder.get_object("spinButtonVelocidad")
        campo.set_property('editable', False)
        
    def onIdChanged(self, combo_box):
        if (self.menu == "Actualizar" or self.menu == "Eliminar") and combo_box.get_active() != -1:
            self.rellenar_datos_criatura(combo_box.get_active_text())
        elif (self.menu == "Actualizar" or self.menu == "Eliminar") and combo_box.get_active() == -1:
            self.limpiar_datos_criatura()
        
    def onActionButton(self, boton):
        if self.menu == "Crear":
            nombre = self.builder.get_object("entryNombre")
            elemento = self.builder.get_object("comboBoxElemento")
            ataque = self.builder.get_object("spinButtonAtaque")
            defensa = self.builder.get_object("spinButtonDefensa")
            velocidad = self.builder.get_object("spinButtonVelocidad")
            
            if nombre.get_text() == "" or elemento.get_active() == -1:
                titulo = "Advertencia"
                mensaje = "Por favor, indique el nombre y el elemento de la criatura"
                self.mostrar_pop_up(titulo, mensaje)
            else:
                self.tabla_bd.insertar_criatura(nombre.get_text(), elemento.get_active_text(), ataque.get_value_as_int(), defensa.get_value_as_int(), velocidad.get_value_as_int())
                
                titulo = "Información"
                mensaje = "Se ha creado la información de la criatura"
                self.mostrar_pop_up(titulo, mensaje)
                
                self.limpiar_datos_criatura()
                self.actualizar_combo_box_id()
        elif self.menu == "Obtener":
            id = self.builder.get_object("comboBoxId")
            
            if id.get_active() == -1:
                titulo = "Advertencia"
                mensaje = "Por favor, seleccione el número identificador de la criatura para consultar sus datos"
                self.mostrar_pop_up(titulo, mensaje)
            else:
                self.rellenar_datos_criatura(id.get_active_text())
        elif self.menu == "Actualizar":
            id = self.builder.get_object("comboBoxId")
            
            if id.get_active() == -1:
                titulo = "Advertencia"
                mensaje = "Por favor, seleccione el número identificador de la criatura para actualizar sus datos"
                self.mostrar_pop_up(titulo, mensaje)
            else:
                nombre = self.builder.get_object("entryNombre")
                elemento = self.builder.get_object("comboBoxElemento")
                ataque = self.builder.get_object("spinButtonAtaque")
                defensa = self.builder.get_object("spinButtonDefensa")
                velocidad = self.builder.get_object("spinButtonVelocidad")
                
                self.tabla_bd.actualizar_criatura(id.get_active_text(), nombre.get_text(), elemento.get_active_text(), ataque.get_value_as_int(), defensa.get_value_as_int(), velocidad.get_value_as_int())
                
                titulo = "Información"
                mensaje = "Se ha actualizado la información de la criatura"
                self.mostrar_pop_up(titulo, mensaje)
        elif self.menu == "Eliminar":
            id = self.builder.get_object("comboBoxId")
            
            if id.get_active() == -1:
                titulo = "Advertencia"
                mensaje = "Por favor, seleccione el número identificador de la criatura para eliminar sus datos"
                self.mostrar_pop_up(titulo, mensaje)
            else:
                self.tabla_bd.eliminar_criatura(id.get_active_text())
                
                titulo = "Información"
                mensaje = "Se ha eliminado la información de la criatura"
                self.mostrar_pop_up(titulo, mensaje)
                
                self.actualizar_combo_box_id()
        
    def onAboutDialog(self, *args):
        self.acerca_de = self.builder.get_object("acercaDe")
        self.acerca_de.show_all()
        
    def onCloseAbout(self, *args):
        self.acerca_de = self.builder.get_object("acercaDe")
        self.acerca_de.hide()
    
    def onClosePopUp(self, *args):
        self.pop_up = self.builder.get_object("popUp")
        self.pop_up.hide()
    
    def obtener_indice_elemento_combo_box(self, elemento):
        if elemento == "Aire":
            return "0"
        elif elemento == "Agua":
            return "1"
        elif elemento == "Fuego":
            return "2"
        elif elemento == "Tierra":
            return "3"
        
    def limpiar_datos_criatura(self):
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
    
    def mostrar_pop_up(self, titulo, mensaje):
        campo = self.builder.get_object("tituloPopUp")
        campo.set_text(titulo)
        
        campo = self.builder.get_object("mensajePopUp")
        campo.set_text(mensaje)
        
        self.pop_up = self.builder.get_object("popUp")
        self.pop_up.show_all()
    
    def rellenar_datos_criatura(self, id):
        criatura = self.tabla_bd.seleccionar_criatura(id)
        
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
