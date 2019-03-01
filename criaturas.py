# -*- coding: utf-8 -*-

from clases.criaturas_gui import Criaturas_GUI
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def main():
    ventana_criaturas = Criaturas_GUI()
    Gtk.main()
    
    return 0

if __name__ == '__main__':
    main()
