from interfaz import aplicacion

if __name__ == "__main__":

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

    aplicacion(producto, clientes)