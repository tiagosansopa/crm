#Proyecto 2 Bases de Datos
#Pablo Barreno, 14159
#Santiago Solorzano, 14619
#Olga Cobaquil, 

import kivy
import psycopg2

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup 
from kivy.loader import Loader
from kivy.lang import Builder
from kivy.app import App 


class CRM(App):
    def build(self):
        self.layoutMaster = FloatLayout(size=(100, 100))
        
		#Titulo
		
        lbl0 = Label(text="CRM",font_size='20sp',pos_hint={'x': .45, 'y': 0.95},size_hint=(None,None),size=(90,30))
        self.layoutMaster.add_widget(lbl0)
		
		#Menu
		
        menu = FloatLayout(pos_hint={'x': .0010, 'y': 0.73},size_hint=(None,None),size=(600,100))
		
		#Cliente Menu
        clientMenu = Label(text="Cliente",pos_hint={'x': .0010, 'y': 0.90},size_hint=(None,None),size=(90,30))
        menu.add_widget(clientMenu)
		
        nuevoMenu = Button(text="Nuevo",pos_hint={'x': .15, 'y': 0.90},size_hint=(None,None),size=(90,30))
        nuevoMenu.bind(on_press=self.mostrarNuevoCliente)
        menu.add_widget(nuevoMenu)
		
        actualizarMenu = Button(text="Actualizar",pos_hint={'x': .3, 'y': 0.90},size_hint=(None,None),size=(90,30))
        actualizarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(actualizarMenu)
		
        eliminarMenu = Button(text="Eliminar",pos_hint={'x': .45, 'y': 0.90},size_hint=(None,None),size=(90,30))
        eliminarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(eliminarMenu)
		
        buscarMenu = Button(text="Buscar",pos_hint={'x': .6, 'y': 0.90},size_hint=(None,None),size=(90,30))
        buscarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(buscarMenu)
		
        redesSocialesMenu = Button(text="Redes Sociales",pos_hint={'x':.9, 'y': 0.90},size_hint=(None,None),size=(150,30))
        redesSocialesMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(redesSocialesMenu)
        
		#Proveedor Menu
        clientMenu = Label(text="Proveedor",pos_hint={'x': .0010, 'y': 0.60},size_hint=(None,None),size=(90,30))
        menu.add_widget(clientMenu)
		
        nuevoMenu = Button(text="Nuevo",pos_hint={'x': .15, 'y': 0.60},size_hint=(None,None),size=(90,30))
        nuevoMenu.bind(on_press=self.mostrarNuevoCliente)
        menu.add_widget(nuevoMenu)
		
        actualizarMenu = Button(text="Actualizar",pos_hint={'x': .3, 'y': 0.60},size_hint=(None,None),size=(90,30))
        actualizarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(actualizarMenu)
		
        eliminarMenu = Button(text="Eliminar",pos_hint={'x': .45, 'y': 0.60},size_hint=(None,None),size=(90,30))
        eliminarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(eliminarMenu)
		
        buscarMenu = Button(text="Buscar",pos_hint={'x': .6, 'y': 0.60},size_hint=(None,None),size=(90,30))
        buscarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(buscarMenu)
        
		#Ventas Menu
        clientMenu = Label(text="Ventas",pos_hint={'x': .0010, 'y': 0.30},size_hint=(None,None),size=(90,30))
        menu.add_widget(clientMenu)
		
        nuevoMenu = Button(text="Nuevo",pos_hint={'x': .15, 'y': 0.30},size_hint=(None,None),size=(90,30))
        nuevoMenu.bind(on_press=self.mostrarNuevoCliente)
        menu.add_widget(nuevoMenu)
		
        actualizarMenu = Button(text="Actualizar",pos_hint={'x': .3, 'y': 0.30},size_hint=(None,None),size=(90,30))
        actualizarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(actualizarMenu)
		
        eliminarMenu = Button(text="Eliminar",pos_hint={'x': .45, 'y': 0.30},size_hint=(None,None),size=(90,30))
        eliminarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(eliminarMenu)
		
        buscarMenu = Button(text="Buscar",pos_hint={'x': .6, 'y': 0.30},size_hint=(None,None),size=(90,30))
        buscarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(buscarMenu)
		
        #Abonos
        clientMenu = Label(text="Abonos",pos_hint={'x': .0010, 'y': 0.01},size_hint=(None,None),size=(90,30))
        menu.add_widget(clientMenu)
		
        nuevoMenu = Button(text="Nuevo",pos_hint={'x': .15, 'y': 0.01},size_hint=(None,None),size=(90,30))
        nuevoMenu.bind(on_press=self.mostrarNuevoCliente)
        menu.add_widget(nuevoMenu)
		
        actualizarMenu = Button(text="Actualizar",pos_hint={'x': .3, 'y': 0.01},size_hint=(None,None),size=(90,30))
        actualizarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(actualizarMenu)
		
        eliminarMenu = Button(text="Eliminar",pos_hint={'x': .45, 'y': 0.01},size_hint=(None,None),size=(90,30))
        eliminarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(eliminarMenu)
		
        buscarMenu = Button(text="Buscar",pos_hint={'x': .6, 'y': 0.01},size_hint=(None,None),size=(90,30))
        buscarMenu.bind(on_press=self.mostrarBusqueda)
        menu.add_widget(buscarMenu)
		
		
		#====================================================================================================================
		
        self.layoutMaster.add_widget(menu)
		
        #Formulario Cliente Nuevo
        self.formularioNuevo = FloatLayout(pos_hint={'x': .020, 'y': 0.0},size_hint=(None,None),size=(800,400))
		
        lbl1 = Label(text="ID",font_size='16sp',pos_hint={'x': .001, 'y': 0.9},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl1)
        self.ID = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.90},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.ID)
		
        lbl2 = Label(text="Nombre",font_size='16sp',pos_hint={'x': .001, 'y': 0.80},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl2)
        self.Nombre = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.80},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.Nombre)
		
        lbl3 = Label(text="Apellido",font_size='16sp',pos_hint={'x': .001, 'y': 0.70},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl3)
        self.apellido = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.70},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.apellido)
		
        lbl3 = Label(text="Telefono",font_size='16sp',pos_hint={'x': .001, 'y': 0.60},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl3)
        self.telefono = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.60},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.telefono)
		
        lbl4 = Label(text="Direccion",font_size='16sp',pos_hint={'x': .001, 'y': 0.50},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl4)
        self.direccion = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.50},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.direccion)
		
        lbl5 = Label(text="Pais",font_size='16sp',pos_hint={'x': .001, 'y': 0.40},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl5)
        self.nacionalidad = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.40},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.nacionalidad)
		
        lbl6 = Label(text="DPI",font_size='16sp',pos_hint={'x': .001, 'y': 0.30},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl6)
        self.dpi = TextInput(text='', multiline=False,pos_hint={'x': 0.14, 'y': 0.30},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.dpi)
		
        lbl7 = Label(text="NIT",font_size='16sp',pos_hint={'x': .001, 'y': 0.20},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl7)
		
        self.nit = TextInput(text='', multiline=False,pos_hint={'x': .14, 'y': 0.20},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.nit)
		
        lbl8 = Label(text="Foto",font_size='16sp',pos_hint={'x': .001, 'y': 0.10},size_hint=(None,None),size=(90,30))
        self.formularioNuevo.add_widget(lbl8)
		
        self.fotodir= TextInput(text='', multiline=False,pos_hint={'x': .14, 'y': 0.10},size_hint=(None,None),size=(200,30))
        self.formularioNuevo.add_widget(self.fotodir)
		
        reload = Button(text="Reload",pos_hint={'x': 0.4, 'y': 0.1},size_hint=(None,None),size=(90,30))
        reload.bind(on_press=self.recargarFoto)
        self.formularioNuevo.add_widget(reload)
		
		
		#Foto
        self.foto = AsyncImage(source="def.jpg",pos_hint={'x': .65, 'y': 0.40}, size_hint=(None,None), size=(180,229))
        self.formularioNuevo.add_widget(self.foto)
		
        ingresar = Button(text="Ingresar",pos_hint={'x': 0.76, 'y': 0.1},size_hint=(None,None),size=(90,30))
        ingresar.bind(on_press=self.ingresarClienteNuevo)
        self.formularioNuevo.add_widget(ingresar)
		
        self.layoutMaster.add_widget(self.formularioNuevo)
        return self.layoutMaster
		
    def recargarFoto(self,btn):
        self.foto.source=self.fotodir.text+".jpg"
		
    def ingresarClienteNuevo(self,btn):
        cadenaConexion = "host='localhost' \dbname='test' user='postgres' password='jkl'"
        obj=psycopg2.connect("host='localhost' dbname='test' user='postgres' password='jkl'")
        objCursor=obj.cursor();
        objCursor.execute("INSERT INTO tblTest VALUES ("+self.Nombre.text+");")
        obj.commit()
        objCursor.execute("SELECT * FROM tblTest;")
        registros=objCursor.fetchall()
        print(registros)
    
    def mostrarBusqueda(self,btn):
        #self.add_widget()
        self.layoutMaster.remove_widget(self.formularioNuevo)
    
    def mostrarNuevoCliente(self,btn):
        self.layoutMaster.add_widget(self.formularioNuevo)
        #self.remove_widget()
	    
if __name__ == "__main__":
    CRM().run()