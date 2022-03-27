from dibujo import Dibujo
from utils import levantarExcepcion

class Atomo(Dibujo):
    pass

class PuntoSimple(Atomo):
    def dibujar(self, posicion):
        self._setear_propiedades_dibujo()
        point(posicion.x, posicion.y)
        
    def _setear_propiedades_dibujo(self):
        stroke(255)
        strokeWeight(3)
        strokeCap(ROUND)

class LineaSimple(Atomo):
    def dibujar(self, centro):
        print("LineaSimple", "dibujando")
