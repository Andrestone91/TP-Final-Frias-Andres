from variables import ARCHIVO_USUARIOS
from logica import leer_json

def iniciar_sesion(usuario: dict):

        informacion_usuarios: dict = leer_json(ARCHIVO_USUARIOS)
        contador_intentos = 0
        run_login = True

        while run_login:      
            input_usuario = input("nombre de usuario: ")
            input_password = input("contraseña: ")

            usuario_encontrado = buscar_usuario_con_credenciales(informacion_usuarios.get("usuarios"), input_usuario, input_password)

            if usuario_encontrado:
                usuario = usuario_encontrado
                print("sesion iniciada correctamente")
                run_login = False
            else:
                contador_intentos += 1
                run_login = manejo_intentos(contador_intentos, 3)

        return usuario  

def buscar_usuario_con_credenciales(dict_usuarios: dict, input_usuario: str, input_password: str) -> bool:
    for usuario in dict_usuarios:
        if usuario.get("username") == input_usuario and usuario.get("password") == input_password:
            return usuario

def manejo_intentos(contador_intentos: int, intentos: int) -> bool:
    if contador_intentos == intentos:
        print("se agotaron los intentos")
        return False
    print("vuelva a intentar")
    return True