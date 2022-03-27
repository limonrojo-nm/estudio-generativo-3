from core import ConCore
from utils import levantarExcepcion

class Dibujo:
    def dibujar(self): levantarExcepcion("ERROR: No implementado", self)

class DibujoPrincipal(ConCore, Dibujo):
    def __init__(self, dibujos):
        """
        @dibujos: [Dibujo]
        """
        self.dibujos = dibujos
    
    def dibujar(self):
        for dibujo in self.dibujos:
            dibujo.dibujar()
