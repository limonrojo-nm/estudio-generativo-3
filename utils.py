
def levantarExcepcion(msg, obj=None):
    obj_detail = " @> " + str(obj.__class__) if obj is not None else ""
    print(msg + obj_detail)
    raise Exception()


class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self): return self._x
    
    @property
    def y(self): return self._y


class GenaradorRuido:
    _noise_offset = 0.0
    
    def __init__(self, incremento, amplitud_fija=1):
        self._incremento = incremento
        self._amplitud_fija = amplitud_fija
        self._semilla_random = int(random(90000))
        
    
    def __call__(self):
        self._incrementar_offset()
        noiseSeed(self._semilla_random)
        return noise(self.noise_offset)
    
    @property
    def incremento(self): return self._incremento
    
    @property
    def amplitud_fija(self): return self._amplitud_fija
    
    @property
    def noise_offset(self): return self._noise_offset
    
    def _incrementar_offset(self):
        self._noise_offset += self.incremento


class ExportadorDeFotogramas:
    def __init__(self, core, frecuencia_exportacion=1, ceros_n_fotograma=5):
        self._c = core
        self._frecuencia_exportacion = frecuencia_exportacion
        self._ceros_n_fotograma = ceros_n_fotograma
        self._codigo_seq = str(random(99999)).zfill(5)
    
    @property
    def c(self): return self._c
    @property
    def frecuencia_exportacion(self): return self._frecuencia_exportacion
    @property
    def ceros_n_fotograma(self): return self._ceros_n_fotograma
    
    def __call__(self):
        if (self.c.n_fotograma % self.frecuencia_exportacion) == 0:
            save("frames/" + self._codigo_seq + "/" + str(self.c.n_fotograma).zfill(self.ceros_n_fotograma) + ".png")
    
    def exportar_fin(self):
        save("output/FINAL-" + self._codigo_seq + ".png")
    
