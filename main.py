from interfaz import aplicacion
from datasets import productos, clientes, ventas, detalle_ventas
from variables import ARCHIVO_CLIENTES, ARCHIVO_PRODUCTOS, ARCHIVO_USUARIOS, ARCHIVO_VENTAS

if __name__ == "__main__":
    
    aplicacion(productos, clientes, ventas, detalle_ventas)