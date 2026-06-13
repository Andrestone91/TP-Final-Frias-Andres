from interfaz import aplicacion
from datasets import producto, clientes, ventas, detalle_ventas

if __name__ == "__main__":
    aplicacion(producto, clientes, ventas, detalle_ventas)