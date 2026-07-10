from validaciones import validar_str, validar_int, validar_float, validar_bool
from logica import obtener_ids, mostrar_info_completa_matriz, obtener_list_diccionario_productos,\
        do_bubble_sort, obtener_productos_activos, parsear_str_a_booleano, mostrar_info_completa

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
    activo = validar_bool("ingrese si esta activo [true - false]: ")

    nuevo_producto = [nuevo_id, nombre, stock, precio_unitario, activo]

    matriz_producto.append(nuevo_producto)
    print("producto agregado correctamente\n")
    mostrar_info_completa_matriz(matriz_producto)

def actualizar_producto(matriz_producto: list[list], producto_modificado: list, id: int):
    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][0] == id:
            for columna in range(1, cantidad_columnas):
                matriz_producto[fila][columna] = producto_modificado[columna]
    print("el producto fue modificado\n")
    lista_dict_productos = obtener_list_diccionario_productos(matriz_producto)
    productos_activos = obtener_productos_activos(lista_dict_productos)
    mostrar_info_completa(productos_activos, "productos")

def modificar_producto(matriz_producto: list[list]):
    mostrar_info_completa_matriz(matriz_producto)
    input_int = validar_int("ingresar ID del prodcuto a modificar: ")
    producto_a_modificar = obtener_producto_por_dato(matriz_producto, 0, input_int)
    info = f'{producto_a_modificar[0]},{producto_a_modificar[1]},{producto_a_modificar[2]},{producto_a_modificar[3]},'\
        f'{producto_a_modificar[4]}\n'
    if producto_a_modificar:
        print("el producto a modificar es\n")
        print(info)
        opcion = validar_str("que dato desea modificar? [nombre, inventario, precio, activo]: ")

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
            case "activo":
                activo = validar_bool("nuevo estado [True - False]: ")
                producto_a_modificar[4] = activo
            case _:
                print("la opcion no coincide, producto no modificado")
                return
        
        actualizar_producto(matriz_producto, producto_a_modificar, input_int)
    else:
        print("ERROR: no se encontro el id seleccionado")

def borrar_producto(matriz_producto:list[list]) -> bool:
    mostrar_info_completa_matriz(matriz_producto)

    dado_de_baja = False
    input_id = validar_int("ingrese el numero id a dar de baja: ")
    input_modo = validar_str("[logica - fisica]: ")

    match input_modo:
        case "logica":
            for fila in range(len(matriz_producto)):
                if matriz_producto[fila][0] == input_id:
                    matriz_producto[fila][4] = False
                    print("producto ahora esta inactivo\n")
                    dado_de_baja = True
                    break
        case "fisica":
            for fila in range(len(matriz_producto)):
                if matriz_producto[fila][0] == input_id:
                    matriz_producto.pop(fila)
                    print("producto borrado\n")
                    dado_de_baja = True
                    break
        case _:
            print("opcion no valida")
            return
        
    if not dado_de_baja:
         print("no se encontro el producto")

    mostrar_info_completa_matriz(matriz_producto)
    return dado_de_baja

def ver_productos_ord(matriz_producto: list[list], clave: str, ord: str):
    lista_dict_productos = obtener_list_diccionario_productos(matriz_producto)
    productos_activos = obtener_productos_activos(lista_dict_productos)
    do_bubble_sort(productos_activos, clave, "productos", ord)