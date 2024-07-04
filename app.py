import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def conexion():
    connection = psycopg2.connect(
        user="postgres",
        password="1234567",
        host="localhost",
        port="5432",
        database="Inventario")
    return connection

def send_email(to_address):
    from_address = "tuemail@example.com"
    subject = "Límite de préstamos excedido"
    body = "Ha sobrepasado el límite de tres préstamos activos."

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_address, "tucontraseña")
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Correo enviado")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

def menu(opcion, cursor):
    if opcion == '0':
        print("SALIENDO...")
    elif opcion == '1':
        crear_usuario(cursor)
    elif opcion == '2':
        ver_usuarios(cursor)
    elif opcion == '3':
        ver_usuario(cursor)
    elif opcion == '4':
        actualizar_usuario(cursor)
    elif opcion == '5':
        eliminar_usuario(cursor)
    elif opcion == '6':
        crear_equipo(cursor)
    elif opcion == '7':
        ver_equipos(cursor)
    elif opcion == '8':
        ver_equipo(cursor)
    elif opcion == '9':
        actualizar_equipo(cursor)
    elif opcion == '10':
        eliminar_equipo(cursor)
    elif opcion == '11':
        crear_prestamo(cursor)
    elif opcion == '12':
        ver_prestamos(cursor)
    elif opcion == '13':
        ver_prestamo(cursor)
    elif opcion == '14':
        actualizar_prestamo(cursor)
    elif opcion == '15':
        eliminar_prestamo(cursor)
    elif opcion == '16':
        ver_equipos_disponibles(cursor)
    elif opcion == '17':
        ver_equipos_ocupados(cursor)
    elif opcion == '18':
        crear_funcion_y_trigger(cursor)

