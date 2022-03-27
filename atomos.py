from core import ConCore
from dibujo import Dibujo
from utils import levantarExcepcion, GenaradorRuido



class Atomo(Dibujo, ConCore):
    pass

class PuntoSimple(Atomo):
    def __init__(self):
        self._base_color = random(150, 255)
        self._ruido_color = GenaradorRuido(.02)
        
        self._ruido_ancho = GenaradorRuido(.008)
        self._ancho = int(random(15, 20))
        
    def dibujar(self, posicion):
        self._setear_propiedades_dibujo(posicion)
        point(posicion.x, posicion.y)
        self._resetear_propiedades_dibujo()
        
    
    def _setear_propiedades_dibujo(self, posicion):
        pushStyle()
        
        dist_centro = dist(self.c.centro_x, self.c.centro_y, posicion.x, posicion.y)
        color_punto = self._base_color *  ((dist_centro / 500) + (self._ruido_color() * .5)) 
        stroke(color_punto, 100)
        strokeWeight(self._ancho * (1 - self._ruido_ancho()*.5))
        strokeCap(ROUND)
        
        
    
    def _resetear_propiedades_dibujo(self):
        popStyle()

class LineaSimple(Atomo):
    def dibujar(self, centro):
        print("LineaSimple", "dibujando")
