###Formulario de Registe 
## 3MLIDTS-Josseline

from ast import Delete
from multiprocessing import Value
import tkinter as tk 

###definicion de funciones 
def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
    
def borrar():
    limpiar_campos()
    
def guardar_valores():
    ###obtener valores desde los entrys
    nombres= tbNombre.get()
    apellidos= tbApellidos.get()
    edad= tbEdad.get()
    estatura= tbEstatura.get()
    telefono= tbTelefono.get()
    ###obetener el genero del RadioButton
    genero= ""
    if var_genero.get()==1:
        genero= "Masculino"
    elif var_genero.get()==2:  
        genero= "Femenino" 
    datos ="Nombres"+ nombres + "\n"+"Apellidos:" + apellidos + "\n"+"Edad:" + edad+"\n"+"Estatura:" + estatura+"\n"+"Telefono"+ telefono +"Genero:"+genero+"\n"
    
    
## Creacion de ventana
ventana = tk.Tk() 
ventana.geometry("720x500") 
ventana.title("Formulario Vr.01")
##Crear variable para RadioButton
var_genero = tk.IntVar() ##checked en python, variable local

## Creacion deetiquetas y campos de entrada 
IbNombre= tk.Label(ventana, text="Nombres :") 
## Nueva propiedad de ordenamiento 
IbNombre.pack()
tbNombre= tk.Entry()
tbNombre.pack() ##Va apilando los textos en vertical y orden

IbApellidos= tk.Label(ventana, text="Apellidos :") 
IbApellidos.pack()
tbApellidos= tk.Entry()
tbApellidos.pack() 

IbTelefono= tk.Label(ventana, text="Telefono :") 
IbTelefono.pack()
tbTelefono= tk.Entry()
tbTelefono.pack()

IbEdad= tk.Label(ventana, text="Edad :") 
IbEdad.pack()
tbEdad= tk.Entry() 
tbEdad.pack()

IbEstatura= tk.Label(ventana, text="Estatura :")  
IbEstatura.pack()
tbEstatura= tk.Entry() 
tbEstatura.pack()

IbGenero= tk.Label(ventana, text="Genero")  
IbGenero.pack()  
rbMasculino= tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value=1 )
rbMasculino.pack() 

IbGenero= tk.Label(ventana, text="Genero")  
rbFemenino= tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value=2 ) 
rbFemenino.pack() 

##creacion de botones
btnBorrar= tk.Button(ventana, text= "Borrar Valores", command=borrar)
btnBorrar.pack() 
btnGuardar = tk.Button(ventana, text = "Guardar")
btnGuardar.pack() 


ventana.mainloop()

