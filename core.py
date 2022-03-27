ANCHO = 1000
ALTO = 1000

class Core:
    _n_fotograma = 0
    _imprimirFotograma = True
    
    @property
    def n_fotograma(self): return self._n_fotograma
    
    @property
    def ancho(self): return ANCHO
    
    @property
    def alto(self): return ALTO
    
    @property
    def bg_color(self): return 20
    @property
    def bg_alpha(self): return 240

    
    @property
    def centro_x(self): return self.ancho / 2
    
    @property
    def centro_y(self): return self.alto / 2
    
    def dibujar(self):
        self._contarFotograma()
    
    def _contarFotograma(self):
        if self._imprimirFotograma: print(self._n_fotograma)
        self._n_fotograma += 1
        

c = Core()

class ConCore:
    core = c
    
    @property
    def c(self): return self.core
