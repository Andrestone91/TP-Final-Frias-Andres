from interfaz import aplicacion
from datasets import productos, clientes, ventas, detalle_ventas
from variables import ARCHIVO_CLIENTES, ARCHIVO_PRODUCTOS, ARCHIVO_USUARIOS, ARCHIVO_VENTAS, ARCHIVO_DETALLE_VENTA
from logica import leer_csv, parsear_dataset_lidict, parsear_dataset_producto_matriz

if __name__ == "__main__":

    # productos = leer_csv(ARCHIVO_PRODUCTOS)
    # matriz_productos = parsear_dataset_producto_matriz(productos)

    # clientes = leer_csv(ARCHIVO_CLIENTES)
    # dict_clientes = parsear_dataset_lidict(clientes)

    # ventas = leer_csv(ARCHIVO_VENTAS)
    # dict_ventas = parsear_dataset_lidict(ventas)

    # detalle_venta = leer_csv(ARCHIVO_DETALLE_VENTA)
    # dict_detalle_venta = parsear_dataset_lidict(detalle_venta)

    aplicacion(productos, clientes, ventas, detalle_ventas)