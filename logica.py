from validaciones import validar_str, validar_int, validar_float

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

def obtener_producto_por_dato(matriz_producto: list[list], columna: int, valor) -> list:
    producto = []

    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][columna] == valor:
            for columna in range(cantidad_columnas):
                 producto.append(matriz_producto[fila][columna])

    return producto
    
def cargar_producto(matriz_producto: list[list]):
    ids = obtener_ids(matriz_producto)
    ids.reverse()
    
    obtener_ultimo_id = ids[0]
    nuevo_id = obtener_ultimo_id + 1

    nombre = validar_str("ingresar nombre del producto: ")
    stock = validar_int("stock disponible: ")
    precio_unitario = validar_float("ingrese precio unitario: ")

    nuevo_producto = [nuevo_id, nombre, stock, precio_unitario]

    matriz_producto.append(nuevo_producto)
    print("producto agregado correctamente")
    print(matriz_producto)

def actualizar_producto(matriz_producto: list[list], producto_modificado: list, id: int):
    cantidad_filas = len(matriz_producto)
    cantidad_columnas = len(matriz_producto[0])

    for fila in range(cantidad_filas):
        if matriz_producto[fila][0] == id:
            for columna in range(1, cantidad_columnas):
                matriz_producto[fila][columna] = producto_modificado[columna]

    print(matriz_producto)

def modificar_producto(matriz_producto: list[list]):

    input_int = validar_int("ingresar ID del prodcuto a modificar: ")
    producto_a_modificar = obtener_producto_por_dato(matriz_producto, 0, input_int)
    print("el producto a modificar es: ")
    print(producto_a_modificar)
    opcion = input("que dato desea modificar? [nombre, inventario, precio]: ")

    match opcion:
        case "nombre":
            nuevo_nombre = validar_str("nuevo nombre: ")
            producto_a_modificar[1] = nuevo_nombre
        case "inventario":
            nuevo_stock = validar_int("nuevo stock: ")
            producto_a_modificar[2] = nuevo_stock
        case "precio":
            nuevo_precio = validar_float("nuevo precio: ")
            producto_a_modificar[3] = nuevo_precio
        case _:
            print("la opcion no coincide, producto no modificado")
    
    actualizar_producto(matriz_producto, producto_a_modificar, input_int)

def producto_a_borrar(matriz_producto:list[list]):
      print(matriz_producto)

      input_id = validar_int("ingrese el numero id a borrar: ")

      for fila in range(len(matriz_producto)):
          if matriz_producto[fila][0] == input_id:
              matriz_producto.pop(fila)
              print("producto borrado:")
              break
          else:
              print("id no encontrado:")
      print(matriz_producto)

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

    else:
        print("lista no reconocida")

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
# def parsear_dict_valor(lista: list[dict], keys: list[str], posiciones: list[int], tipo: str):
#     for fila in lista:
#         for key, posicion in zip(keys, posiciones):
#             if key in fila:
#                     fila[key] = convertir_valor(fila[key], tipo)
#             else:
#                 if 0 <= posicion < len(fila):
#                     fila[posicion] = convertir_valor(fila[posicion], tipo)

#     return lista
    
def parsear_dataset_lidict(datos: list[str]) -> list[dict]:
    str_claves_limpias = datos.pop(0).replace('\n', '')
    claves = split_texto(str_claves_limpias, ',')
    lista_dict_heroes = []

    for heroe in datos:
        heroe = heroe.replace('\n', '')
        datos_heroe = split_texto(heroe, ',')
        heroe_dict = {}

        for indice_clave in range(len(claves)):
            heroe_dict.update(
                {claves[indice_clave] : datos_heroe[indice_clave]}
            )
        lista_dict_heroes.append(heroe_dict)
    return lista_dict_heroes

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

def filtrar_info_dic(lista: list[dict], clave: str, id: int):
    item_dicccionario = {}
    for item in lista:
        if item.get(clave) == id:
            item_dicccionario.update(item)
            break

    return item_dicccionario