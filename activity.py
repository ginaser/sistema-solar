import gi
import logging

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox


from sugar3.activity.widgets import(
	ActivityToolbarButton,
	StopButton)


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

logger = logging.getLogger(__name__)

class SistemaSolar(activity.Activity):

	def __init__(self, handle):
		activity.Activity.__init__(self, handle)
		self.max_participants =1

		self.agregar_toolbar()
		self.agregar_canvas()
		


	def agregar_toolbar(self):
		toolbar_box = ToolbarBox()
		
		activity_toolbar_button = ActivityToolbarButton(self)
		activity_stop_button = StopButton(self)

		toolbar_box.toolbar.insert(activity_toolbar_button, 0)
		activity_toolbar_button.show()

		toolbar_box.toolbar.insert(activity_stop_button, -1)
		activity_stop_button.show()

		self.set_toolbar_box(toolbar_box)
		toolbar_box.show()

	def agregar_canvas(self):
		self.canvas = Gtk.ScrolledWindow()
		self.inner_canvas = Gtk.VBox()
		self.canvas.add(self.inner_canvas)

		self.agregar_texto_nombre()
		self.agregar_BotonNombre()
		self.agregar_label_nombre()
		self.canvas.show_all()

	def agregar_BotonNombre(self):
		self.nombre = Gtk.Grid()
		self.nombre.set_column_homogeneous(True)

		self.boton_hola = Gtk.Button(label = "Click para ingresar su nombre")
		self.boton_hola.connect('clicked', self.cambiar_nombre)
		self.nombre.attach(self.boton_hola, 0,3,1,1)		
		self.inner_canvas.pack_start(self.nombre, False, False, 0)

	def agregar_texto_nombre(self):
		self.nombreag = Gtk.Grid()
		self.nombreag.set_column_homogeneous(True)

		texto_nombre = Gtk.Entry()
		self.nombreag.attach(texto_nombre, 0,3,2,1)

		self.inner_canvas.pack_start(self.nombreag, False, False, 0)

	def agregar_label_nombre(self):
		self.labelcontedor = Gtk.Grid()
		self.labelcontedor.set_column_homogeneous(True)
		
		self.lnombre = Gtk.Label('El sistema solar es el conjunto formado por el Sol')
		self.labelcontedor.attach(self.lnombre, 0,4,1,1)

		self.inner_canvas.pack_start(self.labelcontedor, False, False, 0)

	def cambiar_nombre(self, btn):
		self.lnombre.set_markup(self.texto_nombre.get_text())


