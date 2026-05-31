from validaciones import validar_str, validar_int, validar_float

def crear_matriz(filas: int) -> list[list]:
    matriz = []

    for fila in range(filas):
        matriz.append([])

    return matriz

def obtener_ids(matriz_productos: list[list]) -> list:
    lista_ids = []

    cantidad_filas = len(matriz_productos)

    for fila in range(cantidad_filas):
        lista_ids.append(matriz_productos[fila][0])
    
    return lista_ids

def obtener_producto_por_dato(matriz_producto: list[list], columna: int, valor) -> list:
    producto = []

    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][columna] == valor:
            for columna in range(cantidad_columnas):
                 producto.append(matriz_producto[fila][columna])

    return producto
    
def cargar_producto(matriz_producto: list[list]):
    ids = obtener_ids(matriz_producto)
    ids.reverse()
    
    obtener_ultimo_id = ids[0]
    nuevo_id = obtener_ultimo_id + 1

    nombre = validar_str("ingresar nombre del producto: ")
    stock = validar_int("stock disponible: ")
    precio_unitario = validar_float("ingrese precio unitario: ")

    nuevo_producto = [nuevo_id, nombre, stock, precio_unitario]

    matriz_producto.append(nuevo_producto)
    print("producto agregado correctamente")
    print(matriz_producto)

def actualizar_producto(matriz_producto: list[list], producto_modificado: list, id: int):
    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][0] == id:
            for columna in range(1, cantidad_columnas):
                matriz_producto[fila][columna] = producto_modificado[columna]

    print("producto actualizado")
    print(matriz_producto)

def modificar_producto(matriz_producto: list[list]):

    input_int = validar_int("ingresar ID del prodcuto a modificar: ")
    producto_a_modificar = obtener_producto_por_dato(matriz_producto, 0, input_int)
    print("el producto a modificar es: ")
    print(producto_a_modificar)
    opcion = input("que dato desea modificar? [nombre, inventario, precio]: ")

    match opcion:
        case "nombre":
            nuevo_nombre = validar_str("nuevo nombre: ")
            producto_a_modificar[1] = nuevo_nombre
        case "inventario":
            nuevo_stock = validar_int("nuevo stock: ")
            producto_a_modificar[2] = nuevo_stock
        case "precio":
            nuevo_precio = validar_float("nuevo precio: ")
            producto_a_modificar[3] = nuevo_precio
        case _:
            print("la opcion no coincide")
    
    actualizar_producto(matriz_producto, producto_a_modificar, input_int)

    