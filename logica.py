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

def obtener_ids_clientes(lista_clientes: list[dict]) -> list:
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
        "id": f"{nuevo_id}",
        "apellido": f"{input_apellido}",
        "nombre": f"{input_nombre}",
        "ciudad": f"{input_ciudad}"
    }

    lista_clientes.append(nuevo_cliente)
    print(lista_clientes)

def obtener_cliente_por_dato(lista_clientes: list[dict], id: int) -> dict:
    """
    obtiene un cliente en formato diccionario

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

    tipo_datos: list[str] = ["apellido", "nombre", "ciudad"]

    input_id = validar_int(f"ingrese el ID del cliente a modificar: ")
    cliente = obtener_cliente_por_dato(lista_clientes, input_id)
    
    if len(cliente) > 0:
        print("cliente seleccionado es: ")
        print(cliente)

        input_tipo = validar_str(f"ingrese el tipo de dato a modificar [{tipo_datos[0]}-{tipo_datos[1]}-{tipo_datos[2]}]:")
        tipo_es_valido = validar_tipo(tipo_datos, input_tipo)

        cliente_a_modificar(cliente, tipo_es_valido, tipo_datos, input_tipo, lista_clientes)
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
                "id": f"{cliente.get("id")}",
                "apellido": f"{cliente.get("apellido")}",
                "nombre": f"{cliente.get("nombre")}",
                "ciudad": f"{cliente.get("ciudad")}"
            })
            print("cliente actualizado correctamente")
            print(lista_cliente)
            break

def validar_tipo(tipo_lista: list[str], input_tipo: str) -> bool:

    if input_tipo == tipo_lista[0] or\
        input_tipo == tipo_lista[1] or\
        input_tipo == tipo_lista[2]:

        return True
    else:
        return False
    
def cliente_a_modificar(cliente: dict, tipo_es_valido: bool, tipo_datos: list[str], input_tipo: str, lista_clientes: list[dict]):
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
        actualizar_cliente(lista_clientes, cliente)
    else:
        print(f"el tipo {input_tipo} es incorrecto vuelva a intentar")