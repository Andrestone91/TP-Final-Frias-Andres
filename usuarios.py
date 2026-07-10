from logica import mostrar_info_completa, obtener_ids_dict, filtrar_info_dic
from archivos import actualizar_lista_json
from validaciones import validar_int, validar_str, validar_alphanum
from variables import ARCHIVO_USUARIOS

def mostrar_usuarios(lista_usuarios: list[dict]):
    mostrar_info_completa(lista_usuarios.get("usuarios"), "usuarios")

def borrar_usuario(lista_usuarios: list[dict]):
    lista_dict_usuarios: list[dict] = lista_usuarios.get("usuarios")
    mostrar_info_completa(lista_dict_usuarios, "usuarios")

    input_id = validar_int("ingrese el id usuario a borrar: ")

    for indice_usuario in range(len(lista_dict_usuarios)):
        if lista_dict_usuarios[indice_usuario].get("id") == input_id:
            lista_dict_usuarios.pop(indice_usuario)
            actualizar_lista_json(ARCHIVO_USUARIOS, lista_usuarios)
            break

    mostrar_info_completa(lista_dict_usuarios, "usuarios")

def crear_usuario(lista_usuarios: list[dict]) -> bool:

    user_valido = False
    password_valido = False
    dict_usuarios: list[dict] = lista_usuarios.get("usuarios")
    
    input_usuario = validar_str("ingrese el nombre de usuario: ")

    for usuario in dict_usuarios:

        if  input_usuario == usuario.get("username"):
            print("[SYSTEM] -- el nombre de usuario ya existe --")
            user_valido = crear_usuario(lista_usuarios)
            break
            
    if user_valido:
        return user_valido
    
    input_password = validar_alphanum("ingrese el password (min. 8 caracteres): ")

    if len(input_password) < 8:
        print("[SYSTEM] -- el password debe contener 8 caracteres como minimo --")
        password_valido = crear_usuario(lista_usuarios)

    if password_valido:
        return password_valido
     
    input_tipo = validar_str("ingrese el tipo [admin - vendedor]: ")

    ids = obtener_ids_dict(dict_usuarios, "id")
    ids.reverse()
    ultimo_id = ids[0]
    nuevo_id = ultimo_id + 1

    dict_usuarios.append({
            "id": nuevo_id,
            "username": input_usuario,
            "password": input_password,
            "tipo": input_tipo,
            "esta_online": False
    })
    actualizar_lista_json(ARCHIVO_USUARIOS, lista_usuarios)
    mostrar_info_completa(dict_usuarios, "usuarios")
    return True

def editar_usuario(lista_usuarios: list[dict]):
    dict_usuarios = lista_usuarios.get("usuarios")
    mostrar_info_completa(dict_usuarios, "usuarios")
    
    input_id = validar_int("seleccione el id del usuario a modificar: ")

    usuario_a_modificar = filtrar_info_dic(dict_usuarios, "id" ,input_id)
    if usuario_a_modificar:
        print("el usuario a modificar es: ")
        usuario = f'{usuario_a_modificar.get("id")},{usuario_a_modificar.get("username")}'\
            f',{usuario_a_modificar.get("password")},{usuario_a_modificar.get("tipo")},{usuario_a_modificar.get("esta_online")}'
        print(usuario)
        opcion = input("que dato desea modificar? [password, tipo]: ")

        match opcion:
            case "password":
                nuevo_password = validar_alphanum("nuevo password [min 8 caracteres]: ")
                if len(nuevo_password) >= 8:
                    usuario_a_modificar.update({'password': nuevo_password})
                else:
                    print("[SYSTEM] -- el password debe contener 8 caracteres como minimo --")
                    return
            case "tipo":
                nuevo_tipo = validar_str("tipo [admin - vendedor]: ")
                usuario_a_modificar.update({'tipo': nuevo_tipo})
            case _:
                print("la opcion no coincide, usuario no modificado")
                return
        actualizar_usuario(lista_usuarios, usuario_a_modificar)
    else:
        print("[SYSTEM] -- el id seleccionado no existe --")

def actualizar_usuario(lista_usuarios: list[dict], usuario: dict):

    """
    actualiza la lista de usuario

    arg: 
        usuario (dicr): el usuario ya modificado que se usa para actualizar la lista de usuarios.
        lista_usuarios (list[dict]): contiene la lista de usuarios en formato de diccionario.
        
    return:
    """
    dict_usuarios = lista_usuarios.get("usuarios")
    cantidad_filas = len(dict_usuarios)

    for fila in range(cantidad_filas):
        if dict_usuarios[fila].get("id") == usuario.get("id"):
            dict_usuarios[fila].update({
                "password": usuario.get("password"),
                "tipo": usuario.get("tipo"),
            })
            actualizar_lista_json(ARCHIVO_USUARIOS, lista_usuarios)
            mostrar_info_completa(dict_usuarios, "usuarios")
            break