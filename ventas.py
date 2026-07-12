from logica import do_bubble_sort, mostrar_info_completa, filtrar_info_dic, obtener_valores_unicos,\
      obtener_list_diccionario_productos, filtrar_dato_dict, filtrar_por_id_venta
from validaciones import validar_int, validar_str
from variables import ARCHIVO_VENTAS, ARCHIVO_PRODUCTOS, ARCHIVO_DETALLE_VENTA
from archivos import guardar_dataset_dict_archivo

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

    for indice_ventas in range(len(lista_ventas)):
        if lista_ventas[indice_ventas].get("id") == input_id:
            lista_detalle_venta_filtrado = filtrar_dato_dict(lista_detalle_ventas, filtrar_por_id_venta, input_id)

            for indice_detalle in range(len(lista_detalle_venta_filtrado)):
                producto_encontrado = filtrar_info_dic(dict_productos, "id", lista_detalle_venta_filtrado[indice_detalle].get("id_producto"))
                for producto in dict_productos:
                    if producto_encontrado.get("id") == producto.get("id"):
                        stock_actual = producto.get("stock")
                        cantidad_en_detalle_venta = lista_detalle_venta_filtrado[indice_detalle].get("cantidad")
                        producto.update({"stock": stock_actual + cantidad_en_detalle_venta})
                        break
                    
                for indice in range(len(lista_detalle_ventas)):
                    if lista_detalle_ventas[indice].get("id") == lista_detalle_venta_filtrado[indice_detalle].get("id"):
                        lista_detalle_ventas.pop(indice)
                        break

            lista_ventas.pop(indice_ventas)
            break
    guardar_dataset_dict_archivo(lista_ventas, ARCHIVO_VENTAS)
    guardar_dataset_dict_archivo(dict_productos, ARCHIVO_PRODUCTOS)
    guardar_dataset_dict_archivo(lista_detalle_ventas, ARCHIVO_DETALLE_VENTA)
    mostrar_info_completa(lista_ventas, "ventas")

def cargar_venta(lista_ventas: list[dict], lista_detalle_ventas: list[dict], matriz_productos: list[list],\
                  lista_clientes: list[dict]):
    
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

    venta_seleccionado = filtrar_info_dic(lista_ventas, "id", input_venta_id)
    cliente = filtrar_info_dic(lista_clientes, "id", venta_seleccionado.get("id_cliente"))

    if not cliente:
        print("ERROR: el cliente no existe")
        return

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
    print("el producto fue agregado correctamente\n")
    guardar_dataset_dict_archivo(lista_detalle_ventas, ARCHIVO_DETALLE_VENTA)
    guardar_dataset_dict_archivo(dict_productos, ARCHIVO_PRODUCTOS)
    mostrar_info_completa(lista_detalle_ventas, "detalle_venta")

def modificar_venta(lista_ventas: list[dict], lista_detalle_ventas: list[dict], matriz_productos: list[list],\
                        lista_clientes: list[dict]):
    dict_productos = obtener_list_diccionario_productos(matriz_productos)

    mostrar_info_completa(lista_ventas, "ventas")
    input_venta_id = validar_int("seleccione el ID de la venta para modificar: ")

    venta_seleccionado = filtrar_info_dic(lista_ventas, "id", input_venta_id)
    cliente = filtrar_info_dic(lista_clientes, "id", venta_seleccionado.get("id_cliente"))

    if not cliente:
        print("ERROR: el cliente no existe")
        return

    detalle_venta_encontrados = filtrar_dato_dict(lista_detalle_ventas, filtrar_por_id_venta, input_venta_id)
    productos = []
    for detalle in detalle_venta_encontrados:
        producto = filtrar_info_dic(dict_productos, "id", detalle.get("id_producto"))
        productos.append(producto.get("nombre"))

    mostrar_info_completa(dict_productos, "productos")

    input_nombre_producto = validar_str(f"ingrese el nombre del producto para modificar cantidad ó uno nuevo" + \
                                         f" para agregar {productos}: ")
    producto_filtrado = filtrar_info_dic(dict_productos, "nombre", input_nombre_producto)

    if not producto_filtrado:
        print("no se encontro el producto")
        return
    
    stock = producto_filtrado.get("stock")

    for detalle in detalle_venta_encontrados:
        if detalle.get("id_producto") == producto_filtrado.get("id"):
            print(f"la cantidad actual para {producto_filtrado.get("nombre")} es {detalle.get("cantidad")}")
            nueva_cantidad = validar_int("ingrese la nueva cantidad [0 para borrarla]: ")

            if nueva_cantidad > stock:
                print("cantidad supera el limite disponible")
                return
            
            for producto in dict_productos:
                if producto.get("id") == producto_filtrado.get("id"):
                    stock_anterior = stock + detalle.get("cantidad")
                    producto.update({"stock": stock_anterior - nueva_cantidad})
                    break

            for indice in range(len(lista_detalle_ventas)):
                if lista_detalle_ventas[indice].get("id") == detalle.get("id") and nueva_cantidad > 0:
                    lista_detalle_ventas[indice].update({"cantidad": nueva_cantidad})
                    break

                elif lista_detalle_ventas[indice].get("id") == detalle.get("id"):
                    lista_detalle_ventas.pop(indice)
                    break
            print("se actualizo la venta correctamente\n")
            guardar_dataset_dict_archivo(lista_detalle_ventas, ARCHIVO_DETALLE_VENTA)
            guardar_dataset_dict_archivo(dict_productos, ARCHIVO_PRODUCTOS)
            mostrar_info_completa(lista_detalle_ventas, "detalle_venta")
            return
        
    cantidad = validar_int(f"se agrega {producto_filtrado.get("nombre")}, ingresa la cantidad: ")
    ids_detalle = obtener_valores_unicos(lista_detalle_ventas, "id")
    ids_detalle.reverse()
    ultimo_id = ids_detalle[0]
    nuevo_id = ultimo_id + 1

    if cantidad > stock:
        print("cantidad supera el limite disponible")
        return
    
    for producto in dict_productos:
        if producto.get("id") == producto_filtrado.get("id"):
            producto.update({"stock": stock - cantidad})
            break

    lista_detalle_ventas.append({
        "id": nuevo_id,
        "id_venta": input_venta_id,
        "id_producto": producto_filtrado.get("id"),
        "cantidad": cantidad
    })
    print("se actualizo la venta correctamente\n")
    guardar_dataset_dict_archivo(lista_detalle_ventas, ARCHIVO_DETALLE_VENTA)
    guardar_dataset_dict_archivo(dict_productos, ARCHIVO_PRODUCTOS)
    mostrar_info_completa(lista_detalle_ventas, "detalle_venta")       

