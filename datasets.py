producto: list[list]=[
        [1, "Yerba", 25, 4500.0],
        [2, "Azúcar", 40, 1200.0],
        [3, "Arroz", 30, 2100.0],
        [4, "Aceite", 18, 3200.0],
        [5, "Leche", 50, 1700.0],
        [6, "Fideos", 35, 1600.0],
        [7, "Lavandina", 20, 1900.0],
        [8, "Shampoo", 15, 4800.0],
        [9, "Galletitas", 28, 1400.0],
        [10, "Alfajor", 60, 800.0]
    ]

clientes: list[dict] = [
    {
        "id": 1,
        "apellido": "Gomez",
        "nombre": "Juan",
        "ciudad": "Buenos Aires"
    },
    {
        "id": 2,
        "apellido": "Perez",
        "nombre": "Lucia",
        "ciudad": "Cordoba"
    },
    {
        "id": 3,
        "apellido": "Fernandez",
        "nombre": "Martin",
        "ciudad": "Rosario"
    },
    {
        "id": 4,
        "apellido": "Lopez",
        "nombre": "Carla",
        "ciudad": "Mendoza"
    },
    {
        "id": 5,
        "apellido": "Ramirez",
        "nombre": "Sofia",
        "ciudad": "La Plata"
    }
]

ventas: list[dict] = [
    {
        "id": 1,
        "id_cliente": 2
    },
    {
        "id": 2,
        "id_cliente": 1
    },
    {
        "id": 3,
        "id_cliente": 3
    },
    {
        "id": 4,
        "id_cliente": 5
    },
    {
        "id": 5,
        "id_cliente": 4
    },
    {
        "id": 6,
        "id_cliente": 1
    },
    {
        "id": 7,
        "id_cliente": 4
    },
    {
        "id": 8,
        "id_cliente": 2
    },
    {
        "id": 9,
        "id_cliente": 5
    },
    {
        "id": 10,
        "id_cliente": 1
    },
]

detalle_ventas: list[dict] = [
    {
        "id": 1,
        "id_venta": 1,
        "id_producto": 1,
        "cantidad": 1
    },
    {
        "id": 2,
        "id_venta": 2,
        "id_producto": 3,
        "cantidad": 1
    },
    {
        "id": 3,
        "id_venta": 3,
        "id_producto": 2,
        "cantidad": 3
    },
    {
        "id": 4,
        "id_venta": 4,
        "id_producto": 6,
        "cantidad": 2
    },
    {
        "id": 5,
        "id_venta": 5,
        "id_producto": 9,
        "cantidad": 4
    },
    {
        "id": 6,
        "id_venta": 6,
        "id_producto": 8,
        "cantidad": 5
    },
    {
        "id": 7,
        "id_venta": 7,
        "id_producto": 4,
        "cantidad": 2
    },
    {
        "id": 8,
        "id_venta": 8,
        "id_producto": 6,
        "cantidad": 1
    },
    {
        "id": 9,
        "id_venta": 9,
        "id_producto": 6,
        "cantidad": 3
    },
    {
        "id": 10,
        "id_venta": 10,
        "id_producto": 6,
        "cantidad": 2
    },
    {
        "id": 11,
        "id_venta": 1,
        "id_producto": 3,
        "cantidad": 1
    },
    {
        "id": 12,
        "id_venta": 1,
        "id_producto": 8,
        "cantidad": 4
    },
    {
        "id": 13,
        "id_venta": 1,
        "id_producto": 10,
        "cantidad": 4
    },
]