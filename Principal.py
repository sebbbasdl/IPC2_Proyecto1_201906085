from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from MatrizP import matriz
import random
from tkinter import messagebox
from xml.dom import minidom
import webbrowser as wb

raiz=Tk()

def espar(n):
    return pow(-1,n)==1

def verificacion(coorx,coory,numeroR,F,C,matrizJuego):
    """contadorE=0
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
        return False"""
    if numeroR==1:
        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)
        er3 = matrizJuego.obtenerValorporPosicion(coorx, coory - 1)
        er4 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er5 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory)

        er6 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er7 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 1)
        er8 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory - 1)

        er9 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory)
        er10 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory + 1)
        er11 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory - 1)

        er12 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory)
        er13 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory + 1)
        er14 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory - 1)

        er15 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory + 1)
        er16 = matrizJuego.obtenerValorporPosicion(coorx + 3-1, coory + 1)
        er17 = matrizJuego.obtenerValorporPosicion(coorx + 3+1, coory + 1)
        er18 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory + 1+1)

        er19=matrizJuego.obtenerValorporPosicion(coorx+4,coory)



        if coory+1!=C and F-coorx>=4 and (str(er1)=="None" and str(er2)=="None" and str(er3)=="None" and str(er4)=="None" and str(er5)=="None" and str(er6)=="None" and str(er7)=="None" and str(er8)=="None" and str(er9)=="None" and str(er10)=="None" and str(er11)=="None" and str(er12)=="None" and str(er13)=="None" and str(er14)=="None" and str(er15)=="None" and str(er16)=="None" and str(er17)=="None" and str(er18)=="None" and str(er19)=="None"):
            return True
        else:
            return False

    elif numeroR==2:

        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)
        er3 = matrizJuego.obtenerValorporPosicion(coorx, coory - 1)
        er4 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er5 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory)


        er6 = matrizJuego.obtenerValorporPosicion(coorx+1, coory)
        er7 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 1)
        er8 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory - 1)

        er9 = matrizJuego.obtenerValorporPosicion(coorx+2, coory)
        er10 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory + 1)
        er11= matrizJuego.obtenerValorporPosicion(coorx + 2, coory - 1)

        er12 = matrizJuego.obtenerValorporPosicion(coorx+3, coory)
        er13 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory + 1)
        er14= matrizJuego.obtenerValorporPosicion(coorx + 3, coory - 1)

        er15 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory - 1)
        er16 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory - 1-1)
        er17 = matrizJuego.obtenerValorporPosicion(coorx + 3+1, coory - 1)
        er18 = matrizJuego.obtenerValorporPosicion(coorx + 3-1, coory - 1)

        er19 = matrizJuego.obtenerValorporPosicion(coorx + 4, coory)



        if coory+1!=1 and F-coorx>=4 and (str(er1) == "None" and str(er2) == "None" and str(er3) == "None" and str(er4) == "None" and str(er5) == "None" and str(er6) == "None" and str(er7) == "None" and str(er8) == "None" and str(er9) == "None" and str(er10) == "None" and str(er11) == "None" and str(er12) == "None" and str(er13) == "None" and str(er14) == "None" and str(er15) == "None" and str(er16) == "None" and str(er17) == "None" and str(er18) == "None" and str(er19)=="None"):
            return True
        else:
            return False

    elif numeroR==3:
        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx-1, coory)
        er3 = matrizJuego.obtenerValorporPosicion(coorx+1, coory)
        er4 = matrizJuego.obtenerValorporPosicion(coorx, coory-1)
        er5 = matrizJuego.obtenerValorporPosicion(coorx, coory+1)

        er6 = matrizJuego.obtenerValorporPosicion(coorx-1, coory+1)
        er7 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 1)

        er8 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory + 2)
        er9 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 2)

        er10 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory + 3)
        er11 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 3)
        er12 = matrizJuego.obtenerValorporPosicion(coorx , coory + 4)

        er13 = matrizJuego.obtenerValorporPosicion(coorx, coory+1)
        er14 = matrizJuego.obtenerValorporPosicion(coorx, coory + 2)
        er15 = matrizJuego.obtenerValorporPosicion(coorx, coory + 3)


        if C-coory>=4 and (str(er1)=="None" and str(er2)=="None" and str(er3)=="None" and str(er4)=="None" and str(er5)=="None" and str(er6)=="None" and str(er7)=="None" and str(er8)=="None" and str(er9)=="None" and str(er10)=="None" and str(er11)=="None" and str(er12)=="None" and str(er13)=="None" and str(er14)=="None" and str(er15)=="None"):

            return True

        else:
            return False

    elif numeroR==4:
        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory)
        er3 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er4 = matrizJuego.obtenerValorporPosicion(coorx, coory - 1)
        er5 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)

        er6 = matrizJuego.obtenerValorporPosicion(coorx+1, coory)
        er7 = matrizJuego.obtenerValorporPosicion(coorx+1+1, coory)
        er8 = matrizJuego.obtenerValorporPosicion(coorx+1, coory-1)

        er9 = matrizJuego.obtenerValorporPosicion(coorx, coory+1)
        er10 = matrizJuego.obtenerValorporPosicion(coorx-1, coory+1)
        er11 = matrizJuego.obtenerValorporPosicion(coorx, coory+1+1)

        er12 = matrizJuego.obtenerValorporPosicion(coorx+1, coory+1)
        er13 = matrizJuego.obtenerValorporPosicion(coorx+1+1, coory+1)
        er14 = matrizJuego.obtenerValorporPosicion(coorx+1, coory+1+1)



        if C!=coory+1 and F!=coorx+1 and (str(er1) == "None" and str(er2) == "None" and str(er3) == "None" and str(er4) == "None" and str(er5) == "None" and str(er6) == "None" and str(er7) == "None" and str(er8) == "None" and str(er9) == "None" and str(er10) == "None" and str(er11) == "None" and str(er12) == "None" and str(er13) == "None" and str(er14) == "None"):
            return True

        else:
            return False

    elif numeroR==5:
        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory)
        er3 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er4 = matrizJuego.obtenerValorporPosicion(coorx, coory - 1)
        er5 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)

        er6 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory + 1)
        er7 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 1)

        er8 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory + 2)
        er9 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 2)

        er10 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory + 3)
        er11 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 3)
        er12 = matrizJuego.obtenerValorporPosicion(coorx, coory + 4)

        er13 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)
        er14 = matrizJuego.obtenerValorporPosicion(coorx, coory + 2)
        er15 = matrizJuego.obtenerValorporPosicion(coorx, coory + 3)

        er16 = matrizJuego.obtenerValorporPosicion(coorx-1-1, coory + 1)
        er17 = matrizJuego.obtenerValorporPosicion(coorx-1-1, coory +2)

        if  coorx+1!=1 and coory+1!=C and C-coory>=4 and (str(er1) == "None" and str(er2) == "None" and str(er3) == "None" and str(er4) == "None" and str(er5) == "None" and str(er6) == "None" and str(er7) == "None" and str(er8) == "None" and str(er9) == "None" and str(er10) == "None" and str(er11) == "None" and str(er12) == "None" and str(er13) == "None" and str(er14) == "None" and str(er15) == "None" and str(er16) == "None" and str(er17) == "None"):

            return True
        else:
            return False

    elif numeroR==6:
        er1 = matrizJuego.obtenerValorporPosicion(coorx, coory)
        er2 = matrizJuego.obtenerValorporPosicion(coorx, coory + 1)
        er3 = matrizJuego.obtenerValorporPosicion(coorx, coory - 1)
        er4 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er5 = matrizJuego.obtenerValorporPosicion(coorx - 1, coory)

        er6 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory)
        er7 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory + 1)
        er8 = matrizJuego.obtenerValorporPosicion(coorx + 1, coory - 1)

        er9 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory)
        er10 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory + 1)
        er11 = matrizJuego.obtenerValorporPosicion(coorx + 2, coory - 1)

        er12 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory)
        er13 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory + 1)
        er14 = matrizJuego.obtenerValorporPosicion(coorx + 3, coory - 1)
        er15 = matrizJuego.obtenerValorporPosicion(coorx + 4, coory)

        if F-coorx>=4 and (str(er1) == "None" and str(er2) == "None" and str(er3) == "None" and str(er4) == "None" and str(er5) == "None" and str(er6) == "None" and str(er7) == "None" and str(er8) == "None" and str(er9) == "None" and str(er10) == "None" and str(er11) == "None" and str(er12) == "None" and str(er13) == "None" and str(er14) == "None" and str(er15) == "None") :
            return True

        else:
            return False




