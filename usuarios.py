from logica import mostrar_info_completa
from archivos import actualizar_lista_json
from validaciones import validar_int
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