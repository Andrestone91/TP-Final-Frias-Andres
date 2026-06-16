from logica import do_bubble_sort
# id_venta,id_cliente,apellido,nombre,monto_venta

# Id_venta: debe extraerse del dataset detalle_venta 

# Id_cliente: debe extraerse del dataset ventas (donde coincida el ID de la venta) 

# apellido y nombre: debe extraerse del dataset clientes (segun su ID) 

# monto_venta: debe extraerse de la suma de cantidad de productos * precio unitario 
# (para esto, la cantidad de productos se obtendra desde el dataset detalle_venta y el precio unitario del dataset productos, 
# donde coincidan sus ids) 

def cargar_venta(lista_detalle_ventas: list[dict]):
    lista_detalle_ventas = obtener_detalle_ventas_de_una_venta(lista_detalle_ventas)
    print(lista_detalle_ventas)
    
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

def filtrar_info_dic(lista: list[dict], clave: str, id: int):
    item_dicccionario = {}
    for item in lista:
        if item.get(clave) == id:
            item_dicccionario.update(item)
            break

    return item_dicccionario

def armar_dic(venta: dict, cliente: dict, id_venta):
    info = f"{id_venta},{venta.get("id_cliente")},{cliente.get("apellido")},{cliente.get("nombre")}" + "\n"
    return info

def mostrar_info_completa_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict],
                                 lista_detalle_ventas: list[dict]):
    
    lista_ids_unicos_detalle_ventas = obtener_ids_unicos(lista_detalle_ventas, "id_venta")

    info = ""
    for id_venta in lista_ids_unicos_detalle_ventas:
        venta = filtrar_info_dic(lista_ventas, "id", id_venta)
        cliente = filtrar_info_dic(lista_clientes, "id", venta.get("id_cliente"))
        # detalle_venta = obtener_detalle_ventas_de_una_venta(lista_detalle_ventas, id_venta)
        # lista_detalle_final_ord = []
        # do_bubble_sort(lista_detalle_final_ord, "id", "lista_detalle_final_ord", "DEC")
        detalle_venta_final = armar_dic(venta, cliente, id_venta)
        info += detalle_venta_final
    print(info)
        
