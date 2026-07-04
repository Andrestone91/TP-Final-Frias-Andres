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
        return contenido

def actualizar_lista_json(ruta: str, informacion: list[dict]):
    with open(ruta, "w", encoding=CODIFICACION) as json_file:
        json.dump(informacion, json_file, indent=4)