from core import ConCore
from utils import levantarExcepcion

class Dibujo:
    def dibujar(self): levantarExcepcion("ERROR: No implementado", self)

class DibujoPrincipal(ConCore, Dibujo):
    _alpha_bg = .0
    
    def __init__(self, dibujos):
        """
        @dibujos: [Dibujo]
        """
        self.dibujos = dibujos
    
    def dibujar(self):
        self._manejar_reset_fondo()
        for dibujo in self.dibujos:
            dibujo.dibujar()
        
    def _manejar_reset_fondo(self):
        pushStyle()
        fill(0, 255 * self._alpha_bg)
        rect(0, 0, self.c.ancho, self.c.alto)
        popStyle()
