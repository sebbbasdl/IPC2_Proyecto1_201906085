from Nodos import Nodo, nodoE
from EncabezadosXY import listaE

class matriz:
    def __init__(self):
        self.eFilas=listaE()
        self.eColumnas=listaE()

    def insertarM(self,fila,columna,valor):
        nuevo=Nodo(fila,columna,valor)
        #encabezado por fila
        eFila=self.eFilas.getE(fila)
        if eFila==None:
            eFila= nodoE(fila)
            eFila.accesoNodo=nuevo
            self.eFilas.setE(eFila)
        else:
            if nuevo.columna<eFila.accesoNodo.columna:
                nuevo.derecha=eFila.accesoNodo
                eFila.accesoNodo.izquierda=nuevo
                eFila.accesoNodo=nuevo
            else:
                actual=eFila.accesoNodo
                while actual.derecha !=None:
                    if nuevo.columna<actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha
                if actual.derecha==None:
                    actual.derecha=nuevo
                    nuevo.izquierda=actual

        #encabezada por columna
        eColumna=self.eColumnas.getE(columna)
        if eColumna==None:
            eColumna=nodoE(columna)
            eColumna.accesoNodo=nuevo
            self.eColumnas.setE(eColumna)
        else:
            if nuevo.fila<eColumna.accesoNodo.fila:
                nuevo.abajo=eColumna.accesoNodo
                eColumna.accesoNodo.arriba=nuevo
                eColumna.accesoNodo=nuevo
            else:
                actual=eColumna.accesoNodo
                while actual.abajo!=None:
                    if nuevo.fila<actual.abajo.fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if actual.abajo==None:
                    actual.abajo=nuevo
                    nuevo.arriba=actual

    def recorrerF(self):
        eFila=self.eFilas.primero
        print("\nRecorrido Filas")
        while eFila!=None:
            actual=eFila.accesoNodo
            print("\nFila"+str(actual.fila))
            print("Columna: Valor")
            while actual!=None:
                print(str(actual.columna)+"      "+actual.valor)
                actual=actual.derecha

            eFila=eFila.siguiente
        print("Fin recorrido filas\n")

    def recorrerC(self):
        eColumna=self.eColumnas.primero
        print("\nRecorrido columnas:")
        while eColumna!=None:
            actual=eColumna.accesoNodo
            print("\nColumna"+str(actual.columna))
            print("fila  Valor")
            while actual!=None:
                print(str(actual.fila)+"      "+actual.valor)
                actual=actual.abajo
            eColumna=eColumna.siguiente
        print("Fin recorrido columnas\n")

    def obtenerValorporPosicion(self,fila,columna):
        eFila=self.eFilas.primero
        while eFila!=None:
            actual=eFila.accesoNodo
            while actual!=None:
                if actual.fila==fila and actual.columna==columna:
                    actual1=actual.valor
                    print(actual1)
                    return actual1

                actual=actual.derecha
            eFila=eFila.siguiente
"""prueba=matriz()
prueba.insertarM(1,0,"rojo")
prueba.insertarM(1,2,"None")

prueba.recorrerC()
prueba.recorrerF()

valorxd=str(prueba.obtenerValorporPosicion(1,0))
valor=str(prueba.obtenerValorporPosicion(1,2))

print(valorxd)
print(valor)"""
