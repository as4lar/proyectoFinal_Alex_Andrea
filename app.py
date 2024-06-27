import psycopg2

def conexion():
    connection = psycopg2.connect(
        user="",
        password="",
        host="localhost",
        port="5432",
        database="Inventario")
    return connection

def menu(opcion, cursor):
    if opcion == '0':
        print("SALIENDO...")
    elif opcion == '16':
        ver_equipos_disponibles(cursor)
    elif opcion == '17':
        ver_equipos_ocupados(cursor)

def crear_tabla_usuarios(cursor):
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            area VARCHAR(100) NOT NULL,
            cargo VARCHAR(100),
            correo VARCHAR(100)
        );""")
        cursor.execute("COMMIT")
        print("Tabla usuarios creada")
    except Exception as e:
        print(f"Error {e} al crear la tabla")

def crear_tabla_equipos(cursor):
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS equipos (
            id SERIAL PRIMARY KEY,
            tipo VARCHAR(100) NOT NULL,
            marca VARCHAR(100) NOT NULL,
            modelo VARCHAR(100) NOT NULL,
            numero_serie VARCHAR(100),
            precio DECIMAL,
            disponible BOOLEAN
        );""")
        cursor.execute("COMMIT")
        print("Tabla equipos creada")
    except Exception as e:
        print(f"Error {e} al crear la tabla")

def crear_tabla_prestamos(cursor):
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS prestamos (
            id SERIAL PRIMARY KEY,
            id_usuario INT REFERENCES usuarios(id),
            id_equipo INT REFERENCES equipos(id),
            fecha_entrega DATE,
            fecha_devolucion DATE
        );""")
        cursor.execute("COMMIT")
        print("Tabla prestamos creada")
    except Exception as e:
        print(f"Error {e} al crear la tabla")

def ver_equipos_disponibles(cursor):
    try:
        cursor.execute("""
            SELECT id, tipo, marca, modelo, numero_serie, precio
            FROM equipos
            WHERE disponible = TRUE;
        """)
        resultados = cursor.fetchall()
        for row in resultados:
            print("Equipo ID:", row[0])
            print("Tipo:", row[1])
            print("Marca:", row[2])
            print("Modelo:", row[3])
            print("Número de Serie:", row[4])
            print("Precio:", row[5])
            print("-" * 50)
    except Exception as e:
        print(f"Error {e} al consultar los equipos disponibles")

def ver_equipos_ocupados(cursor):
    try:
        cursor.execute("""
            SELECT e.id, e.tipo, e.marca, e.modelo, e.numero_serie, e.precio, u.id AS usuario_id, u.nombre, u.area, u.cargo, u.correo
            FROM equipos e
            JOIN prestamos p ON e.id = p.id_equipo
            JOIN usuarios u ON p.id_usuario = u.id
            WHERE e.disponible = FALSE;
        """)
        resultados = cursor.fetchall()
        for row in resultados:
            print("Equipo ID:", row[0])
            print("Tipo:", row[1])
            print("Marca:", row[2])
            print("Modelo:", row[3])
            print("Número de Serie:", row[4])
            print("Precio:", row[5])
            print("Usuario ID:", row[6])
            print("Nombre del Usuario:", row[7])
            print("Área:", row[8])
            print("Cargo:", row[9])
            print("Correo:", row[10])
            print("-" * 50)
    except Exception as e:
        print(f"Error {e} al consultar los equipos ocupados y sus usuarios")


connection = None
cursor = None
try:
    connection = conexion()
    cursor = connection.cursor()
    crear_tabla_usuarios(cursor)
    crear_tabla_equipos(cursor)
    crear_tabla_prestamos(cursor)

    opcion = '10'
    while opcion != '0':
        print("MENU")
        print("0.- SALIR")
        print("------ USUARIOS ------")
        print("1.- CREAR USUARIO")
        print("2.- VER USUARIOS")
        print("3.- VER USUARIO")
        print("4.- ACTUALIZAR DATOS USUARIO")
        print("5.- ELIMINAR USUARIO")
        print("------ EQUIPOS ------")
        print("6.- CREAR EQUIPO")
        print("7.- VER EQUIPOS")
        print("8.- VER EQUIPO")
        print("9.- ACTUALIZAR EQUIPO")
        print("10.- ELIMINAR EQUIPO")
        print("------ PRESTAMOS ------")
        print("11.- CREAR PRESTAMO")
        print("12.- VER PRESTAMOS")
        print("13.- VER PRESTAMO")
        print("14.- ACTUALIZAR PRESTAMO")
        print("15.- ELIMINAR PRESTAMO")
        print("------ INFORMACION ADICIONAL ------")
        print("16.- EQUIPOS DISPONIBLES")
        print("17.- EQUIPOS EN PRÉSTAMO")

        opcion = input("Ingrese una opción: ")
        menu(opcion, cursor)
except Exception as e:
    print(f"Error {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

