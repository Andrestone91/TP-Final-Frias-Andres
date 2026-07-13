from validaciones import validar_str, validar_int, validar_float, validar_bool
from logica import obtener_ids, mostrar_info_completa_matriz, obtener_list_diccionario_productos,\
        do_bubble_sort, mostrar_info_completa, filtrar_dato_dict, filtrar_por_activo
from archivos import guardar_matriz_archivo
from variables import ARCHIVO_PRODUCTOS

def obtener_producto_por_dato(matriz_producto: list[list], columna: int, valor) -> list:
    """
    obtiene un producto en formato lista mediante su ID

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista
        columna (int): columna donde se va a buscar el valor
        valor: valor a buscar en la columna

    return:
        producto (list): contiene el producto encontrado en formato
    """
    producto = []

    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][columna] == valor:
            for columna in range(cantidad_columnas):
                 producto.append(matriz_producto[fila][columna])

    return producto
    
def obtener_cabecera_productos() -> list[str]:
    """
    obtiene la cabecera de los productos

    arg:

    return:
        cabecera (list[str]): contiene la cabecera de los productos
    """
    cabecera = ["id","nombre","inventario","precio","activo"]
    return cabecera

def cargar_producto(matriz_producto: list[list]):
    """
    agrega un nuevo producto a la lista

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista

    return:
    """

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

    cabecera = obtener_cabecera_productos()

    guardar_matriz_archivo(matriz_producto, cabecera, ARCHIVO_PRODUCTOS)
    mostrar_info_completa_matriz(matriz_producto)

def actualizar_producto(matriz_producto: list[list], producto_modificado: list, id: int):
    """
    actualiza un producto en la lista

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista
        producto_modificado (list): contiene el producto modificado en formato de lista
        id (int): id del producto a modificar

    return:
    """
    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][0] == id:
            for columna in range(1, cantidad_columnas):
                matriz_producto[fila][columna] = producto_modificado[columna]

    cabecera = obtener_cabecera_productos()

    guardar_matriz_archivo(matriz_producto, cabecera, ARCHIVO_PRODUCTOS)

    lista_dict_productos = obtener_list_diccionario_productos(matriz_producto)
    productos_activos = filtrar_dato_dict(lista_dict_productos, filtrar_por_activo, "true")

    mostrar_info_completa(lista_dict_productos, "productos")

def modificar_producto(matriz_producto: list[list]):
    """
    funcion para modificar un producto

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista

    return:
    """
    mostrar_info_completa_matriz(matriz_producto)
    input_int = validar_int("ingresar ID del prodcuto a modificar: ")
    producto_a_modificar = obtener_producto_por_dato(matriz_producto, 0, input_int)

    if not producto_a_modificar:
        print("producto no encontrado")
        return
    
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
    """
    borra un producto de la lista

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista

    return:
        dado_de_baja (bool): devuelve true si se borro el producto, de lo contrario false
    """
    mostrar_info_completa_matriz(matriz_producto)

    dado_de_baja = False
    input_id = validar_int("ingrese el numero id a dar de baja: ")
    input_modo = validar_str("[logica - fisica]: ")

    cabecera = obtener_cabecera_productos()

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
         return
    
    guardar_matriz_archivo(matriz_producto, cabecera, ARCHIVO_PRODUCTOS)
    mostrar_info_completa_matriz(matriz_producto)
    return dado_de_baja

def ver_productos_ord(matriz_producto: list[list], clave: str, ord: str):
    """
    muestra los productos ordenados por la clave y el orden ingresado

    arg: 
        matriz_producto (list[list]): contiene la lista de productos en formato de lista
        clave (str): clave por la cual se va a ordenar
        ord (str): orden ascendente o descendente

    return:
    """
    lista_dict_productos = obtener_list_diccionario_productos(matriz_producto)
    productos_activos = filtrar_dato_dict(lista_dict_productos, filtrar_por_activo, "true")
    do_bubble_sort(productos_activos, clave, "productos", ord)