def insertarPiezas(numeroJ,coorx,coory,numeroPieza,color,ventanaJuego,matrizJuego):
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
    global numeroxd
    ventanaJuego = Tk()
    ventanaJuego.geometry("1920x1080")
    ventanaJuego.title("Juego")
    jugador1 = "Jugador1"
    jugador2 = "Jugador2"
    numeroxd = random.randint(1, 6)

    archivo = filedialog.askopenfilename(title="Abrir")
    print(archivo)

    xml=minidom.parse(archivo)
    matrizb= xml.getElementsByTagName("matriz")

    for ma in matrizb:
        nombre= ma.getElementsByTagName("nombre")[0]
        filas  = ma.getElementsByTagName("filas")[0]
        columnas = ma.getElementsByTagName("columnas")[0]
        color1 = ma.getElementsByTagName("color1")[0]
        color2= ma.getElementsByTagName("color2")[0]
        imagen = ma.getElementsByTagName("imagen")[0]


    nombre1=nombre.firstChild.data
    filas1 = filas.firstChild.data
    columnas1 = columnas.firstChild.data
    color11 = color1.firstChild.data
    color21 = color2.firstChild.data
    imagen1 = imagen.firstChild.data


    if str(color11)=="Rojo" or str(color11)=="rojo":

        color11="red"

    elif str(color11)=="Verde" or str(color11)=="verde":
        color11="green"

    elif str(color11)=="Amarillo"or str(color11)=="amarillo":
        color11="yellow"

    elif str(color11)=="Azul" or str(color11)=="azul":
        color11="blue"


    #color2
    if str(color21) == "Rojo" or str(color21) == "rojo":
        color21 = "red"

    elif str(color21) == "Verde" or str(color21) == "verde":
        color21 = "green"

    elif str(color21) == "Amarillo" or str(color21) == "amarillo":
        color21 = "yellow"

    elif str(color21) == "Azul" or str(color21) == "azul":
        color21 = "blue"

    print(nombre1,filas1,columnas1,color11,color21,imagen1)

    matrizL=matriz()


    imagen2= imagen1.split(" ")
    print(imagen2)
    if imagen2[0]=="" and imagen2[int(filas1)]:
        imagen2.pop(0)
    else:

        print(imagen2)












    print("xd2" + str(turno))
    contador = 0
    c1 = str(color11)
    c2 = str(color21)
    m = int(filas1)
    n = int(columnas1)
    cantidad = 20

    piezasInterfaz(numeroxd, ventanaJuego)
    print(m)
    print(n)
    for m1 in range(m):
        for n1 in range(n):
            Bespacio = Button(ventanaJuego, bg="white", width=1, height=1).grid(row=0 + m1, column=0 + n1)
    cantidadx = 0
    for n2 in range(n):
        cantidadx += 1
        Bcoordenadas = Button(ventanaJuego, text=str(cantidadx), bg="gray48", width=1, height=1).grid(row=m,
                                                                                                      column=0 + n2)

    cantidady = 0
    for m2 in range(m):
        cantidady += 1
        Bcoordenadas = Button(ventanaJuego, text=str(cantidady), bg="gray48", width=1, height=1).grid(
            row=0 + m2, column=n)
    print("Realizando Tablero")



    for m2 in range(int(filas1)):
        for n2 in range(int(columnas1)):
            valor=imagen2[m2][n2]

            if valor=="1":

                matrizL.insertarM(m2,n2,1)
                Bcoordenadas = Button(ventanaJuego, bg=color11, width=1, height=1).grid(row=m2,column=n2)
            elif valor=="2":

                matrizL.insertarM(m2,n2,2)
                Bcoordenadas = Button(ventanaJuego, bg=color21, width=1, height=1).grid(row=m2, column=n2)

    # INsertar jugador 1

    lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=250 + 10)
    lblCJJ1 = Label(ventanaJuego, text="Ingrese coordenadas para la pieza:", font=("Agency FB", 14)).place(
        x=1000 + 10, y=250 + 10 + 40)
    lblFJ1 = Label(ventanaJuego, text="Fila:", font=("Agency FB", 10)).place(x=1000 + 10, y=250 + 50 + 40)
    lblColJ1 = Label(ventanaJuego, text="Columna:", font=("Agency FB", 10)).place(x=1000 + 275, y=250 + 50 + 40)

    entradaX = IntVar()
    entradaY = IntVar()

    txtF = Entry(ventanaJuego, textvariable=entradaX).place(x=1000 + 70, y=250 + 50 + 40)
    txtC = Entry(ventanaJuego, textvariable=entradaY).place(x=1000 + 340, y=250 + 50 + 40)

    def guardar():
        print("Escribiendo archivo XML")

        if c1 == "red":
            c1aux = "rojo"
        elif c1 == "blue":
            c1aux = "azul"

        elif c1 == "yellow":
            c1aux = "amarillo"

        elif c1 == "green":
            c1aux = "verde"

        # color2

        if c2 == "red":
            c1aux2 = "rojo"
        elif c2 == "blue":
            c1aux2 = "azul"

        elif c2 == "yellow":
            c1aux2 = "amarillo"

        elif c2 == "green":
            c1aux2 = "verde"

        archivoxml = open("PartidaGuardada.xml", "w")

        archivoxml.write("<matrices>\n")
        archivoxml.write("\t<matriz>\n")
        archivoxml.write("\t\t<nombre>Partida1</nombre>\n")
        archivoxml.write("\t\t<filas>" + str(m) + "</filas>\n")
        archivoxml.write("\t\t<columnas>" + str(n) + "</columnas>\n")
        archivoxml.write("\t\t<color1>" + c1aux + "</color1>\n")
        archivoxml.write("\t\t<color2>" + c1aux2 + "</color2>\n")
        imagen = ""
        for m11 in range(m):
            if m11 != 0:
                imagen += " "

            for n11 in range(n):

                cadena = str(matrizL.obtenerValorporPosicion(m11, n11))

                if cadena == "None":
                    imagen += "-"
                elif cadena == "1":
                    imagen += "1"
                elif cadena == "2":
                    imagen += "2"

        print(imagen)
        print(str(m11) + str(m))
        print(str(n11) + str(n))
        archivoxml.write("\t\t<imagen>" + imagen + "</imagen>\n")
        archivoxml.write("\t</matriz>\n")
        archivoxml.write("</matrices>")

    def terminar():

        print("Cantidad: " + str(cantidad))
        print("Cantidad J1: " + str(cantidadPiezasJ1))
        print("Cantidad J2: " + str(cantidadPiezasJ2))

        if cantidadPiezasJ1 > cantidadPiezasJ2:
            print("Gano Jugador 1")
            messagebox.showinfo("GANADOR: ", "Jugador1 ")
            botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                   height=altob, state=DISABLED).place(x=1143, y=250 + 150)

        elif cantidadPiezasJ2 > cantidadPiezasJ2:
            print("Gano Jugador 2")
            messagebox.showinfo("GANADOR: ", "Jugador2 ")
            botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                   height=altob, state=DISABLED).place(x=1143, y=250 + 150)

        elif cantidadPiezasJ2 == cantidadPiezasJ1:
            print("Empate")
            messagebox.showinfo("EMPATE ",
                                "Jugador1: " + str(cantidadPiezasJ1) + "\nJugador2: " + str(cantidadPiezasJ2))
            botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                   height=altob, state=DISABLED).place(x=1143, y=250 + 150)

    def prueba1():
        global turno, numeroxd, contadorError, cantidadPiezasJ1, cantidadPiezasJ2

        print("Turno: " + str(turno))
        print("->" + str(numeroxd))
        cx = entradaX.get()-1
        cy = entradaY.get()-1
        print("(" + str(cx) + str(cy) + ")")

        v = verificacion(cx, cy, numeroxd, m, n, matrizL)
        print("V: " + str(v))

        if espar(turno) == True:

            if verificacion(cx, cy, numeroxd, m, n, matrizL) == True:
                lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10,
                                                                                             y=250 + 10)

                numJugador = 1
                insertarPiezas(numJugador, cx, cy, numeroxd, c1, ventanaJuego, matrizL)
                contadorError = 0
                numeroxd = random.randint(1, 6)
                piezasInterfaz(numeroxd, ventanaJuego)
                turno = 1
                lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                              font=("Arial", 14)).place(x=1150 + 10,
                                                        y=250 + 10)
                cantidadPiezasJ1 += 1
                print("J1: " + str(cantidadPiezasJ1))
            else:
                contadorError += 1
                lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                              font=("Arial", 14)).place(x=1150 + 10,
                                                        y=250 + 10)

                if contadorError == 2:
                    turno = 1
                    contadorError = 0
                    print("perdio j1")
                    lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)


        else:

            if verificacion(cx, cy, numeroxd, m, n, matrizL) == True:
                lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10,
                                                                                             y=250 + 10)

                numJugador = 2

                insertarPiezas(numJugador, cx, cy, numeroxd, c2, ventanaJuego, matrizL)

                contadorError = 0
                numeroxd = random.randint(1, 6)
                piezasInterfaz(numeroxd, ventanaJuego)
                turno = 0
                lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                              font=("Arial", 14)).place(x=1150 + 10,
                                                        y=250 + 10)

                cantidadPiezasJ2 += 1
                print("J2: " + str(cantidadPiezasJ2))
            else:
                contadorError += 1
                lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                              font=("Arial", 14)).place(x=1150 + 10,
                                                        y=250 + 10)

                if contadorError == 2:
                    print("perdio J2")
                    turno = 0
                    contadorError = 0
                    lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)

                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)

        print("Error: " + str(contadorError))

        if cantidad == cantidadPiezasJ1:
            print("Gano Jugador 1")
            messagebox.showinfo("GANADOR: ", "Jugador1 ")
            botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                   height=altob, state=DISABLED).place(x=1143, y=250 + 150)
        elif cantidad == cantidadPiezasJ2:
            print("Gano Jugador 2")
            messagebox.showinfo("GANADOR:", "Jugador2 ")
            botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                   height=altob, state=DISABLED).place(x=1143, y=250 + 150)

        lblCJ1 = Label(ventanaJuego, text="Piezas incertadas Jugador1: " + str(cantidadPiezasJ1), bg="gray63",
                       font=("Arial", 10)).place(x=20, y=700)
        lblCJ2 = Label(ventanaJuego, text="Piezas incertadas Jugador2: " + str(cantidadPiezasJ2), bg="gray63",
                       font=("Arial", 10)).place(x=20, y=730)

    botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                           height=altob).place(x=1143, y=250 + 150)

    botonGuardar = Button(ventanaJuego, command=guardar, text="Guardar partida", bg="goldenrod3", width=anchob,
                          height=altob).place(x=1310, y=250 + 150 + 50)
    botonTerminar = Button(ventanaJuego, command=terminar, text="Terminar partida", bg="goldenrod3",
                           width=anchob,
                           height=altob).place(x=1010, y=250 + 150 + 50)

    lblCJJ = Label(ventanaJuego,
                   text="Panel -----------------------------------------------------------------------------",
                   bg="gray63", font=("Arial", 14)).place(x=1010,
                                                          y=500)






