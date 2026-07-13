from validaciones import validar_str, validar_int
from logica import mostrar_info_completa, obtener_valores_unicos, do_bubble_sort
from ventas import obtener_detalle_ventas_de_una_venta
from variables import ARCHIVO_CLIENTES
from archivos import guardar_dataset_dict_archivo

def obtener_ids_clientes(lista_clientes: list[dict]) -> list:
    """
    se obtiene la lista de ids de todos los clientes

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        
    return:
        Ids_clientes: lista de id de clientes
    """

    ids_clientes = []

    cantidad_filas = len(lista_clientes)

    for fila in range(cantidad_filas):
        ids_clientes.append(lista_clientes[fila].get("id"))
    
    return ids_clientes

def cargar_cliente(lista_clientes: list[dict]):
    """
    agrega un nuevo cliente a la lista

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario
        
    return:
    """
    ids_clientes = obtener_ids_clientes(lista_clientes)
    input_apellido = validar_str("ingrese el apellido: ")
    input_nombre = validar_str("ingrese el nombre: ")
    input_ciudad = validar_str("ingrese la ciudad: ")

    ids_clientes.reverse()

    ultimo_id = ids_clientes[0]

    nuevo_id = ultimo_id + 1

    nuevo_cliente = {
        "id": nuevo_id,
        "apellido": f"{input_apellido}",
        "nombre": f"{input_nombre}",
        "ciudad": f"{input_ciudad}"
    }

    lista_clientes.append(nuevo_cliente)
    guardar_dataset_dict_archivo(lista_clientes, ARCHIVO_CLIENTES)
    mostrar_info_completa(lista_clientes, "clientes")

def obtener_cliente_por_dato(lista_clientes: list[dict], id: int) -> dict:
    """
    obtiene un cliente en formato diccionario mediante su ID

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario
        id (int): el input id seleccionado
        
    return: devuelve el cliente
    """
    cantidad_filas = len(lista_clientes)
    cliente = {}
    for fila in range(cantidad_filas):
        if lista_clientes[fila].get("id") == id:
            return lista_clientes[fila]
    return cliente

def modificar_cliente(lista_clientes: list[dict]):
    """
    funcion para modificar un cliente

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario
        
    return:
    """
    mostrar_info_completa(lista_clientes, "clientes")
    tipo_datos: list[str] = ["apellido", "nombre", "ciudad", "activo"]

    input_id = validar_int(f"ingrese el ID del cliente a modificar: ")
    cliente = obtener_cliente_por_dato(lista_clientes, input_id)
    
    if len(cliente) > 0:
        print("cliente seleccionado es: ")
        info = f'{cliente.get("id")},{cliente.get("apellido")},{cliente.get("nombre")},{cliente.get("ciudad")},{cliente.get("activo")}'
        print(info)

        input_tipo =\
              validar_str(f"ingrese el tipo de dato a modificar [{tipo_datos[0]}-{tipo_datos[1]}-{tipo_datos[2]}-{tipo_datos[3]}]:")
        tipo_es_valido = validar_tipo(tipo_datos, input_tipo)

        actualizar_un_dato_cliente(cliente, tipo_es_valido, tipo_datos, input_tipo, lista_clientes)
    else:
        print("no se encontro el cliente seleccionado")
    
def actualizar_cliente(lista_cliente: list[dict], cliente: dict):
    """
    actualiza la lista de clientes

    arg: 
        cliente (dicr): el cliente ya modificado que se usa para actualizar la lista de clientes.
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        
    return:
    """
    cantidad_filas = len(lista_cliente)

    for fila in range(cantidad_filas):
        if lista_cliente[fila].get("id") == cliente.get("id"):
            lista_cliente[fila].update({
                "id": cliente.get("id"),
                "apellido": cliente.get("apellido"),
                "nombre": cliente.get("nombre"),
                "ciudad": cliente.get("ciudad"),
                "activo": cliente.get("activo")

            })
            guardar_dataset_dict_archivo(lista_cliente, ARCHIVO_CLIENTES)
            mostrar_info_completa(lista_cliente, "clientes")
            break

def validar_tipo(tipo_lista: list[str], input_tipo: str) -> bool:
    """
    valida el tipo seleccionado para modificar cliente

    arg: 
        input_tipo (str): el tipo ingresado.
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        
    return:
        True ó False
    """

    if input_tipo == tipo_lista[0] or\
        input_tipo == tipo_lista[1] or\
        input_tipo == tipo_lista[2] or\
        input_tipo == tipo_lista[3]:
        return True
    else:
        return False
    
def actualizar_un_dato_cliente(cliente: dict, tipo_es_valido: bool, tipo_datos: list[str], input_tipo: str, lista_clientes: list[dict]):
    """
    se modifica el cliente seleccionado

    arg: 
        cliente (dicr): el cliente que se va a modificar.
        tipo_es_valido (bool): flag para validar si el tipo ingresado fue valido.
        tipo_datos (list[dict]): contiene la lista de tipos de datos permitidos.
        input_tipo (str): el tipo ingresado.
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        
    return:
    """
    if tipo_es_valido:
        input_valor = validar_str(f"ingrese el nuevo valor para {input_tipo}: ")
        match input_tipo:
            case "apellido":
                cliente.update({tipo_datos[0]: input_valor})
            case "nombre":
                cliente.update({tipo_datos[1]: input_valor})
            case "ciudad":
                cliente.update({tipo_datos[2]: input_valor})
            case "activo":
                if input_valor not in ["true", "false"]:
                    print("eñ tipo es incorrecto")
                cliente.update({tipo_datos[3]: input_valor})
        actualizar_cliente(lista_clientes, cliente)
    else:
        print(f"el tipo {input_tipo} es incorrecto vuelva a intentar")

def dar_de_baja(input_nuevo_tipo: str):
    match input_nuevo_tipo:
        case "logica":
            pass
        case "fisica":
            pass

def borrar_cliente(lista_clientes: list[dict]):
    """
    borra un cliente

    arg: 
        lista_clientes (list[dict]): contiene la lista de clientes en formato de diccionario.
        
    return:
    """

    mostrar_info_completa(lista_clientes, "clientes")
    input_id = validar_int("ingrese el numero id a borrar: ")

    for fila in range(len(lista_clientes)):
        if lista_clientes[fila].get("id") == input_id:
            lista_clientes.pop(fila)
            print("cliente borrado:")
            break
    guardar_dataset_dict_archivo(lista_clientes, ARCHIVO_CLIENTES)
    mostrar_info_completa(lista_clientes, "clientes")

def mostrar_cliente_por_ciudad(lista_clientes: list[dict]):
    ciudades = obtener_valores_unicos(lista_clientes, "ciudad")
    info_ciudad = ""
    for ciudad in ciudades:
        info_ciudad += f'{ciudad} - '
    
    input_ciudad = validar_str(f"ingrese algua de las siguientes ciudades --- {info_ciudad}: ")

    if input_ciudad not in ciudades:
        print(f"la ciudad {input_ciudad} no es valida")
        return
    
    clientes_unica_ciudad = obtener_detalle_ventas_de_una_venta(lista_clientes, input_ciudad, "ciudad")
    do_bubble_sort(clientes_unica_ciudad, "apellido", "clientes", "ASC")
