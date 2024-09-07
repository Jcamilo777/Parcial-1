class Ventana:
    estilos_validos = ['O', 'XO', 'OXXO', 'OXO']

    def __init__(self, ancho, alto, estilo):
        if estilo not in Ventana.estilos_validos:
            raise ValueError("Estilo de ventana no válido.")
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.naves = self.calcular_naves()

    def calcular_naves(self):
        # Distribuye el ancho según el número de naves basado en el estilo
        if self.estilo == 'O':
            return [(self.ancho, self.alto)]
        elif self.estilo == 'XO':
            return [(self.ancho / 2, self.alto), (self.ancho / 2, self.alto)]
        elif self.estilo == 'OXXO':
            return [(self.ancho / 4, self.alto), (self.ancho / 4, self.alto), (self.ancho / 4, self.alto), (self.ancho / 4, self.alto)]
        elif self.estilo == 'OXO':
            return [(self.ancho / 3, self.alto), (self.ancho / 3, self.alto), (self.ancho / 3, self.alto)]
        else:
            raise ValueError("Estilo de ventana no reconocido.")
