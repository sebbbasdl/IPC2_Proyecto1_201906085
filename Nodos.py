class Nodo:
    def __init__(self,fila,columna,valor):
        self.valor = valor
        self.fila=fila
        self.columna=columna
        self.derecha=None
        self.izquierda = None
        self.arriba = None
        self.abajo = None


class nodoE:
    def __init__(self,lugar):
        self.lugar=lugar
        self.siguiente=None
        self.anterior = None
        self.accesoNodo=None