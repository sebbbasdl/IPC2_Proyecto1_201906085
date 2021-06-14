from tkinter import *
from tkinter import filedialog

raiz=Tk()


def buscaArchivo():
    archivo = filedialog.askopenfilename(title="Abrir")
    print(archivo)

def procesoPartida():
    ventana2 = Tk()
    ventana2.geometry("500x300+100+100")
    ventana2.title("Obteniendo Valores")
    lblC = Label(ventana2,text="Ingrese el tamaño del tablero:", font=("Agency FB", 14)).place(x=10, y=10)
    lblF = Label(ventana2,text="No. de Filas:", font=("Agency FB", 10)).place(x=20, y=50)
    lblCol = Label(ventana2,text="No. de Columnas:", font=("Agency FB", 10)).place(x=270, y=50)
    
    
    entradaF = IntVar()
    entradaC = IntVar()
    txtF = Entry(ventana2, textvariable=entradaF).place(x=70, y=50)
    txtC = Entry(ventana2, textvariable=entradaC).place(x=340, y=50)




    print("Obteniendo valores del tablero mxn")

    def panelJuego():
        m=entradaF.get()
        n=entradaC.get()

        ventanaJuego = Tk()
        ventanaJuego.geometry("1920x1080")
        ventanaJuego.title("Juego")

        print(m)
        print(n)
        for m1 in range(m):
            for n1 in range(n):
                Bespacio = Button(ventanaJuego, bg="red", width=1, height=1).grid(row=2 + m1, column=6 + n1)
        print("Realizando Tablero")


    botonJugar = Button(ventana2,command=panelJuego, text="Iniciar Juego",bg=colorb,width=anchob,height=altob).place(x=180,y=250)







ventanaP=Tk()
ventanaP.title("Menu Principal")
ventanaP.geometry("1920x1080")
ventanaP.configure(background="gray20")

colorb="gray99"
colorb1="sky blue"
anchob=25
altob=1

botonAbrir= Button(ventanaP, text="Abrir Archivo",command=buscaArchivo,bg=colorb,width=anchob,height=altob).grid(row=1,column=0)
botonIniciar= Button(ventanaP, text="Iniciar Partida",command=procesoPartida,bg=colorb,width=anchob,height=altob).grid(row=2,column=0)
botonTablero= Button(ventanaP, text="Tablero",bg=colorb,width=anchob,height=altob).grid(row=3,column=0)
botonReporte= Button(ventanaP, text="Reportes",bg=colorb,width=anchob,height=altob).grid(row=4,column=0)



ventanaP.mainloop()