import mysql.connector


class Usuarios:
    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="distribuidora"
        )

    @staticmethod
    def verificar_credenciales(correo, contrasena):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s"
        cursor.execute(query, (correo, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario

    def __init__(self, nombre, correo, contrasena, rol, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def crear(self):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO usuarios (nombre, correo, contrasena, rol)
            VALUES (%s, %s, %s, %s)
        """
        values = (self.nombre, self.correo, self.contrasena, self.rol)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            UPDATE usuarios
            SET nombre = %s, correo = %s, contrasena = %s, rol = %s
            WHERE id = %s
        """
        values = (self.nombre, self.correo, self.contrasena, self.rol, id_usuario)
        cursor.execute(query, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0

    @staticmethod
    def eliminar(id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0
