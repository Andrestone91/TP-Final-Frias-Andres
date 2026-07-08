import os
from variables import ARCHIVO_CLIENTES, ARCHIVO_PRODUCTOS, ARCHIVO_USUARIOS, ARCHIVO_VENTAS, ARCHIVO_DETALLE_VENTA
from archivos import leer_json, leer_csv
from validaciones import validar_opcion
from mensajes import  mensaje_menu_area_productos, mensaje_menu_ver_productos,\
      mensaje_menu_clientes, mensaje_menu_ver_clientes, mensaje_menu_ventas, mensaje_menu_ver_ventas, mensaje_menu, imprimir_menu,\
          mensaje_menu_salir, mensaje_menu_usuarios, mensaje_menu_informes
from logica import do_bubble_sort, parsear_dataset_producto_matriz, parsear_dataset_lidict, parsear_dict_valor
from clientes import cargar_cliente, modificar_cliente, borrar_cliente, mostrar_cliente_por_ciudad
from ventas import cargar_venta, mostrar_info_completa_ventas, borrar_venta
from login import iniciar_sesion
from usuarios import mostrar_usuarios, borrar_usuario, crear_usuario, editar_usuario
from detalle_ventas import mostrar_producto_mas_vendido
from productos import cargar_producto, modificar_producto, borrar_producto, ver_productos_ord

def menu_area_productos(matriz_productos: list[list], usuario: dict):
    """
    menu para area de productos

    arg: 
        matriz_productos (list[list]): contiene la matriz de productos
        usuarios (dict): el usuario con el que se inicio sesion
        
    return
    """
    if usuario:
        run = True

        while run:
            mensaje_menu_area_productos()
            opcion_input = validar_opcion(1,5)
       
            match opcion_input:
                case 1:
                    cargar_producto(matriz_productos)
                case 2:
                    modificar_producto(matriz_productos)
                case 3:
                    ver_productos(matriz_productos)
                case 4:
                    borrar_producto(matriz_productos)
                case 5:
                    run = False
    else:
        print('Primero tiene que loguear en el sistema')


def ver_productos(matriz_productos: list[list]):
    """
    menu para ver productos

    arg: 
        
    return
    """
    run = True

    while run:
        mensaje_menu_ver_productos()
        opcion_input = validar_opcion(1,4)

        match opcion_input:
            case 1:
                ver_productos_ord(matriz_productos, "id", "ASC")
            case 2:
                ver_productos_ord(matriz_productos, "stock", "ASC")
            case 3:
                ver_productos_ord(matriz_productos, "nombre", "ASC")
            case 4:
                run = False

def menu_area_clientes(lista_clientes: list[dict], usuario: dict):
    """
    menu para area de clientes

    arg:
      lista_clientes (list[dict]): lista de clientes
      usuario (dict): usuarios en diccionario
    return
    """
    if usuario:
        run = True
        while run:
            mensaje_menu_clientes()
            opcion_input = validar_opcion(1,5)
            match opcion_input:
                case 1:
                    cargar_cliente(lista_clientes)
                case 2:
                    modificar_cliente(lista_clientes)
                case 3:
                    menu_ver_clientes(lista_clientes)
                case 4:
                    borrar_cliente(lista_clientes)
                case 5:
                    run = False
    else:
        print('Primero tiene que loguear en el sistema')

def menu_ver_clientes(lista_clientes: list[dict]):
    """
    menu ver clientes

    arg:
      lista_clientes (list[dict]): lista de clientes

    return
    """
    run = True
    nombre_lista = "clientes"
    while run:
        mensaje_menu_ver_clientes()
        opcion_input = validar_opcion(1,5)
        match opcion_input:
            case 1:
                do_bubble_sort(lista_clientes, "id", nombre_lista)
            case 2:
                do_bubble_sort(lista_clientes, "apellido", nombre_lista)
            case 3:
                do_bubble_sort(lista_clientes, "ciudad", nombre_lista)
            case 4:
                mostrar_cliente_por_ciudad(lista_clientes)
            case 5:
                run = False

def menu_area_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict], 
                    lista_detalle_ventas: list[dict], usuario: dict):
    """
    menu para area de ventas

    arg:
      matriz_productos (list[list]): productos en matriz
      lista_clientes list[dict]: clientes en diccionario
      lista_ventas (list[dict]): ventas en diccionario
      lista_detalle_ventas (list[dict]):  detalle ventas en diccionario
      usuario (dict): usuario en json
      
    return
    """
    if usuario:
        run = True
        while run:
            mensaje_menu_ventas()
            opcion_input = validar_opcion(1,5)
            match opcion_input:
                case 1:
                    # cargar_venta(lista_detalle_ventas)
                    pass
                case 2:
                    # 2 Modificar Ventas
                    pass
                case 3:
                    menu_ver_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas)
                case 4:
                    borrar_venta(lista_ventas, lista_detalle_ventas)
                case 5:
                    run = False
    else:
        print('Primero tiene que loguear en el sistema')

