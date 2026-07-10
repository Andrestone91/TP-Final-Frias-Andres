from variables import CODIFICACION
import json

def leer_json(ruta):
    informacion = {}
    with open (ruta, 'r', encoding=CODIFICACION) as json_file:
        informacion = json.load(json_file)
        print('[SYSTEM] -- Informacion extraida --')
    return informacion

def leer_csv(ruta: str):
    with open(ruta, "r", encoding=CODIFICACION) as file:
        contenido = file.readlines()
        print('[SYSTEM] -- Informacion extraida --')
        return contenido

def actualizar_lista_json(ruta: str, informacion: list[dict]):
    with open(ruta, "w", encoding=CODIFICACION) as json_file:
        json.dump(informacion, json_file, indent=4)
        print("[SYSTEM] -- se actualizo correctamente --")

# def guardar_matriz_archivo(matriz_t: list[list], cabecera: list[str],ruta: str):
#     with open(ruta, 'w', encoding=CODIFICACION) as archivo:

#         lista_texto = []

#         headr = join_lista_a_texto(cabecera, ',') + '\n'
#         lista_texto.append(headr)

#         for fila in matriz_t:
#             texto = join_lista_a_texto(fila, ',') + '\n'
#             lista_texto.append(texto)

#         archivo.writelines(lista_texto)

# def crear_texto_datos(dataset: list[dict]):
#     lista_texto = []
#     extraer_datos_dict(lista_texto, dataset[0], ',', 'keys')
#     for heroe in dataset:
#         extraer_datos_dict(lista_texto, heroe, ',', 'values')
#     return lista_texto

# def guardar_dataset_dict_archivo(dataset: list[dict], ruta: str):

#     with open(ruta, 'w', encoding=CODIFICACION) as file:
#         lista_texto = crear_texto_datos(dataset)
#         file.writelines(lista_texto)