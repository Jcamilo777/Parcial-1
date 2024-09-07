# Proyecto de Cotización de Ventanas PQR

Este proyecto tiene como objetivo automatizar el proceso de cotización de ventanas en la empresa PQR, mejorando la precisión y eficiencia en la estimación de costos según las especificaciones del cliente. El sistema permite calcular el costo total de las ventanas en función de las dimensiones, el estilo, el acabado de aluminio, el tipo de vidrio, y los descuentos aplicables.

## Descripción

El sistema permite a los usuarios ingresar los datos necesarios para generar una cotización precisa de las ventanas:
- **Estilos de ventanas**: O, XO, OXXO, OXO.
- **Acabados de aluminio**: pulido, lacado brillante, lacado mate, anodizado.
- **Tipos de vidrio**: transparente, bronce, azul.
- **Opción de vidrio esmerilado**.
- **Descuento**: 10% para pedidos superiores a 100 ventanas.

## Requerimientos

- **Python 3.x** debe estar instalado.
- El sistema no tiene dependencias adicionales fuera de las bibliotecas estándar de Python.
- Archivos del proyecto:
  - `main.py`: Archivo principal para ejecutar la aplicación.
  - `materiales.py`: Contiene las clases `MaterialAluminio` y `Vidrio`.
  - `ventana.py`: Contiene la clase `Ventana`.
  - `cotizacion.py`: Contiene la clase `Cotizacion` que realiza los cálculos de costos.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/proyecto_cotizacion_ventanas.git

2. Navega al directorio del proyecto:

```bash
cd proyecto_cotizacion_ventanas

```

3. Ejecuta el programa:

```bash
python main.py
```

## Uso
El sistema solicitará los siguientes datos para generar la cotización:

Dimensiones de la ventana (ancho y alto en centímetros).
Estilo de la ventana (O, XO, OXXO, OXO).
Tipo de acabado de aluminio (pulido, lacado brillante, lacado mate, anodizado).
Tipo de vidrio (transparente, bronce, azul).
Vidrio esmerilado (Sí o No).
Cantidad de ventanas.
