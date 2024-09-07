from materiales import MaterialAluminio, Vidrio
from ventana import Ventana

class Cotizacion:
    def __init__(self, ventana, material_aluminio, vidrio, cantidad=1):
        self.ventana = ventana
        self.material_aluminio = material_aluminio
        self.vidrio = vidrio
        self.cantidad = cantidad

    def calcular_costo(self):
        costo_total = 0
        for nave_ancho, nave_alto in self.ventana.naves:
            # Cálculo del aluminio
            perimetro_nave = (nave_ancho + nave_alto) * 2  # Perímetro de la nave
            costo_aluminio = (perimetro_nave - 8) * 2.5 * (self.material_aluminio.precio_por_metro / 100)  # Se descuentan las esquinas
            # Cálculo del vidrio
            area_vidrio = (nave_ancho - 3) * (nave_alto - 3)  # Restamos los márgenes de inserción
            costo_vidrio = area_vidrio * self.vidrio.precio_por_cm2
            # Costo de esquinas y chapas (si aplica)
            costo_esquinas = 4 * 4310
            costo_chapa = 16200 if 'X' in self.ventana.estilo else 0

            costo_nave = costo_aluminio + costo_vidrio + costo_esquinas + costo_chapa
            costo_total += costo_nave

        # Si la cantidad es mayor a 100, aplica un descuento del 10%
        if self.cantidad > 100:
            costo_total *= 0.9

        return costo_total * self.cantidad
