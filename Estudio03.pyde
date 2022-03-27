from core import c
from dibujo import DibujoPrincipal
from radial import el_radial
dibujoPrincipal = DibujoPrincipal([el_radial])

def setup():
    size(c.ancho, c.alto)
    frameRate(100)
    background(20, 250)

def draw():
    dibujoPrincipal.dibujar()
    c.dibujar()
