def crear_matriz(filas: int) -> list[list]:
    """
    crea una matriz vacía con la cantidad de filas especificada

    arg: 
        filas (int): cantidad de filas para la matriz
        
    return:
        list[list]: matriz vacía
    """ 
    matriz = []

    for fila in range(filas):
        matriz.append([])

    return matriz

def obtener_ids(matriz_productos: list[list]) -> list:
    """
    obtiene los IDs de los productos en la matriz

    arg: 
        matriz_productos (list[list]): contiene la matriz de productos.
        
    return:
        lista_ids: lista de id de productos
    """
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
        nombre_lista (str): nombre de la lista para mostrar la información correspondiente.
        
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
            activo = lista_dict[fila].get("activo")

            info += f'{id},{apellido},{nombre},{ciudad},{activo}' + "\n"

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
            activo = lista_dict[fila].get("activo")

            info += f"{id},{nombre},{stock},{precio},{activo}\n"

        print(info)

    elif nombre_lista == "detalle_venta":
        for fila in range(len(lista_dict)):
            id = lista_dict[fila].get("id")
            id_venta = lista_dict[fila].get("id_venta")
            id_producto = lista_dict[fila].get("id_producto")
            cantidad = lista_dict[fila].get("cantidad")

            info += f"{id},{id_venta},{id_producto},{cantidad}\n"

        print(info)

    elif nombre_lista == "producto_cantidad":
        for fila in range(len(lista_dict)):
            id_producto = lista_dict[fila].get("id_producto")
            cantidad = lista_dict[fila].get("cantidad")

            info += f"{id_producto},{cantidad}\n"

        print(info)

def mostrar_info_completa_matriz(matriz: list[list]):
    """
    muestra la inforamcion completa de una matriz

    arg: 
        matriz (list[list]): contiene la matriz de datos.

    return:
    """
    
    info = ''
    for fila in matriz:
        id = fila[0]
        nombre = fila[1]
        inventario = fila[2]
        precio = fila[3]
        activo = fila[4]

        info += f'{id},{nombre},{inventario},{precio},{activo}' + "\n"

    print(info)

