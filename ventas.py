from logica import do_bubble_sort, mostrar_info_completa, filtrar_info_dic
from validaciones import validar_int

def cargar_venta(lista_detalle_ventas: list[dict]):
    pass

def obtener_detalle_ventas_de_una_venta(lista_detalle_ventas: list[dict], id: int) -> list[dict]:
    detalle_ventas = []

    for detalle in lista_detalle_ventas:
        if detalle.get("id_venta") == id:
            detalle_ventas.append(detalle)
    return detalle_ventas

def obtener_ids_unicos(lista: list[dict], clave: str) -> list:
    ids_set = set()

    for item in lista:
        ids_set.add(item.get(clave))
    
    lista_ids_unicos = list(ids_set)

    return lista_ids_unicos

def obtener_list_diccionario_productos(matriz_producto: list[list]) -> list[dict]:
    lista_productos = []

    for producto in matriz_producto:
        lista_productos.append({
            "id": producto[0],
            "nombre": producto[1],
            "stock": producto[2],
            "precio": producto[3],
        })

    return lista_productos

def obtener_precio(id_producto: int, lista_dict_productos: list[dict]) -> float:
    precio = 0
    for producto in lista_dict_productos:
        if producto.get("id") == id_producto:
            precio = producto.get("precio")
    return precio

def obtener_monto_total(id_venta: int, lista_detalle_ventas: list[dict], lista_dict_productos: list[dict]) -> float:
    total = 0
    for detalle in lista_detalle_ventas:
        if detalle.get("id_venta") == id_venta:
            precio = obtener_precio(detalle.get("id_producto"), lista_dict_productos)
            total += detalle.get("cantidad") * precio

    return total
    
def armar_dic(venta: dict, cliente: dict, id_venta, monto_total: float):
    info = f"{id_venta},{venta.get('id_cliente')},{cliente.get('apellido')},{cliente.get('nombre')},{monto_total}\n"
    return info

def mostrar_info_completa_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict],
                                 lista_detalle_ventas: list[dict]):
    
    dict_productos = obtener_list_diccionario_productos(matriz_productos)

    lista_ids_unicos_detalle_ventas = obtener_ids_unicos(lista_detalle_ventas, "id_venta")
    lista_detalle_final: list[dict] = []

    for id_venta in lista_ids_unicos_detalle_ventas:
        venta = filtrar_info_dic(lista_ventas, "id", id_venta)
        cliente = filtrar_info_dic(lista_clientes, "id", venta.get("id_cliente"))
        
        monto_total = obtener_monto_total(id_venta, lista_detalle_ventas, dict_productos)

        lista_detalle_final.append({
            "id_venta": id_venta,
            "id_cliente": venta.get("id_cliente"),
            "apellido": cliente.get("apellido"),
            "nombre":cliente.get("nombre"),
            "monto_total": monto_total
        })

    do_bubble_sort(lista_detalle_final, "id_venta", "lista_detalle_final", "DES")
        
def borrar_venta(lista_ventas: list[dict], lista_detalle_ventas: list[dict]):
    """
    borra una venta

    arg: 
        lista_clientes (list[dict]): contiene la lista clientes en formato diccionario.
        lista_detalle_ventas (list[dict]): contiene la lista detalle de venta en formato diccionario
        
    return:
    """
    mostrar_info_completa(lista_ventas, "ventas")
    input_id = validar_int("ingrese el numero id a borrar: ")

    for fila_venta in range(len(lista_ventas)):
        if lista_ventas[fila_venta].get("id") == input_id:
            lista_detalle_venta = obtener_detalle_ventas_de_una_venta(lista_detalle_ventas, input_id)

            for fila_detalle in lista_detalle_venta:
                print(fila_detalle)
                # lista_detalle_venta.pop(fila_detalle)
            print(lista_ventas[fila_venta])
            # lista_ventas.pop(fila_venta)
            print("venta borrada:")
            break
        
    # mostrar_info_completa(lista_ventas, "ventas")