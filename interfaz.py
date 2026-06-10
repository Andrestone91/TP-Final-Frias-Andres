from validaciones import validar_opcion
import os
from mensajes import mensaje_menu_principal, mensaje_menu_area_productos, mensaje_menu_productos,\
      mensaje_menu_clientes, mensaje_menu_ver_clientes
from logica import cargar_producto, modificar_producto, producto_a_borrar, cargar_cliente,\
      modificar_cliente, borrar_cliente, do_bubble_sort

def menu_area_productos(matriz_productos: list[list]):
    """
    menu para area de productos

    arg: 
        
    return
    """
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

def menu_area_clientes(lista_clientes: list[dict]):
    """
    menu para area de clientes

    arg:
      lista_clientes (list[dict]): lista de clientes

    return
    """
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

def menu_ver_clientes(lista_clientes: list[dict]):
    """
    menu ver clientes

    arg:
      lista_clientes (list[dict]): lista de clientes

    return
    """
    run = True

    while run:
        mensaje_menu_ver_clientes()
        opcion_input = validar_opcion(1,5)
        match opcion_input:
            case 1:
                do_bubble_sort(lista_clientes, "id")
            case 2:
                do_bubble_sort(lista_clientes, "apellido")
            case 3:
                do_bubble_sort(lista_clientes, "ciudad")
            case 4:
                do_bubble_sort(lista_clientes, "apellido")
            case 5:
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

def aplicacion(matriz_productos:list[list], lista_clientes: list[dict]):
    """
    funcion principal de la aplicacion

    arg: 
        matriz_productos (list[list]): la matriz de productos
        
    return:

    """
    lista_clientes_aux = manejo_lista(lista_clientes)

    run = True

    while run:
        mensaje_menu_principal()
        opcion_input = validar_opcion(1,3)

        match opcion_input:
            case 1:
                menu_area_productos(matriz_productos)
            case 2:
                menu_area_clientes(lista_clientes_aux)
            case 3:
                run = False
                print("cerrando programa...")

        os.system("pause")
        os.system('cls')
    
