import csv

def cargar_productos(nombre_archivo):
    
    productos = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                producto = {
                    'nombre': fila['nombre_producto'],
                    'precio': float(fila['precio']),
                    'descuento': float(fila['porcentaje_descuento'])
                }
                productos.append(producto)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return productos

def calcular_precio_promedio(productos):

    if not productos:
        return 0
    total_precio = sum(producto['precio'] for producto in productos)
    return total_precio / len(productos)

def aplicar_descuento(productos):
    
    for producto in productos:
        aplicar = lambda precio, descuento: precio * (1 - descuento / 100)
        producto['precio_descuento'] = aplicar(producto['precio'], producto['descuento'])

# Un ejemplp:

# Cargar los productos desde el archivo CSV
productos = cargar_productos('productos.csv')

if productos:
    # Calcular el precio promedio
    precio_promedio = calcular_precio_promedio(productos)
    print(f"Precio promedio de los productos: ${precio_promedio:.2f}")

    # Aplicar el descuento a todos los productos
    aplicar_descuento(productos)
    print("Precios de los productos después de aplicar sus descuentos específicos:")
    for producto in productos:
        print(f"{producto['nombre']}: Precio original: ${producto['precio']:.2f}, "
              f"Precio con descuento: ${producto['precio_descuento']:.2f}")
