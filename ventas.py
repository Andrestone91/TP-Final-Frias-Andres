from validaciones import validar_int

def cargar_venta(lista_detalle_ventas: list[dict]):
    lista_detalle_ventas = obtener_detalle_ventas_de_una_venta(lista_detalle_ventas)
    print(lista_detalle_ventas)
    
def obtener_detalle_ventas_de_una_venta(lista_detalle_ventas: list[dict]) -> list[dict]:
    detalle_ventas = []

    input_id = validar_int("ingresa el ID de una venta: ")

    for detalle in lista_detalle_ventas:
        if detalle.get("id_venta") == input_id:
            detalle_ventas.append(detalle)
    return detalle_ventas