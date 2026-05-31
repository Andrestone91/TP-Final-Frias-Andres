from validaciones import validar_opcion
import os
from mensajes import mensaje_menu_principal, mensaje_menu_area_productos, mensaje_menu_productos
from logica import cargar_producto, modificar_producto

def menu_area_productos(matriz_productos: list[list]):
    """
    menu para area de productos

    arg: 
        
    return
    """
    run = True

    while run:
        mensaje_menu_area_productos()
        opcion_input = validar_opcion(1,6)

        match opcion_input:
            case 1:
                cargar_producto(matriz_productos)
            case 2:
                modificar_producto(matriz_productos)
            case 3:
                menu_productos()
            case 4:
                pass
            case 5:
                run = False
            case 6:
                print(matriz_productos)

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

def aplicacion(matriz_productos:list[list]):
    """
    funcion principal de la aplicacion

    arg: 
        matriz_productos (list[list]): la matriz de productos
        
    return:

    """

    run = True

    while run:
        mensaje_menu_principal()
        opcion_input = validar_opcion(1,3)

        match opcion_input:
            case 1:
                menu_area_productos(matriz_productos)
            case 2:
                print("opcion no disponible")
            case 3:
                run = False
                print("cerrando programa...")

        os.system("pause")
        os.system('cls')
    
