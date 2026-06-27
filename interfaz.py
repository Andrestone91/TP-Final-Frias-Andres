import os
from validaciones import validar_opcion
from mensajes import mensaje_menu_principal, mensaje_menu_area_productos, mensaje_menu_productos,\
      mensaje_menu_clientes, mensaje_menu_ver_clientes, mensaje_menu_ventas, mensaje_menu_ver_ventas, mensaje_menu, imprimir_menu,\
          mensaje_menu_salir
from logica import cargar_producto, modificar_producto, producto_a_borrar,\
      do_bubble_sort
from clientes import cargar_cliente, modificar_cliente, borrar_cliente
from ventas import cargar_venta, mostrar_info_completa_ventas
from login import iniciar_sesion

def menu_area_productos(matriz_productos: list[list], usuario: dict):
    """
    menu para area de productos

    arg: 
        
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
                    menu_productos()
                case 4:
                    producto_a_borrar(matriz_productos)
                case 5:
                    run = False
    else:
        print('Primero tiene que loguear en el sistema')


def menu_productos():
    """
    menu para ver productos

    arg: 
        
    return
    """
    run = True

    while run:
        mensaje_menu_productos()
        opcion_input = validar_opcion(1,4)

        match opcion_input:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                run = False

def menu_area_clientes(lista_clientes: list[dict], usuario: dict):
    """
    menu para area de clientes

    arg:
      lista_clientes (list[dict]): lista de clientes

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
                do_bubble_sort(lista_clientes, "apellido", nombre_lista)
            case 5:
                run = False

def menu_area_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict], 
                    lista_detalle_ventas: list[dict], usuario: dict):
    """
    menu para area de ventas

    arg:
      lista_ventas (list[dict]): lista de ventas

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
                    pass
                case 3:
                    menu_ver_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas)
                case 4:
                    pass
                case 5:
                    run = False
    else:
        print('Primero tiene que loguear en el sistema')

def menu_ver_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict], 
                    lista_detalle_ventas: list[dict]):
    """
    menu ver ventas

    arg:
      lista_detalle_ventas (list[dict]): lista de detalle ventas

    return
    """
    run = True
    nombre_lista = "ventas"
    while run:
        mensaje_menu_ver_ventas()
        opcion_input = validar_opcion(1,3)
        match opcion_input:
            case 1:
                mostrar_info_completa_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas)
            case 2:
                pass
            case 3:
                run = False

def manejo_lista(lista) -> list[dict]: 
    """
    nueva etiqueta 

    Args:
        lista (List): lista a manejar

    returns:>
        List: lista manejada
    """
    return lista

def aplicacion(matriz_productos:list[list], lista_clientes: list[dict], lista_ventas: list[dict], lista_detalle_ventas: list[dict]):
    """
    funcion principal de la aplicacion

    arg: 
        matriz_productos (list[list]): matriz de productos
        lista_clientes (list[dict]): lista de clientes
        lista_ventas (list[dict]): lista de ventas
        lista_detalle_ventas (list[dict]): lista detalle de venta

    return:
            
    """
    lista_clientes_aux = manejo_lista(lista_clientes)

    usuario = {}
    # usuario = {
    #     "id": 1,
    #     "username": "andre",
    #     "password": "1234",
    #     "tipo": "vendedor",
    #     "esta_online": True
    # }
    
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
                menu_area_clientes(lista_clientes_aux, usuario)
            case 3:
                menu_area_ventas(matriz_productos, lista_clientes, lista_ventas, lista_detalle_ventas, usuario)
            case 4:
                pass
            case 5:
                pass
            case 6:
                run = False
                print("cerrando programa...")

        os.system("pause")
        os.system('cls')
    
