from variables import ARCHIVO_USUARIOS
from archivos import leer_json, actualizar_lista_json

def iniciar_sesion(usuario: dict):
    """
    inicia la sesion

    arg: 
        usuarios (dict): contiene los usuarios en diccionario
        
    return
    """
    informacion_usuarios: dict = leer_json(ARCHIVO_USUARIOS)
    contador_intentos = 0
    run_login = True

    while run_login:      
        input_usuario = input("nombre de usuario: ")
        input_password = input("contraseña: ")

        usuario_encontrado = buscar_usuario(informacion_usuarios, input_usuario, input_password)

        if usuario_encontrado:
            usuario = usuario_encontrado
            print("sesion iniciada correctamente")
            run_login = False
        else:
            contador_intentos += 1
            run_login = manejo_intentos(contador_intentos, 3)

    return usuario  

def buscar_usuario(dict_usuarios: dict, input_usuario: str, input_password: str) -> dict:
    """
    busca el usuario mediante el input, en caso que las credenciales sean validas devuuelve true, de lo contrario false

    arg: 
        usuarios (dict): usuarios en diccionario
        input_usuario (str): usuario ingreado
        input_password (str): password ingresado
    return:
        bool
    """
    lista_usuarios = dict_usuarios.get("usuarios")
    for indice in range(len(lista_usuarios)):
        if lista_usuarios[indice].get("username") == input_usuario and lista_usuarios[indice].get("password") == input_password:
            lista_usuarios[indice].update({"esta_online": True})
            actualizar_lista_json(ARCHIVO_USUARIOS, dict_usuarios)
            return lista_usuarios[indice]

def manejo_intentos(contador_intentos: int, intentos: int) -> bool:
    """
    define el limite de intentos para iniciar la sesion

    arg: 
        contador_intentos (int): acomulador de intentos que se fue realizando
        intentos (int): maximo numero de intentos
    return:
        bool
    """
    if contador_intentos == intentos:
        print("se agotaron los intentos")
        return False
    print("vuelva a intentar")
    return True

def cerrar_sesion(dict_usuarios: dict, id: int):
    lista_usuarios = dict_usuarios.get("usuarios")
    for indice in range(len(lista_usuarios)):
        if lista_usuarios[indice].get("id") == id:
             lista_usuarios[indice].update({"esta_online": False})
    actualizar_lista_json(ARCHIVO_USUARIOS, dict_usuarios)