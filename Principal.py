from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from MatrizP import matriz
import random

raiz=Tk()
raiz2=Tk()

def espar(n):
    return pow(-1,n)==1

def insertarPiezas(numeroJ,coorx,coory,numeroPieza,color,ventanaJuego):
    if numeroPieza==1:
        matrizJuego.insertarM(coorx,coory,numeroJ)
        matrizJuego.insertarM(coorx+1,coory,numeroJ)
        matrizJuego.insertarM(coorx+2,coory,numeroJ)
        matrizJuego.insertarM(coorx+3,coory,numeroJ)
        matrizJuego.insertarM(coorx+3,coory+1,numeroJ)

        #en interfaz
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+1, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+2, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+3, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+3, column=coory+1)

    elif numeroPieza==2:
        matrizJuego.insertarM(coorx,coory.numeroJ)
        matrizJuego.insertarM(coorx+1,coory,numeroJ)
        matrizJuego.insertarM(coorx+2, coory , numeroJ)
        matrizJuego.insertarM(coorx+3, coory , numeroJ)
        matrizJuego.insertarM(coorx+3, coory-1 , numeroJ)

        #en interfaz
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+1, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+2, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+3, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+3, column=coory-1)


    elif numeroPieza==3:
        matrizJuego.insertarM(coorx, coory, numeroJ)
        matrizJuego.insertarM(coorx, coory+1, numeroJ)
        matrizJuego.insertarM(coorx, coory+2, numeroJ)
        matrizJuego.insertarM(coorx, coory+3, numeroJ)

        #en interfaz
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+1)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+2)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+3)




    elif numeroPieza==4:
        matrizJuego.insertarM(coorx, coory, numeroJ)
        matrizJuego.insertarM(coorx+1, coory, numeroJ)
        matrizJuego.insertarM(coorx, coory+1, numeroJ)
        matrizJuego.insertarM(coorx+1, coory+1, numeroJ)

        #en interfaz

        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+1, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+1)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+1, column=coory+1)



    elif numeroPieza==5:
        matrizJuego.insertarM(coorx, coory, numeroJ)
        matrizJuego.insertarM(coorx, coory+1, numeroJ)
        matrizJuego.insertarM(coorx, coory+2, numeroJ)
        matrizJuego.insertarM(coorx, coory+3, numeroJ)
        matrizJuego.insertarM(coorx-1, coory+1, numeroJ)
        matrizJuego.insertarM(coorx-1, coory+2, numeroJ)

        #en interfaz

        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+1)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+2)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory+3)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx-1, column=coory+1)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx-1, column=coory+2)

    elif numeroPieza==6:
        matrizJuego.insertarM(coorx, coory, numeroJ)
        matrizJuego.insertarM(coorx+1, coory, numeroJ)
        matrizJuego.insertarM(coorx+2, coory, numeroJ)
        matrizJuego.insertarM(coorx+3, coory, numeroJ)

        #en interfaz

        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+1, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+2, column=coory)
        botonmatriz = Button(ventanaJuego, bg=color, width=1, height=1).grid(row=coorx+3, column=coory)





def piezasInterfaz(n,ventana):
    global lblC1,lblC2,lblC3,lblC4,lblC5,lblC6
    print("Soy n: "+str(n))

    if n == 1:

        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)
        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="red", font=("Agency FB", 25)).place(x=1300, y=550)
    elif n == 2:

        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="red",
                      font=("Agency FB", 25)).place(x=1300, y=550)

    elif n == 3:
        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="red", font=("Agency FB", 25)).place(x=1300, y=550)

    elif n == 4:
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)
        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="red", font=("Agency FB", 25)).place(x=1300, y=550)
    elif n == 5:

        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)
        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="red", font=("Agency FB", 25)).place(x=1300, y=550)
    elif n == 6:
        lblC6 = Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)

        lblC1 = Label(ventana, text="⬛\n⬛\n⬛\n       ⬛ ⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC2 = Label(ventana, text="         ⬛\n         ⬛\n         ⬛\n  ⬛ ⬛", fg="gray99",
                      font=("Agency FB", 25)).place(x=1300, y=550)
        lblC3 = Label(ventana, text="⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC4 = Label(ventana, text="⬛⬛\n⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC5 = Label(ventana, text="⬛⬛\n⬛⬛⬛⬛", fg="gray99", font=("Agency FB", 25)).place(x=1300, y=550)
        lblC6=Label(ventana, text="⬛\n⬛\n⬛\n⬛", fg="red", font=("Agency FB", 25)).place(x=1300, y=550)


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

        numeroxd=random.randint(1,6)

        print("xd2"+str(turno))
        contador=0
        c1=color1.get()
        c2=color2.get()
        m=entradaF.get()
        n=entradaC.get()

        ventanaJuego = Tk()
        ventanaJuego.geometry("1920x1080")
        ventanaJuego.title("Juego")
        piezasInterfaz(numeroxd, ventanaJuego)
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


        entradaX = IntVar()
        entradaY = IntVar()

        txtF = Entry(ventanaJuego, textvariable=entradaX).place(x=1000+70, y=50+40)
        txtC = Entry(ventanaJuego, textvariable=entradaY).place(x=1000+340, y=50+40)


        def prueba1():
            global turno,numeroxd


            turno += 1
            print("->"+str(numeroxd))
            cx = entradaX.get()
            cy = entradaY.get()
            print("(" + str(cx) + str(cy) + ")")


            piezasInterfaz(numeroxd, ventanaJuego)
            if espar(turno) == True:
                lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=10)
                numJugador=1
                insertarPiezas(numJugador,cx,cy,numeroxd,c1,ventanaJuego)

            else:
                lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10, y=10)
                numJugador=2
                insertarPiezas(numJugador, cx, cy, numeroxd, c2, ventanaJuego)
            numeroxd = random.randint(1, 6)



        botonInsertar = Button(ventanaJuego,command=prueba1, text="Insertar", bg=colorb, width=anchob,height=altob).place(x=1143, y=150)

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


matrizJuego=matriz()
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


"""Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=430)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=457)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=484)
Bcoordenadas = Button(ventanaP, bg="gray48", width=1, height=1).place(x=1143,y=511)"""





ventanaP.mainloop()