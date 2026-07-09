from logica import do_bubble_sort, mostrar_info_completa, filtrar_info_dic, obtener_valores_unicos,\
      obtener_list_diccionario_productos, filtrar_por_clave, obtener_ids_dict
from validaciones import validar_int

def obtener_detalle_ventas_de_una_venta(lista_detalle_ventas: list[dict], id: int, clave: str) -> list[dict]:
    detalle_ventas = []

    for detalle in lista_detalle_ventas:
        if detalle.get(clave) == id:
            detalle_ventas.append(detalle)
    return detalle_ventas

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

def mostrar_info_completa_ventas(matriz_productos: list[list], lista_clientes: list[dict], lista_ventas: list[dict],
                                 lista_detalle_ventas: list[dict], clave: str, ord: str):
    
    dict_productos = obtener_list_diccionario_productos(matriz_productos)

    lista_ids_unicos_detalle_ventas = obtener_valores_unicos(lista_detalle_ventas, "id_venta")
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

    do_bubble_sort(lista_detalle_final, clave, "lista_detalle_final", ord)
        
def borrar_venta(lista_ventas: list[dict], lista_detalle_ventas: list[dict], matriz_productos: list[list]):
    """
    borra una venta

    arg: 
        lista_clientes (list[dict]): contiene la lista clientes en formato diccionario.
        lista_detalle_ventas (list[dict]): contiene la lista detalle de venta en formato diccionario
        
    return:
    """
    dict_productos = obtener_list_diccionario_productos(matriz_productos)
    mostrar_info_completa(lista_ventas, "ventas")
    input_id = validar_int("ingrese el numero id a borrar: ")

    for fila_venta in range(len(lista_ventas)):
        if lista_ventas[fila_venta].get("id") == input_id:
            lista_detalle_venta = obtener_detalle_ventas_de_una_venta(lista_detalle_ventas, input_id, "id_venta")

            for fila_detalle in lista_detalle_venta:
                producto = filtrar_info_dic(dict_productos, "id", fila_detalle.get("id_producto"))
                producto.update({"inventario": producto.get("stock") + fila_detalle.get("cantidad")})
                lista_detalle_venta.pop({"id": fila_detalle.get("id")})
                print(lista_detalle_venta)
                # lista_detalle_venta.pop(fila_detalle)
            print(lista_ventas[fila_venta])
            # lista_ventas.pop(fila_venta)
            print("venta borrada:")
            break
        
    # mostrar_info_completa(lista_ventas, "ventas")

def cargar_venta(lista_ventas: list[dict], lista_detalle_ventas: list[dict], matriz_productos: list[list]):
    dict_productos = obtener_list_diccionario_productos(matriz_productos)

    mostrar_info_completa(lista_ventas, "ventas")
    input_venta_id = validar_int("seleccione el ID de la venta para cargar un producto: ")
    ids_ventas = obtener_valores_unicos(lista_ventas, "id")

    for id in ids_ventas:
        if input_venta_id not in ids_ventas:
            print("la venta no existe")
            return

    mostrar_info_completa(dict_productos, "productos")
    input_id_producto = validar_int("ingrese el ID del producto: ")
    ids_productos = obtener_valores_unicos(dict_productos, "id")

    for id in ids_productos:
        if input_id_producto not in ids_productos:
            print("el producto no existe")
            return
    
    producto_seleccionado = filtrar_info_dic(dict_productos, "id", input_id_producto)

    input_cantidad = validar_int("cantidad del producto: ")

    stock = producto_seleccionado.get("stock")
    if input_cantidad > stock:
        print("cantidad supera el limite disponible")
        return
    
    for producto in dict_productos:
        if producto.get("id") == input_id_producto:
            producto.update({"stock": stock - input_cantidad})
            break

    ids_detalle_ventas = obtener_valores_unicos(lista_detalle_ventas, "id")

    ids_detalle_ventas.reverse()

    ultimo_id = ids_detalle_ventas[0]

    nuevo_id =  ultimo_id + 1

    lista_detalle_ventas.append({
        "id": nuevo_id,
        "id_venta": input_venta_id,
        "id_producto": input_id_producto,
        "cantidad": input_cantidad
    })
    mostrar_info_completa(dict_productos, "productos")
    mostrar_info_completa(lista_detalle_ventas, "detalle_venta")
