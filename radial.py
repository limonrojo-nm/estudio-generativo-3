from core import ConCore
from dibujo import Dibujo
from atomos import LineaSimple, PuntoSimple, PuntoComplejo, generar_punto_complejo
from utils import Punto, GenaradorRuido

class Radial(Dibujo, ConCore):
    _fotogramas_por_giro = 90
    
    
    def __init__(self, atomo, factor_giro=1):
        self._amplitud_noise = GenaradorRuido(.005)
        self._angulo_noise = GenaradorRuido(.005)
        self._amplitud_maxima_noise = GenaradorRuido(.005)
        self._atomo = atomo
        self._factor_giro = factor_giro
    
    @property
    def atomo(self): return self._atomo
    @property
    def factor_giro(self): return self._factor_giro
    @property
    def fotogramas_por_giro(self): return self._fotogramas_por_giro
    @property
    def amplitud_maxima(self): return (self.c.alto + self.c.ancho) / 2 * .9 * self._amplitud_maxima_noise()
    
    
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
        
        angulo_actual = PI*2 * (float(self.c.n_fotograma) * self.factor_giro / self.fotogramas_por_giro + self._angulo_noise())
        return angulo_actual
    
    @property
    def _amplitud_actual(self):
        return self.amplitud_maxima * self._amplitud_noise()
        
class RadialFactory:
    _radiales = []
    _radiales_generados = False
    
    def __init__(self, cantidad=1):
        self._cantidad = cantidad
        self._atomo = PuntoComplejo()
    
    @property
    def cantidad(self): return self._cantidad
    
    def radiales(self):
        self._manejar_generacion()
        return self._radiales
    
    def _manejar_generacion(self):
        if not self._radiales_generados:
            for _ in range(self.cantidad):
                self._radiales.append(
                   Radial(atomo=PuntoSimple(), factor_giro=random(-1, 1)) 
                )
            self._radiales_generados = True


radial_factory = RadialFactory(100)

        
