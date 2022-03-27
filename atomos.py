from core import ConCore
from dibujo import Dibujo
from utils import levantarExcepcion, GenaradorRuido, semilla_random_factory



class Atomo(Dibujo, ConCore):
    pass

class PuntoSimple(Atomo):
    def __init__(self):
            
        self._base_color = random(150, 255)
        self._ruido_color = GenaradorRuido(.02)
        self._ruido_x = GenaradorRuido(.07)
        self._ruido_y = GenaradorRuido(.08)
        
        self._ruido_ancho = GenaradorRuido(.008)
        self._ancho = int(random(15, 20))
        
    def dibujar(self, posicion):
        
        self._setear_propiedades_dibujo(posicion)
        
        point(self.pos_x(posicion), self.pos_y(posicion))
        # point(posicion.x, posicion.y)
        self._resetear_propiedades_dibujo()
        
    
    def pos_x(self, posicion):
        print("self.dispersion_x", self.dispersion_x)
        return posicion.x + (self.dispersion_x * (self._ruido_x()-.5))
    
    def pos_y(self, posicion):
        return posicion.y + (self.dispersion_y * (self._ruido_y()-.5))
    
    @property
    def dispersion_x(self): return (float(mouseX) / self.c.ancho) * 1000
    @property
    def dispersion_y(self): return (float(mouseY) / self.c.alto) * 1000
    
    def _setear_propiedades_dibujo(self, posicion):
        pushStyle()
        
        dist_centro = dist(self.c.centro_x, self.c.centro_y, posicion.x, posicion.y)
        color_punto = self._base_color *  ((dist_centro / 500) + (self._ruido_color() * .5)) 
        stroke(color_punto, 60)
        strokeWeight(self._ancho * (1 - self._ruido_ancho()*.5))
        strokeCap(ROUND)
    
    def _resetear_propiedades_dibujo(self):
        popStyle()

class PuntoComplejo(Atomo):
    _puntos = []
    def __init__(self):
        cantidad = int(random(3, 7))
        print("cantidad", cantidad)
        for i in range(cantidad):
            
            self._puntos.append(PuntoSimple())
        # self._puntos = [PuntoSimple(), PuntoSimple(), PuntoSimple()]
        
    def dibujar(self, posicion):    
        for punto in self._puntos:
            punto.dibujar(posicion)

def generar_punto_complejo():
    return PuntoComplejo()

class LineaSimple(Atomo):
    def dibujar(self, centro):
        print("LineaSimple", "dibujando")
