import random
import gi
import logging
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import (ActivityToolbarButton, StopButton)

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
logger = logging.getLogger(__name__)


class sistemasolar(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.agregar_toolbar()
        self.agregar_contenedor()
        self.PrimeraVentanaSistemaSolar()
        

    def agregar_toolbar(self):
        toolbar_box = ToolbarBox()
        aplicacion_toolbar_boton = ActivityToolbarButton(self)
        aplicacion_stop_boton = StopButton(self)
        toolbar_box.toolbar.insert(aplicacion_toolbar_boton, 0)
        aplicacion_toolbar_boton.show()
        toolbar_box.toolbar.insert(aplicacion_stop_boton, -1)
        aplicacion_stop_boton.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def agregar_contenedor(self):
        self.canvas = Gtk.Grid()
        self.add(self.canvas)

    def PrimeraVentanaSistemaSolar(self):
        self.sistemasolar = Gtk.Button('Sistema Solar')
        self.planetas = Gtk.Button('Planetas')
        self.canvas.attach(self.planta, 0, 0, 1, 1)
        self.canvas.attach_next_to(
            self.planetas,
            self.sistemasolar,
            Gtk.PositionType.RIGHT,
            1,
            1
        )
        self.sistemasolar.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.canvas.show_all()

    def SegundaVentanaSistemaSolar(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_definicion = Gtk.Label('Definicion')
        self.label_galeria = Gtk.Label('galeria')

        self.boton_siguiente = Gtk.Button('Siguiente')
        self.canvas.attach(self.galeria,0,0,1,1)
        self.canvas.attach_next_to(self.label_definicion,self.label_galeria,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach(self.boton_siguiente,0,2,1,1)

        self.canvas.show_all()
        self.boton_siguiente.connect('clicked',self.TerceraVentanaSistemaSolar)
        


    def TerceraVentanaSistemaSolar(self,b):
        
        for widget in self.canvas:
            self.canvas.remove(widget)
        
    
        self.boton_definicion = Gtk.Button('Inicio')
        self.label_definicion = Gtk.Label('Numero de veces')
        self.numero_de_entrada = Gtk.Entry() 
    


  