# CRUD de usuarios
#-----------------------------------------------------------
def crear_usuario(cursor):
    try:
        cursor.execute("BEGIN")
        nombre = input("Ingrese el nombre del usuario: ")
        area = input("Ingrese el área del usuario: ")
        cargo = input("Ingrese el cargo del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        cursor.execute(f"""
            INSERT INTO usuarios (nombre, area, cargo, correo)
            VALUES ('{nombre}', '{area}', '{cargo}', '{correo}');
        """)
        cursor.execute("COMMIT")
        print("Usuario creado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al crear el usuario")

def ver_usuarios(cursor):
    try:
        cursor.execute("BEGIN")
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0])
            print("Nombre:", row[1])
            print("Área:", row[2])
            print("Cargo:", row[3])
            print("Correo:", row[4])
            print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar los usuarios")

def ver_usuario(cursor):
    try:
        cursor.execute("BEGIN")
        id_usuario = input("Ingrese el ID del usuario: ")
        cursor.execute(f"SELECT * FROM usuarios WHERE id = {id_usuario}")
        resultado = cursor.fetchone()
        print("ID:", resultado[0])
        print("Nombre:", resultado[1])
        print("Área:", resultado[2])
        print("Cargo:", resultado[3])
        print("Correo:", resultado[4])
        print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar el usuario")

def actualizar_usuario(cursor):
    try:
        cursor.execute("BEGIN")
        id_usuario = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        area = input("Ingrese el área del usuario: ")
        cargo = input("Ingrese el cargo del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        cursor.execute(f"""
            UPDATE usuarios
            SET nombre = '{nombre}', area = '{area}', cargo = '{cargo}', correo = '{correo}'
            WHERE id = {id_usuario};
        """)
        cursor.execute("COMMIT")
        print("Usuario actualizado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al actualizar el usuario")

def eliminar_usuario(cursor):
    try:
        cursor.execute("BEGIN")
        id_usuario = input("Ingrese el ID del usuario: ")
        cursor.execute(f"DELETE FROM usuarios WHERE id = {id_usuario}")
        cursor.execute("COMMIT")
        print("Usuario eliminado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al eliminar el usuario")

#-----------------------------------------------------------

# CRUD de equipos
#-----------------------------------------------------------
def crear_equipo(cursor):
    try:
        cursor.execute("BEGIN")
        tipo = input("Ingrese el tipo del equipo: ")
        marca = input("Ingrese la marca del equipo: ")
        modelo = input("Ingrese el modelo del equipo: ")
        numero_serie = input("Ingrese el número de serie del equipo: ")
        precio = float(input("Ingrese el precio del equipo: "))
        disponible = True
        cursor.execute(f"""
            INSERT INTO equipos (tipo, marca, modelo, numero_serie, precio, disponible)
            VALUES ('{tipo}', '{marca}', '{modelo}', '{numero_serie}', {precio}, {disponible});
        """)
        cursor.execute("COMMIT")
        print("Equipo creado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al crear el equipo")

def ver_equipos(cursor):
    try:
        cursor.execute("BEGIN")
        cursor.execute("SELECT * FROM equipos")
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0])
            print("Tipo:", row[1])
            print("Marca:", row[2])
            print("Modelo:", row[3])
            print("Número de Serie:", row[4])
            print("Precio:", row[5])
            print("Disponible:", row[6])
            print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar los equipos")

def ver_equipo(cursor):
    try:
        cursor.execute("BEGIN")
        id_equipo = input("Ingrese el ID del equipo: ")
        cursor.execute(f"SELECT * FROM equipos WHERE id = {id_equipo}")
        resultado = cursor.fetchone()
        print("ID:", resultado[0])
        print("Tipo:", resultado[1])
        print("Marca:", resultado[2])
        print("Modelo:", resultado[3])
        print("Número de Serie:", resultado[4])
        print("Precio:", resultado[5])
        print("Disponible:", resultado[6])
        print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar el equipo")

def actualizar_equipo(cursor):
    try:
        cursor.execute("BEGIN")
        id_equipo = input("Ingrese el ID del equipo: ")
        tipo = input("Ingrese el tipo del equipo: ")
        marca = input("Ingrese la marca del equipo: ")
        modelo = input("Ingrese el modelo del equipo: ")
        numero_serie = input("Ingrese el número de serie del equipo: ")
        precio = float(input("Ingrese el precio del equipo: "))
        disponible = input("Ingrese si el equipo está disponible (True/False): ")
        cursor.execute(f"""
            UPDATE equipos
            SET tipo = '{tipo}', marca = '{marca}', modelo = '{modelo}', numero_serie = '{numero_serie}', precio = {precio}, disponible = {disponible}
            WHERE id = {id_equipo};
        """)
        cursor.execute("COMMIT")
        print("Equipo actualizado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al actualizar el equipo")

def eliminar_equipo(cursor):
    try:
        cursor.execute("BEGIN")
        id_equipo = input("Ingrese el ID del equipo: ")
        cursor.execute(f"DELETE FROM equipos WHERE id = {id_equipo}")
        cursor.execute("COMMIT")
        print("Equipo eliminado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al eliminar el equipo")   

#-----------------------------------------------------------

# CRUD de prestamos
#-----------------------------------------------------------

def crear_prestamo(cursor):
    try:
        cursor.execute("BEGIN")
        id_usuario = input("Ingrese el ID del usuario: ")
        id_equipo = input("Ingrese el ID del equipo: ")
        fecha_entrega = input("Ingrese la fecha de entrega (YYYY-MM-DD): ")
        fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
        cursor.execute(f"""
            INSERT INTO prestamos (id_usuario, id_equipo, fecha_entrega, fecha_devolucion)
            VALUES ({id_usuario}, {id_equipo}, '{fecha_entrega}', '{fecha_devolucion}');
        """)
        cursor.execute(f"""
            UPDATE equipos
            SET disponible = FALSE
            WHERE id = {id_equipo};
        """)
        cursor.execute("COMMIT")
        print("Préstamo creado")
    except psycopg2.Error as e:
        if e.pgcode == 'P0001':  # Capturamos la excepción específica lanzada por el trigger
            cursor.execute(f"SELECT correo FROM usuarios WHERE id = {id_usuario}")
            correo_usuario = cursor.fetchone()[0]
            send_email(correo_usuario)  # Enviamos el correo al usuario
        cursor.execute("ROLLBACK")
        print(f"Error {e} al crear el préstamo")

def ver_prestamos(cursor):
    try:
        cursor.execute("BEGIN")
        cursor.execute("""SELECT * FROM prestamos""")
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0])
            print("ID Usuario:", row[1])
            print("ID Equipo:", row[2])
            print("Fecha de Entrega:", row[3])
            print("Fecha de Devolución:", row[4])
            print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar los préstamos")

def ver_prestamo(cursor):
    try:
        cursor.execute("BEGIN")
        id_prestamo = input("Ingrese el ID del préstamo: ")
        cursor.execute(f"SELECT * FROM prestamos WHERE id = {id_prestamo}")
        resultado = cursor.fetchone()
        print("ID:", resultado[0])
        print("ID Usuario:", resultado[1])
        print("ID Equipo:", resultado[2])
        print("Fecha de Entrega:", resultado[3])
        print("Fecha de Devolución:", resultado[4])
        print("-" * 50)
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al consultar el préstamo")

def actualizar_prestamo(cursor):
    try:
        cursor.execute("BEGIN")
        id_prestamo = input("Ingrese el ID del préstamo: ")
        id_usuario = input("Ingrese el ID del usuario: ")
        id_equipo = input("Ingrese el ID del equipo: ")
        fecha_entrega = input("Ingrese la fecha de entrega (YYYY-MM-DD): ")
        fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
        cursor.execute(f"""
            UPDATE prestamos
            SET id_usuario = {id_usuario}, id_equipo = {id_equipo}, fecha_entrega = '{fecha_entrega}', fecha_devolucion = '{fecha_devolucion}'
            WHERE id = {id_prestamo};
        """)
        cursor.execute("COMMIT")
        print("Préstamo actualizado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al actualizar el préstamo")

def eliminar_prestamo(cursor):
    try:
        cursor.execute("BEGIN")
        id_prestamo = input("Ingrese el ID del préstamo: ")
        cursor.execute(f"SELECT id_equipo FROM prestamos WHERE id = {id_prestamo}")
        id_equipo = cursor.fetchone()[0]
        cursor.execute(f"""
            UPDATE equipos
            SET disponible = TRUE
            WHERE id = {id_equipo};
        """)
        cursor.execute(f"DELETE FROM prestamos WHERE id = {id_prestamo}")
        cursor.execute("COMMIT")
        print("Préstamo eliminado")
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error {e} al eliminar el préstamo")

#-----------------------------------------------------------

def crear_funcion_y_trigger(cursor):
    try:
        cursor.execute("""
            CREATE OR REPLACE FUNCTION verificar_prestamos()
            RETURNS TRIGGER AS $$
            BEGIN
                IF (SELECT COUNT(*) FROM prestamos WHERE id_usuario = NEW.id_usuario) >= 3 THEN
                    RAISE EXCEPTION 'El usuario ya tiene 3 préstamos activos';
                END IF;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        """)
        cursor.execute("COMMIT")

        cursor.execute("""
            CREATE TRIGGER trigger_verificar_prestamos
            BEFORE INSERT ON prestamos
            FOR EACH ROW
            EXECUTE FUNCTION verificar_prestamos();
        """)
        cursor.execute("COMMIT")
        print("Función y trigger creados")
    except Exception as e:
        print(f"Error {e} al crear la función y el trigger")

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
        print("------ FUNCIONES Y TRIGGERS ------")
        print("18.- CREAR FUNCION Y TRIGGER")

        opcion = input("Ingrese una opción: ")
        menu(opcion, cursor)
except Exception as e:
    print(f"Error {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

