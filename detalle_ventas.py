from logica import filtrar_info_dic, obtener_valores_unicos, obtener_list_diccionario_productos, do_bubble_sort,\
          filtrar_dato_dict, filtrar_por_id, filtrar_por_id_venta

from ventas import obtener_detalle_ventas_de_una_venta

def obtener_producto_cantidad(lista_detalle_venta: list[dict]) -> list[dict]:
    """
    obtiene la cantidad de cada producto vendido

    arg: 
        lista_detalle_venta (list[dict]): contiene la lista de detalle de ventas en formato de diccionario.
        
    return:
        producto_cantidad: lista de diccionarios con id_producto y cantidad vendida
    """
    producto_cantidad: list[dict] = []
    lista_ids_productos_unicos_detalle_ventas = obtener_valores_unicos(lista_detalle_venta, "id_producto")
    for id_producto in lista_ids_productos_unicos_detalle_ventas:
   
        detalle_filtrado = obtener_detalle_ventas_de_una_venta(lista_detalle_venta, id_producto, "id_producto")
        cantidad = 0
        for indice in range(len(detalle_filtrado)):
            cantidad += detalle_filtrado[indice].get("cantidad")
        
        producto_cantidad.append({
            "id_producto": detalle_filtrado[0].get("id_producto"),
            "cantidad": cantidad
        })
    return producto_cantidad

def mostrar_productos_cantidad_ventas(lista_detalle_venta: list[dict], matriz_productos: list[list], info: str, ord: str):
    """
    muestra los productos con su cantidad vendida

    arg: 
        lista_detalle_venta (list[dict]): contiene la lista de detalle de ventas en formato de diccionario.
        matriz_productos (list[list]): contiene la matriz de productos.
        info (str): información adicional para mostrar.
        ord (str): criterio de ordenamiento.

    return:
    """

    dict_productos = obtener_list_diccionario_productos(matriz_productos)
    lista_producto_cantidad = obtener_producto_cantidad(lista_detalle_venta)
    do_bubble_sort(lista_producto_cantidad, "cantidad", "ninguno", ord)
    producto_encontrado = filtrar_info_dic(dict_productos, "id", lista_producto_cantidad[0].get("id_producto"))

    mensaje = \
    f"""
    el producto {info} vendido es:
    id: {lista_producto_cantidad[0].get("id_producto")}
    nombre: {producto_encontrado.get("nombre")}
    cantidad: {lista_producto_cantidad[0].get("cantidad")}
    """
    print(mensaje)

def mostrar_cliente_con_mas_compras(lista_clientes: list[dict], lista_detalle_venta: list[dict], lista_ventas: list[dict]):
    """
    muestra el cliente que realizó más compras

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        lista_detalle_venta (list[dict]): contiene la lista de detalle de ventas en formato de diccionario.
        lista_ventas (list[dict]): contiene la lista de ventas en formato de diccionario.

    return:
    """
    cliente_cantidad: list[dict] = []

    for venta in lista_ventas:
        ventas_cliente = filtrar_dato_dict(lista_ventas, filtrar_por_id, venta.get("id_cliente"))
        cantidad = 0
        for id_venta in ventas_cliente:
            detalle_por_cliente = filtrar_dato_dict(lista_detalle_venta, filtrar_por_id_venta, id_venta.get("id"))
            for indice_detalle in range(len(detalle_por_cliente)):
                cantidad += detalle_por_cliente[indice_detalle].get("cantidad")
        cliente_cantidad.append({
            "id_cliente": id_venta.get("id_cliente"),
            "cantidad": cantidad
        })

    do_bubble_sort(cliente_cantidad, "cantidad", "ninguno", "DES")

    cliente = filtrar_info_dic(lista_clientes, "id", cliente_cantidad[0].get("id_cliente"))

    mensaje = \
    f"""
    cliente que mas compras realizo:
    id: {cliente.get("id")}
    apellido: {cliente.get("apellido")}
    nombre: {cliente.get("nombre")}
    cantidad de compras: {cliente_cantidad[0].get("cantidad")}
    """
    print(mensaje)

def mostrar_monto_total_ventas(lista_detalle_venta: list[dict], matriz_productos: list[list]):
    """
    muestra el monto total de ventas

    arg: 
        lista_detalle_venta (list[dict]): contiene la lista de detalle de ventas en formato de diccionario.
        matriz_productos (list[list]): contiene la matriz de productos.

    return:
    """
    dict_productos = obtener_list_diccionario_productos(matriz_productos)

    monto_total = 0
    for detalle in lista_detalle_venta:
        producto = filtrar_dato_dict(dict_productos, filtrar_por_id, detalle.get("id_producto"))
        cantidad = detalle.get("cantidad")
        monto = producto[0].get("precio") * cantidad
        monto_total += monto

    mensaje =\
    f"""
    monto total de ventas:
    $ {monto_total}
    """
    print(mensaje)

def mostrar_cantidad_productos_vendidos(lista_detalle_venta: list[dict]):
    """
    muestra la cantidad total de productos vendidos

    arg: 
        lista_detalle_venta (list[dict]): contiene la lista de detalle de ventas en formato de diccionario.

    return:
    """
    productos_vendidos_total = 0
    for detalle in lista_detalle_venta:
        cantidad = detalle.get("cantidad")
        productos_vendidos_total += cantidad

    mensaje =\
    f"""
    cantidad de productos vendidos: {productos_vendidos_total}
    """
    print(mensaje)
