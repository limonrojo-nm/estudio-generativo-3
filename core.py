ANCHO = 1000
ALTO = 1000

class Core:
    _nFotograma = 0
    _imprimirFotograma = True
    
    @property
    def nFotograma(self): return self._nFotograma
    
    @property
    def ancho(self): return ANCHO
    
    @property
    def alto(self): return ALTO
    
    @property
    def centro_x(self): return self.ancho / 2
    
    @property
    def centro_y(self): return self.alto / 2
    
    def dibujar(self):
        self._contarFotograma()
    
    def _contarFotograma(self):
        if self._imprimirFotograma: print(self._nFotograma)
        self._nFotograma += 1
        

c = Core()

class ConCore:
    core = c
    
    @property
    def c(self): return self.core