def procesoPartida():

    matrizJuego=matriz()
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

    lblP= Label(ventanaJuego, text="Cantidad de Piezas:", font=("Agency FB", 10)).place(x=1000+20 , y=200)

    cantidadP=IntVar()
    txtC1 = Entry(ventanaJuego, textvariable=cantidadP).place(x=1000 + 100, y=200)




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
        cantidad=cantidadP.get()


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


        #INsertar jugador 1

        lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10, y=250+10)
        lblCJJ1 = Label(ventanaJuego, text="Ingrese coordenadas para la pieza:", font=("Agency FB", 14)).place(x=1000+10, y=250+10+40)
        lblFJ1 = Label(ventanaJuego, text="Fila:", font=("Agency FB", 10)).place(x=1000+10, y=250+50+40)
        lblColJ1 = Label(ventanaJuego, text="Columna:", font=("Agency FB", 10)).place(x=1000+275, y=250+50+40)


        entradaX = IntVar()
        entradaY = IntVar()

        txtF = Entry(ventanaJuego, textvariable=entradaX).place(x=1000+70, y=250+50+40)
        txtC = Entry(ventanaJuego, textvariable=entradaY).place(x=1000+340, y=250+50+40)

        def guardar():
            print("Escribiendo archivo XML")

            if c1=="red":
                c1aux="rojo"
            elif c1=="blue":
                c1aux="azul"

            elif c1=="yellow":
                c1aux="amarillo"

            elif c1=="green":
                c1aux="verde"

            #color2

            if c2 == "red":
                c1aux2 = "rojo"
            elif c2 == "blue":
                c1aux2 = "azul"

            elif c2 == "yellow":
                c1aux2 = "amarillo"

            elif c2 == "green":
                c1aux2 = "verde"


            archivoxml = open("PartidaGuardada.xml", "w")

            archivoxml.write("<matrices>\n")
            archivoxml.write("\t<matriz>\n")
            archivoxml.write("\t\t<nombre>Partida1</nombre>\n")
            archivoxml.write("\t\t<filas>"+str(m)+"</filas>\n")
            archivoxml.write("\t\t<columnas>"+str(n)+"</columnas>\n")
            archivoxml.write("\t\t<color1>"+c1aux+"</color1>\n")
            archivoxml.write("\t\t<color2>" + c1aux2 + "</color2>\n")
            imagen = ""
            for m11 in range(m):
                if m11!=0:
                    imagen+=" "

                for n11 in range(n):

                    cadena=str(matrizJuego.obtenerValorporPosicion(m11,n11))

                    if cadena=="None":
                        imagen+="-"
                    elif cadena=="1":
                        imagen+="1"
                    elif cadena =="2":
                        imagen+="2"


            print(imagen)
            print(str(m11)+str(m))
            print(str(n11)+str(n))
            archivoxml.write("\t\t<imagen>"+imagen+"</imagen>\n")
            archivoxml.write("\t</matriz>\n")
            archivoxml.write("</matrices>")






        def terminar():

            print("Cantidad: "+str(cantidad))
            print("Cantidad J1: "+str(cantidadPiezasJ1))
            print("Cantidad J2: " + str(cantidadPiezasJ2))

            if cantidadPiezasJ1>cantidadPiezasJ2:
                print("Gano Jugador 1")
                messagebox.showinfo("GANADOR: ", "Jugador1 ")
                botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                       height=altob, state=DISABLED).place(x=1143, y=250 + 150)
                ganador = "Jugador 1"

            elif cantidadPiezasJ2>cantidadPiezasJ2:
                print("Gano Jugador 2")
                messagebox.showinfo("GANADOR: ", "Jugador2 ")
                botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                       height=altob, state=DISABLED).place(x=1143, y=250 + 150)
                ganador = "Jugador 2"

            elif cantidadPiezasJ2==cantidadPiezasJ1:
                print("Empate")
                messagebox.showinfo("EMPATE ", "Jugador1: "+str(cantidadPiezasJ1)+"\nJugador2: "+str(cantidadPiezasJ2))
                botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                       height=altob, state=DISABLED).place(x=1143, y=250 + 150)
                ganador = "Empate"


        def prueba1():
            global turno,numeroxd,contadorError, cantidadPiezasJ1,cantidadPiezasJ2,DatosJugador1,DatosJugador2, ganador

            print("Turno: " + str(turno))
            print("->" + str(numeroxd))
            cx = entradaX.get() - 1
            cy = entradaY.get() - 1
            print("(" + str(cx) + str(cy) + ")")
            v = verificacion(cx, cy, numeroxd, m, n, matrizJuego)
            print("V: " + str(v))



            #html



            archivohtml = open("reporte.html", "w")
            archivohtml.write("<html>\n")
            archivohtml.write("<head>\n")
            archivohtml.write("\t<tittle>REPORTE</tittle>\n")
            archivohtml.write("</head>\n")
            archivohtml.write("<body>\n")
            archivohtml.write("\t<style>\n")
            archivohtml.write("#inicio{\nborder:solid 2px black;\nwidth: 80%\nmargin:0 auto;\npadding:5px;\ntext-align:center;\n\n}\nfieldset{\nmargin-bottom: 10px\ntext-align:right;\n}\nlegend{\nborder:solid 3px green;\npadding: 5px;\nfont-weight: bold;\nborder-radius: 20px\nbody{\nbackground: url(fondo.jpg);\nbackground-size: 100%\n\n}")
            archivohtml.write("\n\t</style>\n")
            archivohtml.write("<div id=\"inicio\">\n")
            archivohtml.write("<h2>El tamaño de la matriz es:" +str(m)+"X"+str(n)+ "</h2><br>\n")
            archivohtml.write("\t<fieldset>\n")
            archivohtml.write("\t\t<legend>Jugador1: "+c1+" Cantidad de piezas incertadas:"+str(cantidadPiezasJ1)+"</legend>\n")
            archivohtml.write("\t\t<h5>" + DatosJugador1+"<br>")
            archivohtml.write("\t\t+</h5>\n")
            archivohtml.write("\t</fieldset>\n")
            archivohtml.write("\t<fieldset>\n")
            archivohtml.write("\t\t<legend>Jugador2: "+c2+" Cantidad de piezas incertadas:"+str(cantidadPiezasJ2)+"</legend>\n")
            archivohtml.write("\t\t<h5>" + DatosJugador2+"<br>")
            archivohtml.write("\t\t+</h5>\n")
            archivohtml.write("\t</fieldset>\n")
            archivohtml.write("</div>\n")
            archivohtml.write("</body>")









            if espar(turno) == True:


                if verificacion(cx,cy,numeroxd,m,n,matrizJuego)==True:
                    lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)

                    DatosJugador1+="Inserta Pieza "+str(numeroxd)+" en fila: "+str(cx+1)+", columna: "+str(cy+1)+"<br>\n"


                    numJugador = 1
                    insertarPiezas(numJugador,cx,cy,numeroxd,c1,ventanaJuego,matrizJuego)
                    contadorError=0
                    numeroxd = random.randint(1, 6)
                    piezasInterfaz(numeroxd, ventanaJuego)
                    turno=1
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)
                    cantidadPiezasJ1+=1
                    print("J1: "+str(cantidadPiezasJ1))
                else:
                    contadorError+=1
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)

                    if contadorError==2:
                        turno=1
                        DatosJugador1 +="Error al insertar Pieza "+str(numeroxd)+" en fila:"  + str(cx+1) + ", columna: " + str(cy+1) + ", Numero de errores: "+str(contadorError)+"<br>\n"
                        contadorError=0
                        print("perdio j1")

                        lblCJJ = Label(ventanaJuego, text=jugador2, bg=c2, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                     y=250 + 10)
                        lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                                      font=("Arial", 14)).place(x=1150 + 10,
                                                                y=250 + 10)


            else:


                if verificacion(cx,cy,numeroxd,m,n,matrizJuego)==True:
                    lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                 y=250 + 10)


                    numJugador = 2
                    DatosJugador2 += "Inserta Pieza "+str(numeroxd)+" en fila: "+str(cx+1)+", columna: "+str(cy+1)+"<br>\n"
                    insertarPiezas(numJugador, cx, cy, numeroxd, c2, ventanaJuego,matrizJuego)

                    contadorError=0
                    numeroxd = random.randint(1, 6)
                    piezasInterfaz(numeroxd, ventanaJuego)
                    turno=0
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)

                    cantidadPiezasJ2+=1
                    print("J2: "+str(cantidadPiezasJ2))
                else:
                    contadorError+=1
                    lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c2,
                                  font=("Arial", 14)).place(x=1150 + 10,
                                                            y=250 + 10)

                    if contadorError==2:
                        print("perdio J2")
                        DatosJugador2 += "Error al insertar Pieza "+str(numeroxd)+" en fila:"  + str(cx+1) + ", columna: " + str(cy+1) + ", Numero de errores: "+str(contadorError)+"<br>\n"
                        turno=0
                        contadorError=0
                        lblCJJ = Label(ventanaJuego, text=jugador1, bg=c1, font=("Arial", 14)).place(x=1000 + 10,
                                                                                                     y=250 + 10)

                        lblCE = Label(ventanaJuego, text="Cantidad Errores: " + str(contadorError), bg=c1,
                                      font=("Arial", 14)).place(x=1150 + 10,
                                                                y=250 + 10)



            print("Error: "+str(contadorError))

            if cantidad==cantidadPiezasJ1:
                print("Gano Jugador 1")
                messagebox.showinfo("GANADOR: ","Jugador1 " )
                ganador="Jugador 1"
                botonInsertar=Button(ventanaJuego,command=prueba1, text="Insertar", bg=colorb, width=anchob,height=altob, state=DISABLED).place(x=1143, y=250+150)
            elif cantidad==cantidadPiezasJ2:
                print("Gano Jugador 2")
                ganador="Jugador 2"
                messagebox.showinfo("GANADOR:","Jugador2 ")
                botonInsertar = Button(ventanaJuego, command=prueba1, text="Insertar", bg=colorb, width=anchob,
                                       height=altob, state=DISABLED).place(x=1143, y=250 + 150)

            lblCJ1 = Label(ventanaJuego, text="Piezas incertadas Jugador1: " + str(cantidadPiezasJ1), bg="gray63",
                           font=("Arial", 10)).place(x=20, y=700)
            lblCJ2 = Label(ventanaJuego, text="Piezas incertadas Jugador2: " + str(cantidadPiezasJ2), bg="gray63",
                           font=("Arial", 10)).place(x=20, y=730)


        botonInsertar = Button(ventanaJuego,command=prueba1, text="Insertar", bg=colorb, width=anchob,height=altob).place(x=1143, y=250+150)

        botonGuardar=Button(ventanaJuego,command=guardar, text="Guardar partida", bg="goldenrod3", width=anchob,height=altob).place(x=1310, y=250+150+50)
        botonTerminar = Button(ventanaJuego,command=terminar,  text="Terminar partida", bg="goldenrod3", width=anchob,
                              height=altob).place(x=1010, y=250 + 150 + 50)

        lblCJJ = Label(ventanaJuego, text="Panel -----------------------------------------------------------------------------", bg="gray63", font=("Arial", 14)).place(x=1010 ,
                                                                                     y=500)




    botonJugar = Button(ventanaJuego,command=panelJuego, text="Iniciar Juego",bg=colorb,width=anchob,height=altob).place(x=1000+180,y=225)