def menu_modificar_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict], 
                    lista_detalle_ventas: list[dict]):
    """
    menu modificar venta

    arg:
      matriz_productos (list[list]): productos en matriz
      lista_clientes list[dict]: clientes en diccionario
      lista_ventas (list[dict]): ventas en diccionario
      lista_detalle_ventas (list[dict]):  detalle ventas en diccionario

    return
    """

def menu_ver_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict], 
                    lista_detalle_ventas: list[dict]):
    """
    menu ver ventas

    arg:
      matriz_productos (list[list]): productos en matriz
      lista_clientes list[dict]: clientes en diccionario
      lista_ventas (list[dict]): ventas en diccionario
      lista_detalle_ventas (list[dict]):  detalle ventas en diccionario

    return
    """
    run = True
    while run:
        mensaje_menu_ver_ventas()
        opcion_input = validar_opcion(1,3)
        match opcion_input:
            case 1:
                mostrar_info_completa_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas, "id_venta", "DES")
            case 2:
                mostrar_info_completa_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas, "monto_total", "DES")
            case 3:
                run = False

def menu_area_usuarios(lista_usuarios: list[dict], usuario: dict):
    """
    menu para area de usuarios

    arg:
      usuario (dict): usuario en json
      
    return
    """
    if usuario.get("tipo") == "admin":
        run = True
        while run:
            mensaje_menu_usuarios()
            opcion_input = validar_opcion(1,5)
            match opcion_input:
                case 1:
                    crear_usuario(lista_usuarios)
                case 2:
                    editar_usuario(lista_usuarios)
                case 3:
                    mostrar_usuarios(lista_usuarios)
                case 4:
                    borrar_usuario(lista_usuarios)
                case 5:
                    run = False
    else:
        print('usuario no logueado o no permitido')

def menu_area_informes(usuario: dict, lista_detalle_venta: list[dict]):
    """
    menu para area de informes

    arg:
      
      
    return
    """
    if usuario.get("tipo") == "admin":
        run = True
        while run:
            mensaje_menu_informes()
            opcion_input = validar_opcion(1,6)
            match opcion_input:
                case 1:
                    mostrar_producto_mas_vendido(lista_detalle_venta)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    run = False
    else:
        print('usuario no logueado o no permitido')

def manejo_lista(lista) -> list[dict]: 
    """
    nueva etiqueta 

    Args:
        lista (List): lista a manejar

    returns:>
        List: lista manejada
    """
    return lista

def aplicacion():
    """
    funcion principal de la aplicacion

    arg: 

    return:
    """

    productos = leer_csv(ARCHIVO_PRODUCTOS)
    matriz_productos = parsear_dataset_producto_matriz(productos)

    clientes = leer_csv(ARCHIVO_CLIENTES)
    dict_clientes = parsear_dataset_lidict(clientes)
    dict_clientes_parseado = parsear_dict_valor(["id"], [int], dict_clientes)

    ventas = leer_csv(ARCHIVO_VENTAS)
    dict_ventas = parsear_dataset_lidict(ventas)
    dict_ventas_parseado = parsear_dict_valor(["id", "id_cliente"], [int, int], dict_ventas)

    detalle_venta = leer_csv(ARCHIVO_DETALLE_VENTA)
    dict_detalle_venta = parsear_dataset_lidict(detalle_venta)
    dict_detalle_venta_parseado = parsear_dict_valor(
        ["id", "id_venta", "id_producto", "cantidad"], [int, int, int, int], dict_detalle_venta)
    
    lista_usuarios: list[dict] = leer_json(ARCHIVO_USUARIOS)

    usuario = {}
    usuario = {
            "id": 2,
            "username": "otro",
            "password": "1234",
            "tipo": "admin",
            "esta_online": False
        }
    
    run = True
    while run:
        menu = mensaje_menu(usuario)
        menu += mensaje_menu_salir()
        imprimir_menu(menu)
        opcion_input = validar_opcion(0,6)

        match opcion_input:
            case 0:
                if not usuario:
                     usuario = iniciar_sesion(usuario)
                else:
                    print("ya tenes una sesion iniciada")
            case 1:
                menu_area_productos(matriz_productos, usuario)
            case 2:
                menu_area_clientes(dict_clientes_parseado, usuario)
            case 3:
                menu_area_ventas(matriz_productos,\
                                  dict_clientes_parseado, dict_ventas_parseado, dict_detalle_venta_parseado, usuario)
            case 4:
                menu_area_usuarios(lista_usuarios, usuario)
            case 5:
                menu_area_informes(usuario, dict_detalle_venta_parseado)
            case 6:
                run = False
                print("cerrando programa...")

        os.system("pause")
        os.system('cls')
    
