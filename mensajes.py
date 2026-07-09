def mensaje_menu_principal(usuario: dict):
    """
    muestra las opciones disponibles del menu principal

    arg: 
        
    return:
    """

    mensaje ='1. Área Productos'\
    """
    2. Área Clientes
    3. Área Ventas
    """
    if usuario.get("tipo") == "admin":
        mensaje += '4. Área Usuarios'\
    """
    5. Área Informes
    """
    return mensaje

def mensaje_menu_area_productos():
    """
    muestra las opciones disponibles del menu area productos

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU AREA PRODUCTOS

    1 Cargar Producto 
    2 Modificar Producto 
    3 Ver Productos 
    4 Borrar Producto 
    5 Salir (Vuelve al Menú Principal)
    """
    print(mensaje)

def mensaje_menu_ver_productos():
    """
    muestra las opciones disponibles del menu ver productos

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU VER PRODUCTOS

    1 Ordenar por ID ASC 
    2 Ordenar por Stock ASC 
    3 Ordenar por nombre ASC
    4 Volver
    """
    print(mensaje)

def mensaje_menu_clientes():
    """
    muestra las opciones disponibles del menu area clientes

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU AREA CLIENTES
     	
    1 Cargar Cliente 
    2 Modificar Cliente 
    3 Ver CLientes
    4 Borrar Cliente 
    5 Salir (Vuelve al Menú Principal)
    """
    print(mensaje)

def mensaje_menu_ver_clientes():
    """
    muestra las opciones disponibles para ver clientes

    arg: 
        
    return:
    
    """
    mensaje =\
    """
    MENU AREA CLIENTES
    1 Ordenar por ID ASC 
    2 Ordenar por Apellido ASC 
    3 Ordenar por Ciudad ASC 
    4 Filtrar por Ciudad (y ordenar por Apellido ASC)
    5 volver
    """
    print(mensaje)

def mensaje_menu_ventas():
    """
    muestra las opciones disponibles del menu area Ventas

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU AREA VENTAS
     	
    1 Cargar Ventas
    2 Modificar Venta 
    3 Ver Ventas
    4 Borrar Venta 
    5 Salir (Vuelve al Menú Principal)
    """
    print(mensaje)

def mensaje_menu_ver_ventas():
    """
    muestra las opciones disponibles para ver ventas

    arg: 
        
    return:
    
    """
    mensaje =\
    """
    MENU VER VENTAS

    1 Ordenar por ID DES 
    2 Ordenar por monto DES
    3 Volver (area ventas)
    """
    print(mensaje)

def mensaje_menu_usuarios():
    """
    muestra las opciones disponibles del menu area usuarios

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU AREA USUARIOS
     	
    1 Crear usuario 
    2 Modificar Usuarios 
    3 Ver Usuarios 
    4 Borrar Usuarios 
    5 Salir 
    """
    print(mensaje)

def mensaje_menu_informes():
    """
    muestra las opciones disponibles del menu area informes

    arg: 
        
    return:
    """
    
    mensaje =\
    """
    MENU AREA INFORMES
     	
    1 Mostrar producto más vendido y la cantidad 
    2 Mostrar producto menos vendido y la cantidad 
    3 Mostrar cliente con más compras hechas 
    4 Mostrar monto total de ventas
    5 Mostrar cantidad de productos vendidos
    6 Salir 
    """
    print(mensaje)

def mensaje_menu(usuario: dict):
    """
    muestra las opciones disponibles para ver ventas

    arg: 
        
    return:
    
    """
    mensaje =\
    """
    MENU PRINCIPAL

    0. login
    """
    if usuario:
        mensaje += mensaje_menu_principal(usuario)
    return mensaje

def mensaje_menu_salir() -> str:
    """
    muestra menu salir

    arg: 
        
    return:
    
    """
    mensaje = '6. Salir del sistema\n'

    return mensaje

def imprimir_menu(menu: str):
    print(menu)