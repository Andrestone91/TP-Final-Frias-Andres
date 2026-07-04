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
    
def borrar_dato_csv(ruta: str, id: int):
    with open(ruta, "w", encoding=CODIFICACION) as file:
        pass