def do_bubble_sort(lista_dict: list[dict], tipo: str, nombre_lista: str, ord: str= 'ASC'):
    """
    tipo de ordenamiento bubble sort.

    arg: 
        list_dict (list[dict]): contiene la lista de diccionario a ordenar.
        tipo (str): clave del diccionario por la cual se ordenará.
        nombre_lista (str): nombre de la lista para mostrar la información correspondiente.
        ord (str): criterio de ordenamiento.

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

def convertir_valor(valor, tipo: str):
    """
    convierte un valor a un tipo especifico

    arg: 
        valor (str): el valor a convertir.
        tipo (str): el tipo al que se desea convertir.

    return:
        valor convertido al tipo especificado
    """

    if tipo == "int":
        return parsear_str_a_int(valor)
    if tipo == "float":
        return parsear_str_a_float(valor)
    return valor

def parsear_dict_valor(lista_keys: list, lista_tipos: list, dict_lista:list[dict]):
    """
    convierte los valores de un diccionario a tipos especificos

    arg: 
        lista_keys (list): contiene las claves del diccionario.
        lista_tipos (list): contiene los tipos a los que se desea convertir.
        dict_lista (list[dict]): contiene la lista de diccionarios a convertir.

    return:
    """
    for dict_ele in dict_lista:
        for key, tipo in zip(lista_keys, lista_tipos):
            if key in dict_ele:
                dict_ele[key] = tipo(dict_ele[key])

    return dict_lista
    
def parsear_dataset_lidict(datos: list[str]) -> list[dict]:
    """
    convierte un dataset en una lista de diccionarios

    arg: 
        datos (list[str]): contiene el dataset en formato de lista de strings.
        
    return:
        lista_dict: lista de diccionarios
    """

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
    """
    divide un texto en una lista de strings utilizando un separador

    arg: 
        texto (str): el texto a dividir.
        separador (str): el separador a utilizar.

    return:
        lista_str: lista de strings
    """

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
    """
    agrega una palabra a una lista si no está vacía

    arg: 
        lista_palabras (list[str]): contiene la lista de palabras.
        palabra (str): la palabra a agregar.

    return:
        hubo_cambio: True si se agregó la palabra, False si no
    """

    hubo_cambio = False
    if palabra != '':
        lista_palabras.append(palabra)
        hubo_cambio = True
    return hubo_cambio

def parsear_dataset_producto_matriz(datos: list[str]) -> list[list]:
    """
    convierte un dataset de productos en una matriz

    arg: 
        datos (list[str]): contiene el dataset en formato de lista de strings.

    return:
        mi_matriz: matriz de productos
    """

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
    """
    convierte un string a un entero

    arg: 
        texto (str): el string a convertir.
        
    return:
        numero: entero
    """
    numero = int(texto)
    return numero

def parsear_str_a_float(texto: str) -> float:
    """
    convierte un string a un float

    arg: 
        texto (str): el string a convertir.

    return:
        valor: float
    """
    valor = float(texto)
    return valor

def parsear_str_a_booleano(texto: str) -> bool:
    """
    convierte un string a un booleano

    arg: 
        texto (str): el string a convertir.

    return:
        valor: booleano
    """
    if texto == "true":
        return True
    if texto == "false":
        return False

def filtrar_info_dic(lista: list[dict], clave: str, valor: int):
    """
    filtra información de un solo dato en el diccionario

    arg: 
        lista (list[dict]): contiene la lista de diccionarios a filtrar.
        clave (str): la clave del diccionario por la cual se filtrará.
        valor (int): el valor por el cual se filtrará.
    return:
    """
    item_dicccionario = {}
    for item in lista:
        if item.get(clave) == valor:
            item_dicccionario.update(item)
            break

    return item_dicccionario

def filtrar_por_id(dato: dict, valor: int) -> bool:
    """
    filtra un cliente por su ID

    arg: 
        dato (dict): contiene el diccionario a filtrar.
        valor (int): el ID a filtrar.
        
    return:
        True o False
    """
    return dato.get("id") == valor

def filtrar_por_id_venta(dato: dict, valor: int) -> bool:
    """
    filtra una venta por su ID

    arg: 
        dato (dict): contiene el diccionario a filtrar.
        valor (int): el ID a filtrar.
        
    return:
        True o False
    """
    return dato.get("id_venta") == valor

def filtrar_por_activo(dato: dict, valor: str) -> bool:
    """
    filtra por su estado de activo

    arg: 
        dato (dict): contiene el diccionario a filtrar.
        valor (str): el estado de activo a filtrar.
        
    return:
        True o False
    """
    return dato.get("activo") == valor

def filtrar_dato_dict(datos: list[dict], callback, valor: int) -> list[dict]:
    """
    filtra un dato del diccionario

    arg: 
        datos (list[dict]): contiene el diccionario a filtrar.
        valor (int): valor a filtrar.
        callback (function): función de filtrado a utilizar.
        
    return:
        filtrados: lista de diccionarios filtrados
    """

    filtrados = []

    for dato in datos:
        if callback(dato, valor):
            filtrados.append(dato)
    return filtrados

def obtener_valores_unicos(lista: list[dict], clave: str) -> list:
    """
    obtiene los valores únicos de una clave en una lista de diccionarios

    arg: 
        lista (list[dict]): contiene la lista de diccionarios.
        clave (str): la clave del diccionario de la cual se obtendrán los valores únicos.
        
    return:
        lista_ids_unicos: lista de valores únicos
    """

    ids_set = set()

    for item in lista:
        ids_set.add(item.get(clave))
    
    lista_ids_unicos = list(ids_set)

    return lista_ids_unicos

def obtener_ids_dict(lista_dict: list[dict], clave: str) -> list:
    """
    obtiene una lista de IDs de un diccionario

    arg: 
        lista_dict (list[dict]): contiene la lista de diccionarios.
        clave (str): la clave del diccionario de la cual se obtendrán los IDs.
        
    return:
        lista_ids: lista de IDs
    """

    lista_ids = []

    for item in lista_dict:
        lista_ids.append(item.get(clave))
    
    return lista_ids

def obtener_list_diccionario_productos(matriz_producto: list[list]) -> list[dict]:
    """
    obtiene una lista de diccionarios de productos

    arg: 
        matriz_producto (list[list]): contiene la matriz de productos.
        
    return:
        lista_productos: lista de diccionarios de productos
    """
    
    lista_productos = []

    for producto in matriz_producto:
        lista_productos.append({
            "id": producto[0],
            "nombre": producto[1],
            "stock": producto[2],
            "precio": producto[3],
            "activo": producto[4]
        })

    return lista_productos

def join_lista_a_texto(data: list[str], separador: str) -> str:
    """
    convierte una lista de strings en un string separado por un caracter

    arg: 
        data (list[str]): contiene la lista de strings.
        separador (str): el caracter por el cual se separarán los strings.
        
    return:
        nuevo_texto (str): el string resultante
    """

    nuevo_texto = ""
    for palabra in data:
        nuevo_texto += f"{palabra}{separador}"

    nuevo_texto = nuevo_texto[:-1]
    return nuevo_texto

def extraer_datos_dict(target: list[str], diccionario: dict, separador: str, tipo_dato: str):
    """
    extrae los datos de un diccionario y los agrega a una lista de strings

    arg: 
        target (list[str]): contiene la lista de strings donde se agregarán los datos.
        diccionario (dict): contiene el diccionario del cual se extraerán los datos.
        separador (str): el caracter por el cual se separarán los strings.
        tipo_dato (str): el tipo de dato a extraer ('keys' o 'values').

    return:
    """

    if tipo_dato == 'keys':
        datos = list(diccionario.keys())
    else:
        datos = list(diccionario.values())
    texto = join_lista_a_texto(datos, separador) + '\n'
    target.append(texto)

def crear_texto_datos(dataset: list[dict]) -> list[str]:
    """
    convierte un dataset de diccionarios en una lista de strings

    arg: 
        dataset (list[dict]): contiene el dataset en formato de lista de diccionarios.
        
    return:
        lista_texto: lista de strings
    """
    lista_texto = []
    extraer_datos_dict(lista_texto, dataset[0], ',', 'keys')
    for dato in dataset:
        extraer_datos_dict(lista_texto, dato, ',', 'values')
    return lista_texto