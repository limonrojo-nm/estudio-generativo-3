from core import ConCore
from dibujo import Dibujo
from atomos import LineaSimple, PuntoSimple
from utils import Punto, GenaradorRuido

class Radial(Dibujo, ConCore):
    _fotogramas_por_giro = 90
    
    
    def __init__(self, atomo):
        self._amplitud_noise = GenaradorRuido(.001)
        self._angulo_noise = GenaradorRuido(.005)
        self._amplitud_maxima_noise = GenaradorRuido(.005)
        self._atomo = atomo
    
    @property
    def atomo(self): return self._atomo
    @property
    def fotogramas_por_giro(self): return self._fotogramas_por_giro
    @property
    def amplitud_maxima(self): return (self.c.alto + self.c.ancho) / 2 * .7 * self._amplitud_maxima_noise()
    
    
    def dibujar(self):
        """
        Va a dibujar el atomo en una altura determinada,
        en el angulo determinado que le corresponda segun la circunsferencia
        """
        # self.angulo
        self.atomo.dibujar(self._atomo_posicion_actual)

    @property
    def _atomo_posicion_actual(self):
        pos_x = sin(self._angulo_actual) * self._amplitud_actual + self.c.centro_x
        pos_y = cos(self._angulo_actual) * self._amplitud_actual + self.c.centro_y
        return Punto(
            pos_x,
            pos_y
        )
    
    @property
    def _angulo_actual(self):
        """En radianes"""
        
        angulo_actual = PI*2 * (float(self.c.nFotograma) / self.fotogramas_por_giro + self._angulo_noise())
        return angulo_actual
    
    @property
    def _amplitud_actual(self):
        return self.amplitud_maxima * self._amplitud_noise()
        


el_radial = Radial(atomo=PuntoSimple())
        
