def crear_matriz(filas: int) -> list[list]:
    matriz = []

    for fila in range(filas):
        matriz.append([])

    return matriz

def obtener_ids(matriz_productos: list[list]) -> list:
    lista_ids = []

    cantidad_filas = len(matriz_productos)

    for fila in range(cantidad_filas):
        lista_ids.append(matriz_productos[fila][0])
    
    return lista_ids

def mostrar_info_completa(lista_dict: list[dict], nombre_lista: str):
    """
    muestra la inforamcion completa de una lista de diccionario

    arg: 
        lista_dict (list[dict]): contiene la lista en formato de diccionario.
        
    return:
        None
    """
    info = ''

    if nombre_lista == "clientes":

        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            apellido = lista_dict[fila].get("apellido")
            nombre = lista_dict[fila].get("nombre")
            ciudad = lista_dict[fila].get("ciudad")

            info += f'{id},{apellido},{nombre},{ciudad}' + "\n"

        print(info)

    elif nombre_lista == "lista_detalle_final":
        for fila in range(len(lista_dict)):
            id_venta = lista_dict[fila].get("id_venta")
            id_cliente = lista_dict[fila].get("id_cliente")
            apellido = lista_dict[fila].get("apellido")
            nombre = lista_dict[fila].get("nombre")
            monto_total = lista_dict[fila].get("monto_total")

            info += f"{id_venta},{id_cliente},{apellido},{nombre},{monto_total}\n"

        print(info)

    elif nombre_lista == "ventas":
        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            id_cliente = lista_dict[fila].get("id_cliente")

            info += f"{id},{id_cliente}\n"

        print(info)

    elif nombre_lista == "usuarios":
        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            username = lista_dict[fila].get("username")
            password = lista_dict[fila].get("password")
            tipo = lista_dict[fila].get("tipo")
            esta_online = lista_dict[fila].get("esta_online")

            info += f"{id},{username},{password},{tipo},{esta_online}\n"

        print(info)

    elif nombre_lista == "productos":
        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            nombre = lista_dict[fila].get("nombre")
            stock = lista_dict[fila].get("stock")
            precio = lista_dict[fila].get("precio")

            info += f"{id},{nombre},{stock},{precio}\n"

        print(info)

    elif nombre_lista == "detalle_venta":
        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            id_venta = lista_dict[fila].get("id_venta")
            id_producto = lista_dict[fila].get("id_producto")
            cantidad = lista_dict[fila].get("cantidad")

            info += f"{id},{id_venta},{id_producto},{cantidad}\n"

        print(info)

    else:
        print("lista no reconocida")

def mostrar_info_completa_matriz(matriz: list[list]):
    info = ''
    for fila in matriz:
        id = fila[0]
        nombre = fila[1]
        inventario = fila[2]
        precio = fila[3]

        info += f'{id},{nombre},{inventario},{precio}' + "\n"

    print(info)

def do_bubble_sort(lista_dict: list[dict], tipo: str, nombre_lista: str, ord: str= 'ASC'):
    """
    tipo de ordenamiento bubble sort.

    arg: 
        list_dict (list[dict]): contiene la lista de diccionario a ordenar.

    return
        None
    """
    tamanio_lista = len(lista_dict)

    for vueltas in range(tamanio_lista):

        for primer_elemento in range(0, tamanio_lista - vueltas - 1):

            siguiente_elemento = primer_elemento + 1

            diccionario_pe = lista_dict[primer_elemento]
            diccionario_se = lista_dict[siguiente_elemento]

            if diccionario_pe.get(tipo) > diccionario_se.get(tipo) and ord == 'ASC' or\
                diccionario_pe.get(tipo) < diccionario_se.get(tipo) and ord == 'DES':

                lista_dict[primer_elemento], lista_dict[siguiente_elemento] =\
                lista_dict[siguiente_elemento],  lista_dict[primer_elemento]
    mostrar_info_completa(lista_dict,  nombre_lista)

# def do_bubble_sort_matriz(matriz: list[list], indice: str, ord: str= 'ASC'):
#     """
#     tipo de ordenamiento bubble sort.

