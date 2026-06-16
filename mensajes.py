def mensaje_menu_principal():
    """
    muestra las opciones disponibles del menu principal

    arg: 
        
    return:
    """
    
    mensaje =\
    """
        MENU PRINCIPAL

        1. Área Productos 
        2. Área Clientes
        3. Área Ventas
        4. Salir del Sistema
    """
    print(mensaje)

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

def mensaje_menu_productos():
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
         	
        1 Cargar Ventas (permitir agregar productos a la venta) 
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