def reporte():
    wb.open_new(r'reporte.html')


def ayuda():
    ventanaAyuda=Tk()
    ventanaAyuda.title("Ayuda")
    ventanaAyuda.geometry("500x200")
    botonAbrir = Button(ventanaAyuda, text="Sebastian Alejandro de Leon Tenaz, 201906085", bg=colorb, width=45,
                        height=altob).place(x=100, y=80)


ventanaP=Tk()



ventanaP.title("Menu Principal")
ventanaP.geometry("1920x1080")
ventanaP.configure(background="gray20")

DatosJugador1 = ""
DatosJugador2 = ""
ganador=""
#matrizJuego=matriz()
turno=0
turnoJugador=StringVar()
colorb="gray99"
colorb1="sky blue"
anchob=25
altob=1
contadorError=0
cantidadPiezasJ1=0
cantidadPiezasJ2=0

botonAbrir= Button(ventanaP, text="Abrir Archivo",command=buscaArchivo,bg=colorb,width=anchob,height=altob).grid(row=1,column=0)
botonIniciar= Button(ventanaP, text="Iniciar Partida",command=procesoPartida,bg=colorb,width=anchob,height=altob).grid(row=2,column=0)
botonReporte= Button(ventanaP, command=reporte,text="Reporte HTML",bg=colorb,width=anchob,height=altob).grid(row=3,column=0)
botonAyuda= Button(ventanaP,command=ayuda, text="Ayuda",bg=colorb,width=anchob,height=altob).grid(row=4,column=0)




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