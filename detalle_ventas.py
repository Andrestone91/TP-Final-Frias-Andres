from logica import filtrar_info_dic, obtener_ids_unicos
from ventas import obtener_detalle_ventas_de_una_venta

def mostrar_producto_mas_vendido(lista_detalle_venta: list[dict]):
    producto_cantidad = []
    lista_ids_productos_unicos_detalle_ventas = obtener_ids_unicos(lista_detalle_venta, "id_producto")
    for id_producto in lista_ids_productos_unicos_detalle_ventas:
   
        producto_filtrado = obtener_detalle_ventas_de_una_venta(lista_detalle_venta, id_producto, "id_producto")
        print(producto_filtrado)