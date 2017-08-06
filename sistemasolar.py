import random
import gi

#import logging


# importar modulo que contiene clase base de actividad.
'''
from sugar3.activity import activity

from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
from sugar3.activity.widgets import (
    ActivityToolbarButton,
    StopButton
)

#from ppt_utils import OPCIONES  agrega el modulo ppt_utils que contiene el diccionario llamado OPCIONES
'''
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#logger = logging.getLogger(__name__)

class Inicio(Gtk.Window):
	"""docstring for ClassName"""
	def __init__(self, *args, **kwargs):
		super(Inicio, self).__init__(*args,**kwargs)
		self.set_default_size(500,500)
		self.agregar_contenedor()
		self.PrimeraVentanaSistemaSolar()
		

	def agregar_contenedor(self):
        
		self.contenedor = Gtk.Grid()
		self.contenedor.set_row_homogeneous(False)

		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def PrimeraVentanaSistemaSolar(self):

		
		self.sistemasolar = Gtk.Button('Sistema Solar')
		self.planetas = Gtk.Button('Los Planetas')
		self.contenedor.attach(self.sistemasolar,0,0,1,1)
		self.contenedor.attach_next_to(self.planetas,self.sistemasolar,Gtk.PositionType.RIGHT,1,1)	
		self.sistemasolar.connect('clicked',self.SegundaVentanaSistemaSolar)
		self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
		

	def SegundaVentanaSistemaSolar(self,btn):

		#self.gtk_window_set_title (title="hola")

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.boton_definicion= Gtk.Button('Definicion')
		self.boton_galeria = Gtk.Button('Galeria')
		self.contenedor.attach(self.boton_definicion,0,0,1,1)
		self.contenedor.attach_next_to(self.boton_galeria,self.boton_definicion,Gtk.PositionType.RIGHT,1,1)

		self.contenedor.show_all()
		self.boton_definicion.connect('clicked',self.TerceraVentanaSistemaSolar)
		self.boton_galeria.connect('clicked',self.TerceraVentanaSistemaSolar)


	def TerceraVentanaSistemaSolar(self,b):
		
		for widget in self.contenedor:
			self.contenedor.remove(widget)
		
	
		self.boton_inicio_sistemasolar = Gtk.Button('Inicio')
		self.label_sistemasolar = Gtk.Label('Numero de veces')
		

	



if __name__ == '__main__':
	init = Inicio()
	init.show_all()
	Gtk.main()
		







