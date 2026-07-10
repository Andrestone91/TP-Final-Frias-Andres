from logica import filtrar_info_dic, obtener_valores_unicos, obtener_list_diccionario_productos, do_bubble_sort
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