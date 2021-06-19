from Nodos import Nodo, nodoE

class listaE:
    def __init__(self, primero=None):
        self.primero=primero

    def setE(self,nuevo):
        if self.primero==None:
            self.primero=nuevo
        elif nuevo.lugar<self.primero.lugar:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente!=None:
                if nuevo.lugar<actual.siguiente.lugar:
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente

            if actual.siguiente==None:
                actual.siguiente=nuevo
                nuevo.anterior=actual

    def getE(self,lugar):
        actual= self.primero
        while actual!= None:
            if actual.lugar==lugar:
                return actual
            actual=actual.siguiente
        return None