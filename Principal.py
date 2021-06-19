from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from MatrizP import matriz
import random

raiz=Tk()
def espar(n):
    return pow(-1,n)==1


def buscaArchivo():
    archivo = filedialog.askopenfilename(title="Abrir")
    print(archivo)




def procesoPartida():


    print("xd"+str(turno))
    ventana2 = Tk()
    ventana2.geometry("500x300+100+100")
    ventana2.title("Obteniendo Valores")
    jugador1 = "Jugador1"
    jugador2 = "Jugador2"

    lblC = Label(ventana2,text="Ingrese el tamaño del tablero:", font=("Agency FB", 14)).place(x=10, y=10)
    lblF = Label(ventana2,text="No. de Filas:", font=("Agency FB", 10)).place(x=20, y=50)
    lblCol = Label(ventana2,text="No. de Columnas:", font=("Agency FB", 10)).place(x=270, y=50)
    
    
    entradaF = IntVar()
    entradaC = IntVar()
    txtF = Entry(ventana2, textvariable=entradaF).place(x=70, y=50)
    txtC = Entry(ventana2, textvariable=entradaC).place(x=340, y=50)


    lblColores2 = Label(ventana2, text="Escribe las opciones de color en los espacios: \"blue\", \"red\", \"yellow\", \"green\"", font=("Agency FB", 12)).place(x=10, y=90)
    lblC1 = Label(ventana2, text="Color Jugador1:", font=("Agency FB", 10)).place(x=20, y=150)
    lblC2 = Label(ventana2, text="Color Jugador2:", font=("Agency FB", 10)).place(x=270, y=150)
    color1 = StringVar()
    color2 = StringVar()
    txtC1 = Entry(ventana2, textvariable=color1).place(x=90, y=150)
    txtC2 = Entry(ventana2, textvariable=color2).place(x=340, y=150)




    print("Obteniendo valores del tablero mxn")

    def panelJuego():
        global numeroxd
        numeroxd=random.randint(0,10)

        print("xd2"+str(turno))
        contador=0
        c1=color1.get()
        c2=color2.get()
        m=entradaF.get()
        n=entradaC.get()

        ventanaJuego = Tk()
        ventanaJuego.geometry("1920x1080")
        ventanaJuego.title("Juego")

        print(m)
        print(n)
        for m1 in range(m):
            for n1 in range(n):
                Bespacio = Button(ventanaJuego, bg="white", width=1, height=1).grid(row= 0 + m1, column=0 + n1)
        cantidadx=0
        for n2 in range(n):
            cantidadx+=1
            Bcoordenadas = Button(ventanaJuego,text=str(cantidadx), bg="gray48", width=1, height=1).grid(row=m, column=0+n2)

        cantidady=0
        for m2 in range(m):
            cantidady+=1
            Bcoordenadas = Button(ventanaJuego,text=str(cantidady), bg="gray48", width=1, height=1).grid(row=0+m2, column=n)
        print("Realizando Tablero")

        """if espar(turno)==True:
            lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=10)
        else:
            lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10, y=10)"""

        #INsertar jugador 1

        lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=10)
        lblCJJ1 = Label(ventanaJuego, text="Ingrese coordenadas para la pieza:", font=("Agency FB", 14)).place(x=1000+10, y=10+40)
        lblFJ1 = Label(ventanaJuego, text="Coordenada X:", font=("Agency FB", 10)).place(x=1000+10, y=50+40)
        lblColJ1 = Label(ventanaJuego, text="Coordenada Y:", font=("Agency FB", 10)).place(x=1000+275, y=50+40)

        entradaFJ1 = IntVar()
        entradaCJ1 = IntVar()
        txtFJ = Entry(ventanaJuego, textvariable=entradaFJ1).place(x=1000+70, y=50+40)
        txtCJ = Entry(ventanaJuego, textvariable=entradaCJ1).place(x=1000+340, y=50+40)

        def prueba1():
            global turno,numeroxd
            print("hoja jeje")
            turno += 1
            print(turno)
            print("->"+str(numeroxd))
            if espar(turno) == True:
                lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=10)
            else:
                lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10, y=10)

            numeroxd=random.randint(0,10)
            



        botonInsertar = Button(ventanaJuego,command=prueba1, text="Insertar Jugador1", bg=colorb, width=anchob,height=altob).place(x=1143, y=150)

        """#Insertar jugador2

        lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10, y=200)
        lblCJJ1 = Label(ventanaJuego, text="Ingrese coordenadas para la pieza:", font=("Agency FB", 14)).place(
            x=1000 + 10, y=10 + 40+200)
        lblFJ1 = Label(ventanaJuego, text="Coordenada X:", font=("Agency FB", 10)).place(x=1000 + 10, y=50 + 40+200)
        lblColJ1 = Label(ventanaJuego, text="Coordenada Y:", font=("Agency FB", 10)).place(x=1000 + 275, y=50 + 40+200)

        entradaFJ2 = IntVar()
        entradaCJ2 = IntVar()
        txtFJ = Entry(ventanaJuego, textvariable=entradaFJ2).place(x=1000 + 70, y=50 + 40+200)
        txtCJ = Entry(ventanaJuego, textvariable=entradaCJ2).place(x=1000 + 340, y=50 + 40+200)

        Bcoordenadas = Button(ventanaJuego, text=str(cantidady), bg="gray48", width=1, height=1).place(x=1010,y=430)

        botonInsertar = Button(ventanaJuego, text="Insertar Jugador2", bg=colorb, width=anchob,height=altob).place(x=1143, y=150+200)"""

    botonJugar = Button(ventana2,command=panelJuego, text="Iniciar Juego",bg=colorb,width=anchob,height=altob).place(x=180,y=250)







ventanaP=Tk()

ventanaP.title("Menu Principal")
ventanaP.geometry("1920x1080")
ventanaP.configure(background="gray20")

turno=0
turnoJugador=StringVar()
colorb="gray99"
colorb1="sky blue"
anchob=25
altob=1

botonAbrir= Button(ventanaP, text="Abrir Archivo",command=buscaArchivo,bg=colorb,width=anchob,height=altob).grid(row=1,column=0)
botonIniciar= Button(ventanaP, text="Iniciar Partida",command=procesoPartida,bg=colorb,width=anchob,height=altob).grid(row=2,column=0)
botonTablero= Button(ventanaP, text="Tablero",bg=colorb,width=anchob,height=altob).grid(row=3,column=0)
botonReporte= Button(ventanaP, text="Reportes",bg=colorb,width=anchob,height=altob).grid(row=4,column=0)


numeroR=random.randint(1,6)
print(numeroR)

if numeroR==1:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=457)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=484)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=511)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=511)
elif numeroR==2:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=457)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=484)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=511)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=511)

elif numeroR == 3:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1194, y=430)
elif numeroR == 4:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=457)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=457)
elif numeroR == 5:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1194, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160, y=403)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177, y=403)
elif numeroR == 6:
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=430)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=457)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=484)
    Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143, y=511)

#pieza1
"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=457)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=484)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=511)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=511)"""


#pieza2
"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=457)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=484)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=511)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=511)"""

#pieza3

"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1194,y=430)
"""

#pieza4

"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=457)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=457)"""

#pieza5
"""
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1194,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1160,y=403)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1177,y=403)"""

#pieza6
"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=457)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=484)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=511)"""






ventanaP.mainloop()