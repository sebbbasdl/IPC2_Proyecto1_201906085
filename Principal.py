from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from MatrizP import matriz
import random

raiz=Tk()

def espar(n):
    return pow(-1,n)==1

def verificacion(coorx,coory):
    contadorE=0
    prueba0=matrizJuego.obtenerValorporPosicion(coorx,coory)
    prueba1=matrizJuego.obtenerValorporPosicion(coorx,coory-1)
    prueba2=matrizJuego.obtenerValorporPosicion(coorx,coory+1)
    prueba3=matrizJuego.obtenerValorporPosicion(coorx+1,coory)
    prueba4=matrizJuego.obtenerValorporPosicion(coorx-1,coory)
    print("----------------")
    print("en el lugar "+str(prueba0))
    print("izquierda "+str(prueba1))
    print("derecha "+ str(prueba2))
    print("abajo "+str(prueba3))
    print("arriba "+str(prueba4))

    if str(prueba0)=="None":
        contadorE+=1
    if str(prueba1)=="None":

        contadorE+=1
    if str(prueba2)=="None":
        contadorE+=1
    if str(prueba3)=="None":
        contadorE+=1
    if str(prueba4)=="None":
        contadorE+=1
        print(contadorE)
    print(contadorE)
    if contadorE==5:
        return True
    else:
        return False






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
        matrizJuego.insertarM(coorx,coory,numeroJ)
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
    ventanaJuego = Tk()
    ventanaJuego.geometry("1920x1080")
    ventanaJuego.title("Juego")
    jugador1 = "Jugador1"
    jugador2 = "Jugador2"

    lblC = Label(ventanaJuego,text="Ingrese el tamaño del tablero:", font=("Agency FB", 14)).place(x=1000+10, y=10)
    lblF = Label(ventanaJuego,text="No. de Filas:", font=("Agency FB", 10)).place(x=1000+20, y=50)
    lblCol = Label(ventanaJuego,text="No. de Columnas:", font=("Agency FB", 10)).place(x=1000+270, y=50)
    
    
    entradaF = IntVar()
    entradaC = IntVar()
    txtF = Entry(ventanaJuego, textvariable=entradaF).place(x=1000+70, y=50)
    txtC = Entry(ventanaJuego, textvariable=entradaC).place(x=1000+340, y=50)


    lblColores2 = Label(ventanaJuego, text="Escribe las opciones de color en los espacios: \"blue\", \"red\", \"yellow\", \"green\"", font=("Agency FB", 12)).place(x=1000+10, y=90)
    lblC1 = Label(ventanaJuego, text="Color Jugador1:", font=("Agency FB", 10)).place(x=1000+20, y=150)
    lblC2 = Label(ventanaJuego, text="Color Jugador2:", font=("Agency FB", 10)).place(x=1000+270, y=150)
    color1 = StringVar()
    color2 = StringVar()
    txtC1 = Entry(ventanaJuego, textvariable=color1).place(x=1000+90, y=150)
    txtC2 = Entry(ventanaJuego, textvariable=color2).place(x=1000+340, y=150)




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

        lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=250+10)
        lblCJJ1 = Label(ventanaJuego, text="Ingrese coordenadas para la pieza:", font=("Agency FB", 14)).place(x=1000+10, y=250+10+40)
        lblFJ1 = Label(ventanaJuego, text="Fila:", font=("Agency FB", 10)).place(x=1000+10, y=250+50+40)
        lblColJ1 = Label(ventanaJuego, text="Columna:", font=("Agency FB", 10)).place(x=1000+275, y=250+50+40)


        entradaX = IntVar()
        entradaY = IntVar()

        txtF = Entry(ventanaJuego, textvariable=entradaX).place(x=1000+70, y=250+50+40)
        txtC = Entry(ventanaJuego, textvariable=entradaY).place(x=1000+340, y=250+50+40)


        def prueba1():
            global turno,numeroxd,contadorError



            print("Turno: "+str(turno))
            print("->"+str(numeroxd))
            cx = entradaX.get()-1
            cy = entradaY.get()-1
            print("(" + str(cx) + str(cy) + ")")

            """if turno==0:

                insertarPiezas(1, cx, cy, numeroxd, c1, ventanaJuego)
                numeroxd = random.randint(1, 6)
                piezasInterfaz(numeroxd, ventanaJuego)
                lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10, y=250 + 10)

            else:"""


            if espar(turno) == True:


                if verificacion(cx,cy)==True:
                    lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)


                    numJugador = 1
                    insertarPiezas(numJugador,cx,cy,numeroxd,c1,ventanaJuego)
                    contadorError=0
                    numeroxd = random.randint(1, 6)
                    piezasInterfaz(numeroxd, ventanaJuego)
                    turno=1
                else:
                    contadorError+=1
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)


            else:


                if verificacion(cx,cy)==True:
                    lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)


                    numJugador = 2

                    insertarPiezas(numJugador, cx, cy, numeroxd, c2, ventanaJuego)

                    contadorError=0
                    numeroxd = random.randint(1, 6)
                    piezasInterfaz(numeroxd, ventanaJuego)
                    turno=0
                else:
                    contadorError+=1
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)


            print("Error: "+str(contadorError))



        botonInsertar = Button(ventanaJuego,command=prueba1, text="Insertar", bg=colorb, width=anchob,height=altob).place(x=1143, y=250+150)

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

    botonJugar = Button(ventanaJuego,command=panelJuego, text="Iniciar Juego",bg=colorb,width=anchob,height=altob).place(x=1000+180,y=190)







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
contadorError=0
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