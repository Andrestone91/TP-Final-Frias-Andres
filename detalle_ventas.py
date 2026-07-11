from logica import filtrar_info_dic, obtener_valores_unicos, obtener_list_diccionario_productos, do_bubble_sort,\
         filtrar_por_clave

from ventas import obtener_detalle_ventas_de_una_venta

def obtener_producto_cantidad(lista_detalle_venta: list[dict]) -> list[dict]:
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
    cliente_cantidad: list[dict] = []
    
    for venta in lista_ventas:
        ventas_cliente = filtrar_por_clave(lista_ventas, "id_cliente", venta.get("id_cliente"))
        cantidad = 0
        for id_venta in ventas_cliente:
            detalle_por_cliente = filtrar_por_clave(lista_detalle_venta, "id_venta", id_venta.get("id"))
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
