from core import c
from dibujo import DibujoPrincipal
from radial import radial_factory
from utils import ExportadorDeFotogramas

dibujo_principal = DibujoPrincipal(radial_factory.radiales())
exportador_fotogramas = ExportadorDeFotogramas(core=c, frecuencia_exportacion=1)

def setup():
    size(c.ancho, c.alto)
    frameRate(100)
    background(c.bg_color, c.bg_alpha)

def draw():
    dibujo_principal.dibujar()
    c.dibujar()
    exportador_fotogramas()

def stop():
    exportador_fotogramas.exportar_fin()
