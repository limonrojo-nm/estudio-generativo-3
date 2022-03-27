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
    
    def __init__(self, incremento):
        self._incremento = incremento
    
    def __call__(self):
        self._incrementar_offset()
        return noise(self.noise_offset)
    
    @property
    def incremento(self): return self._incremento
    
    @property
    def noise_offset(self): return self._noise_offset
    
    def _incrementar_offset(self):
        self._noise_offset += self.incremento
