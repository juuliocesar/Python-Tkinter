from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from io import open
root = Tk()
root.title("AB-InBev")
#----Variable para los Radiobuttons
valorseleccionadodecerveza = IntVar()

#----Variables para los Checkbuttons

valorlimon = IntVar()
valortajin = IntVar()
valorsalsainglesa = IntVar()

#-----Función para guardar ordén-----------
def GuardarOrden():

	archivo = open("CervezaEscogida.txt","w")

	archivo.write("Escogió la cerveza ")
	archivo.write(str(valorseleccionadodecerveza.get()))
	archivo.write("\nLos ingredientes que escogió son: ")
	archivo.write("\nLimon: ")
	archivo.write(str(valorlimon.get()))
	archivo.write("\nTajin: ")
	archivo.write(str(valortajin.get()))
	archivo.write("\nSalsaInglesa: ")
	archivo.write(str(valorsalsainglesa.get()))
	archivo.close()



#----Función para los Radiobuttons
def imprimirselecciondecerveza():

	if valorseleccionadodecerveza.get() == 1:
		resultado.config(text="Ha seleccionado Corona Extra")

	elif valorseleccionadodecerveza.get() == 2:
		resultado.config(text="Ha seleccionado Modelo Negra")

	else:
		resultado.config(text="Ha seleccionado Barrilito")

#----Función para los checkbuttons

def Ingredientes():
	
	opcionescogida = "Su cerveza llevará: " #Variable para almacenar los ingredientes e imprimirlos

	if valorlimon.get()==1:
		opcionescogida += "Limón, "

	if valortajin.get()==1:
		opcionescogida += "Tajín, "
	
	if valorsalsainglesa.get()==1:
		opcionescogida += "Salsa Inglesa"
		
	resultadoingredientes.config(text=opcionescogida)

#----Función para el Botón

def mostrarInformacion():

	valor = messagebox.askokcancel("¡Gracias!","¿Su orden es correcta?")

	if valor == True:
		root.destroy()

#----Función para el menú

def informacion():

	messagebox.showinfo("AB-InBev 2020","\n Sistema de atención a cliente")


#----Función para el botón de imprimir (En realidad guarda la informacion)

def guardarinfo():

	fichero = filedialog.asksaveasfile(title="Imprimiendo",mode="w",defaultextension=".txt")
	if fichero is not None:
		fichero.write("Escogió la cerveza ")
		fichero.write(str(valorseleccionadodecerveza.get()))
		fichero.write("\nLos ingredientes que escogió son: ")
		fichero.write("\nLimon: ")
		fichero.write(str(valorlimon.get()))
		fichero.write("\nTajin: ")
		fichero.write(str(valortajin.get()))
		fichero.write("\nSalsaInglesa: ")
		fichero.write(str(valorsalsainglesa.get()))
		fichero.close()


Label(root, text="PROCESO DE SELECCIÓN").pack(padx=10)

Label(root, text="1. ¿Qué cerveza prefiere?").pack(pady=10)

corona = Radiobutton(root,text="Extra Corona",variable=valorseleccionadodecerveza,value=1,command=imprimirselecciondecerveza)
corona.pack(anchor="w",padx=10)
negra = Radiobutton(root,text="Modelo Negra",variable=valorseleccionadodecerveza,value=2,command=imprimirselecciondecerveza)
negra.pack(anchor="w",padx=10)
barrilito = Radiobutton(root,text="Barrilito",variable=valorseleccionadodecerveza,value=3,command=imprimirselecciondecerveza)
barrilito.pack(anchor="w",padx=10)

resultado = Label(root,text="")
resultado.pack()


Label(root, text="2. ¿Qué ingredientes desea en su cerveza?").pack()

limon = Checkbutton(root,text="Limon", variable=valorlimon,onvalue=1,offvalue=0,command=Ingredientes)
limon.pack(anchor="w",padx=10)
tajin = Checkbutton(root,text="tajin",variable=valortajin,onvalue=1,offvalue=0,command=Ingredientes)
tajin.pack(anchor="w",padx=10)
salsaInglesa = Checkbutton(root,text="Salsa Inglesa",variable=valorsalsainglesa,onvalue=1,offvalue=0,command=Ingredientes)
salsaInglesa.pack(anchor="w",padx=10)

resultadoingredientes = Label(root,text="",padx=10)
resultadoingredientes.pack()

enviar = Button(root,text="Enviar",command=mostrarInformacion)
enviar.pack(pady=10)

enviar2 = Button(root,text="Enviar2",command=GuardarOrden)
enviar2.pack(pady=10)


imprimir = Button(root,text="Imprimir Orden",command=guardarinfo)
imprimir.pack(pady=5)



barramenu = Menu(root) #Ubicación del Menu
root.config(menu=barramenu)

#Establecemos cuántos elementos tendrá el menú

archivo = Menu(barramenu,tearoff=0)
ayuda = Menu(barramenu,tearoff=0)


#Debemos decirle cuál es el texto de esos menús

barramenu.add_cascade(label="Archivo", menu=archivo)
barramenu.add_cascade(labe="Ayuda", menu=ayuda)

#Agregar subelementos 

archivo.add_command(label="Salir",command=root.destroy)
ayuda.add_command(label="Acerca de",command=informacion)


root.mainloop() #Fin del programa