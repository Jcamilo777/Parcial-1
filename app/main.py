# main.py

from materiales import MaterialAluminio, Vidrio
from ventana import Ventana
from cotizacion import Cotizacion

def solicitar_dato(prompt, tipo_dato=str, opciones=None):
    while True:
        try:
            dato = tipo_dato(input(prompt))
            if opciones and dato not in opciones:
                raise ValueError
            return dato
        except ValueError:
            print(f"Por favor, ingrese un valor válido de tipo {tipo_dato.__name__}" + 
                  (f" entre {opciones}" if opciones else ""))

def main():
    print("Bienvenido al sistema de cotización de ventanas PQR")

    # Solicitar datos al usuario
    ancho = solicitar_dato("Ingrese el ancho de la ventana (en cm): ", float)
    alto = solicitar_dato("Ingrese el alto de la ventana (en cm): ", float)
    estilo = solicitar_dato(
        "Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ", str, ['O', 'XO', 'OXXO', 'OXO']
    )
    tipo_acabado = solicitar_dato(
        "Ingrese el tipo de acabado de aluminio (pulido, lacado_brillante, lacado_mate, anodizado): ",
        str, ['pulido', 'lacado_brillante', 'lacado_mate', 'anodizado']
    )
    tipo_vidrio = solicitar_dato(
        "Ingrese el tipo de vidrio (transparente, bronce, azul): ", str, ['transparente', 'bronce', 'azul']
    )
    esmerilado = solicitar_dato(
        "¿Desea vidrio esmerilado? (si/no): ", str, ['si', 'no']
    ) == 'si'
    cantidad = solicitar_dato("Ingrese la cantidad de ventanas: ", int)

    # Creación de objetos con los datos proporcionados
    ventana = Ventana(ancho, alto, estilo)
    material_aluminio = MaterialAluminio(tipo_acabado)
    vidrio = Vidrio(tipo_vidrio, esmerilado)

    # Cálculo de la cotización
    cotizacion = Cotizacion(ventana, material_aluminio, vidrio, cantidad)
    costo_total = cotizacion.calcular_costo()

    # Mostrar resultado
    print(f"\nEl costo total para {cantidad} ventanas es: ${costo_total:.2f}")

if __name__ == "__main__":
    main()