#     arg: 
#         list_dict (list[dict]): contiene la lista de diccionario a ordenar.

#     return
#         None
#     """
#     tamanio_lista = len(matriz)

#     for vueltas in range(tamanio_lista):

#         for primer_elemento in range(0, tamanio_lista - vueltas - 1):

#             siguiente_elemento = primer_elemento + 1

#             if matriz[primer_elemento][indice] > matriz[siguiente_elemento][indice] and ord == 'ASC' or\
#                 matriz[primer_elemento][indice] < matriz[siguiente_elemento][indice] and ord == 'DES':

#                matriz[primer_elemento], matriz[siguiente_elemento] =\
#                 matriz[siguiente_elemento], matriz[primer_elemento]

#     mostrar_info_completa_matriz(matriz)

def convertir_valor(valor, tipo: str):
    if tipo == "int":
        return parsear_str_a_int(valor)
    if tipo == "float":
        return parsear_str_a_float(valor)
    return valor

def parsear_dict_valor(lista_keys: list, lista_tipos: list, dict_lista:list[dict]):
    for dict_ele in dict_lista:
        for key, tipo in zip(lista_keys, lista_tipos):
            if key in dict_ele:
                dict_ele[key] = tipo(dict_ele[key])

    return dict_lista
    
def parsear_dataset_lidict(datos: list[str]) -> list[dict]:
    str_claves_limpias = datos.pop(0).replace('\n', '')
    claves = split_texto(str_claves_limpias, ',')
    lista_dict = []

    for item in datos:
        item = item.replace('\n', '')
        datos = split_texto(item, ',')
        item_dict = {}

        for indice_clave in range(len(claves)):
            item_dict.update(
                {claves[indice_clave] : datos[indice_clave]}
            )
        lista_dict.append(item_dict)
    return lista_dict

def split_texto(texto: str, separador: str) -> list[str]:
    lista_str = []
    palabra = ''

    for caracter in texto:
        if caracter != separador:
            palabra += caracter
        else:
            if agregar_si_no_vacio(lista_str, palabra):
                palabra = ''
    
    agregar_si_no_vacio(lista_str, palabra)
    return lista_str

def agregar_si_no_vacio(lista_palabras: list[str], palabra: str) -> bool:
    hubo_cambio = False
    if palabra != '':
        lista_palabras.append(palabra)
        hubo_cambio = True
    return hubo_cambio

def parsear_dataset_producto_matriz(datos: list[str]) -> list[list]:
    mi_matriz = []
    for linea in datos:
        if datos.index(linea) == 0:
            continue
        linea = linea.replace('\n', '')
        datos_linea = split_texto(linea, ',')

        datos_linea[0] = parsear_str_a_int(datos_linea[0]) 
        datos_linea[2] = parsear_str_a_int(datos_linea[2]) 
        datos_linea[3] = parsear_str_a_float(datos_linea[3]) 
        
        mi_matriz.append(datos_linea)
    return mi_matriz

def parsear_str_a_int(texto: str) -> int:
    numero = int(texto)
    return numero

def parsear_str_a_float(texto: str) -> float:
    valor = float(texto)
    return valor

def filtrar_info_dic(lista: list[dict], clave: str, valor: int):
    item_dicccionario = {}
    for item in lista:
        if item.get(clave) == valor:
            item_dicccionario.update(item)
            break

    return item_dicccionario

def filtrar_por_clave(datos: list[dict], clave: str, valor: int) -> list[dict]:
    filtrados = []

    for dato in datos:
        if dato.get(clave) == valor:
            filtrados.append(dato)
    return filtrados

def obtener_valores_unicos(lista: list[dict], clave: str) -> list:
    ids_set = set()

    for item in lista:
        ids_set.add(item.get(clave))
    
    lista_ids_unicos = list(ids_set)

    return lista_ids_unicos

def obtener_ids_dict(lista_dict: list[dict], clave: str) -> list:
    lista_ids = []

    for item in lista_dict:
        lista_ids.append(item.get(clave))
    
    return lista_ids

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