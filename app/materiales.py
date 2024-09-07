class MaterialAluminio:
    precios = {
        'pulido': 50700,
        'lacado_brillante': 54200,
        'lacado_mate': 53600,
        'anodizado': 57300
    }

    def __init__(self, tipo):
        if tipo not in MaterialAluminio.precios:
            raise ValueError("Tipo de aluminio no válido.")
        self.tipo = tipo
        self.precio_por_metro = MaterialAluminio.precios[tipo]


class Vidrio:
    precios = {
        'transparente': 8.25,
        'bronce': 9.15,
        'azul': 12.75
    }

    def __init__(self, tipo, esmerilado=False):
        if tipo not in Vidrio.precios:
            raise ValueError("Tipo de vidrio no válido.")
        self.tipo = tipo
        self.precio_por_cm2 = Vidrio.precios[tipo]
        self.esmerilado = esmerilado
        if esmerilado:
            self.precio_por_cm2 += 5.20  # Costo adicional por el esmerilado
