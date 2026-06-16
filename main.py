from interfaz import aplicacion
from datasets import productos, clientes, ventas, detalle_ventas

if __name__ == "__main__":
    aplicacion(productos, clientes, ventas, detalle_ventas)