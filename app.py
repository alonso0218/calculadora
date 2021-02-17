from tkinter import * # importamos todo de tkinter
ventana= Tk()

ventana.tittle("CALCULADORA PYTHON")#nombre paa nuestra calculadora
en_texto= Entry(ventana,font="calibri 20") #entrada de texto y tipo de fuente con tamano
en_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
 
i = 0 #creamos una variable global para que el indice de la calcualdora aumente 
#creamos las funciones del la calculadora

def intro_boton(valor):
    global i
    en_texto.insert(0,valor)
    i += 1 # con esto le indicmos que agregue los numeros a la derecha del numero que ya esta ingresado

def borrar ():#creamos la funcion de borrar 
    en_texto.delete(0,END )#le pasamos los parametros para que borre todo desde el pincipio hasta el final
    i=0 

# usamos la funcion de python "EVAL" que nos ayuda a hacer las operaciones de forma mas practica

def operaciones():
    ecuacion=en_texto.get()#obtenemos la operacion
    resultado=eval(ecuacion)#hacemos la operacion
    en_texto.delete(0,END)#borramos todo desde el principio hasta el final
    en_texto.insert(0,resultado)#mostramos el resultado por pantalla
    i=0 # dejamos nuestro indice en cero para seguir ingresando numeros para mas operaciones 
#creamos los botones de la calculadora
boton1 =  Button(ventana,text="1",width=5,height=2,COMMAND=lambda:intro_boton(1))
boton2 =  Button(ventana,text="2",width=5,height=2,COMMAND=lambda:intro_boton(2))
boton3 =  Button(ventana,text="3",width=5,height=2,COMMAND=lambda:intro_boton(3))
boton4 =  Button(ventana,text="4",width=5,height=2,COMMAND=lambda:intro_boton(4))
boton5 =  Button(ventana,text="5",width=5,height=2,COMMAND=lambda:intro_boton(5))
boton6 =  Button(ventana,text="6",width=5,height=2,COMMAND=lambda:intro_boton(6))
boton7 =  Button(ventana,text="7",width=5,height=2,COMMAND=lambda:intro_boton(7))
boton8 =  Button(ventana,text="8",width=5,height=2,COMMAND=lambda:intro_boton(8))
boton9 =  Button(ventana,text="9",width=5,height=2,COMMAND=lambda:intro_boton(9))
boton0 =  Button(ventana,text="0",width=13,height=2,COMMAND=lambda:intro_boton(0))

boton_borrar =  Button(ventana,text="AC",width=5,height=2,COMMAND=lambda:borrar())
boton_parentesis1 =  Button(ventana,text="(",width=5,height=2,COMMAND=lambda:intro_boton("("))
boton0_parentesis2 =  Button(ventana,text=")",width=5,height=2,COMMAND=lambda:intro_boton(")"))
boton0_punto =  Button(ventana,text=".",width=5,height=2,COMMAND=lambda:intro_boton("."))

boton_div =  Button(ventana,text="/",width=5,height=2,COMMAND=lambda:intro_boton("/"))
boton_multi =  Button(ventana,text="*",width=5,height=2,COMMAND=lambda:intro_boton("*"))
boton_suma =  Button(ventana,text="+",width=5,height=2,COMMAND=lambda:intro_boton("+"))
boton_resta =  Button(ventana,text="-",width=5,height=2,COMMAND=lambda:intro_boton("-"))
boton_igual =  Button(ventana,text="=",width=5,height=2,COMMAND=lambda:operaciones("="))

#posicionamos los  botones de la calculadora
boton_borrar.grid(row="1",column="0",padx="5",pady="5")
boton_parentesis1.grid(row="1",column="1",padx="5",pady="5")
boton0_parentesis2.grid(row="1",column="2",padx="5",pady="5")
boton0_punto.grid(row="1",column="3",padx="5",pady="5")

boton7.grid(row="2",column="0",padx="5",pady="5")
boton8.grid(row="2",column="1",padx="5",pady="5")
boton9.grid(row="2",column="2",padx="5",pady="5")
boton_multi.grid(row="2",column="3",padx="5",pady="5")

boton4.grid(row="3",column="0",padx="5",pady="5")
boton5.grid(row="3",column="1",padx="5",pady="5")
boton6.grid(row="3",column="2",padx="5",pady="5")
boton_suma.grid(row="3",column="3",padx="5",pady="5")

boton1.grid(row="4",column="0",padx="5",pady="5")
boton2.grid(row="4",column="1",padx="5",pady="5")
boton3.grid(row="4",column="2",padx="5",pady="5")
boton_resta.grid(row="4",column="3",padx="5",pady="5")


boton0.grid(row="5",column="0",padx="5",pady="5")#nos saltamos la columna 1 para que el boton cero valla alargado
boton0_punto.grid(row="5",column="2",padx="5",pady="5")
boton_igual.grid(row="5",column="3",padx="5",pady="5")





ventana.mainloop()