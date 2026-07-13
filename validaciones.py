from logica import parsear_str_a_booleano

def validar_opcion(op_min:str, op_max:str) -> int:
    """
    valida la opcion seleccionada

    arg: 
        op_min (int): opcion minima
        op_max (int): opcion maxima
        
    return
        input_int (int): devuelve el numero de la opcion
    """

    input_str = input(f"ingrese una opcion [{op_min}-{op_max}]: ")
    input_int = None

    if not input_str.isnumeric() or \
        not(op_min <= int(input_str) <= op_max):
        print("ERROR:, seleccione una opcion valida")
        input_int = validar_opcion(op_min, op_max)

    if input_int != None:
        return input_int
    else:
        return int(input_str)
    
def validar_str(mensaje: str) -> str:
    """
    valida que el input sea un string

    arg: 
        mensaje (str): mensaje a mostrar al usuario

    return:
        input_str (str): devuelve el string ingresado por el usuario
    """
    input_str = input(mensaje)

    if not input_str.replace(" ", "").isalpha():
        print("ERROR: ingrese un nombre valido")
        return validar_str(mensaje)

    return input_str

def validar_alphanum(mensaje: str) -> str:
    """
    valida que el input sea alfanumerico

    arg: 
        mensaje (str): mensaje a mostrar al usuario

    return:
        input_str (str): devuelve el string ingresado por el usuario
    """
    input_str = input(mensaje)

    if not input_str.isalnum():
        print("ERROR: ingrese caractere validos")
        validar_str(mensaje)

    return input_str

def validar_int(mensaje: str) -> int:
    """
    valida que el input sea un numero entero

    arg: 
        mensaje (str): mensaje a mostrar al usuario

    return:
        input_int (int): devuelve el numero ingresado por el usuario
    """

    input_str = input(mensaje)
    input_int = None

    if not input_str.isnumeric():
        print("ERROR: ingrese un numero")
        input_int = validar_int(mensaje)

    if input_int != None:
        return input_int
    else:
        return int(input_str)

def validar_float(mensaje: str) -> float:
    """
    valida que el input sea un numero decimal

    arg: 
        mensaje (str): mensaje a mostrar al usuario

    return:
        input_float (float): devuelve el numero ingresado por el usuario
    """
    input_str = input(mensaje)
    input_float = None

    if not input_str.isnumeric() or not input_str.isdecimal():
        print("ERROR: ingrese un numero")
        input_float = validar_float(mensaje)

    if input_float != None:
        return input_float
    else:
        return float(input_str)
    
def validar_bool(mensaje: str) -> bool:
    """
    valida que el input sea un booleano

    arg: 
        mensaje (str): mensaje a mostrar al usuario

    return:
        input_bool (bool): devuelve el booleano ingresado por el usuario
    """
    input_str = input(mensaje)

    if input_str not in ('true', 'false'):
        print("ERROR: ingrese true o false")
        return validar_bool(mensaje)
    return parsear_str_a_booleano(input_str)
