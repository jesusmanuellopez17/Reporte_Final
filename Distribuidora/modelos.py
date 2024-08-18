from ConexionBd import ConexionBd


class Proveedores:
    def __init__(self, nombre_compania, nombre, correo, telefono, ciudad, id=None):
        self.id = id
        self.nombre_compania = nombre_compania
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.ciudad = ciudad

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        conexion.close()
        return proveedores

    @staticmethod
    def obtener_por_id(id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id_proveedor,))
        proveedor = cursor.fetchone()
        cursor.close()
        conexion.close()
        return proveedor

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO proveedores (nombre_compania, nombre, correo, telefono, ciudad)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE proveedores
                SET nombre_compania = %s, nombre = %s, correo = %s, telefono = %s, ciudad = %s
                WHERE id = %s
            """
            values = (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad, id_proveedor)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM proveedores WHERE id = %s"
            cursor.execute(query, (id_proveedor,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

class Productos:
    def __init__(self, nombre, descripcion, precio, id_proveedor, id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_proveedor = id_proveedor

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos

    @staticmethod
    def obtener_por_id(id_producto):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        conexion.close()
        return producto

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO productos (nombre, descripcion, precio, id_proveedor)
            VALUES (%s, %s, %s, %s)
        """
        values = (self.nombre, self.descripcion, self.precio, self.id_proveedor)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_producto):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE productos
                SET nombre = %s, descripcion = %s, precio = %s, id_proveedor = %s
                WHERE id = %s
            """
            values = (self.nombre, self.descripcion, self.precio, self.id_proveedor, id_producto)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM productos WHERE id = %s"
            cursor.execute(query, (id_producto,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
            
class Ventas:
    def __init__(self, fecha, id_cliente, total, id=None):
        self.id = id
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.total = total

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return ventas

    @staticmethod
    def obtener_por_id(id_venta):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ventas WHERE id = %s", (id_venta,))
        venta = cursor.fetchone()
        cursor.close()
        conexion.close()
        return venta

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO ventas (fecha, id_cliente, total)
            VALUES (%s, %s, %s)
        """
        values = (self.fecha, self.id_cliente, self.total)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_venta):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE ventas
                SET fecha = %s, id_cliente = %s, total = %s
                WHERE id = %s
            """
            values = (self.fecha, self.id_cliente, self.total, id_venta)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_venta):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM ventas WHERE id = %s"
            cursor.execute(query, (id_venta,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
            
class DetallesVentas:
    def __init__(self, id_venta, id_producto, cantidad, precio_unitario, id=None):
        self.id = id
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_ventas")
        detalles = cursor.fetchall()
        cursor.close()
        conexion.close()
        return detalles

    @staticmethod
    def obtener_por_id(id_detalle):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_ventas WHERE id = %s", (id_detalle,))
        detalle = cursor.fetchone()
        cursor.close()
        conexion.close()
        return detalle

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO detalles_ventas (id_venta, id_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, %s)
        """
        values = (self.id_venta, self.id_producto, self.cantidad, self.precio_unitario)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_detalle):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE detalles_ventas
                SET id_venta = %s, id_producto = %s, cantidad = %s, precio_unitario = %s
                WHERE id = %s
            """
            values = (self.id_venta, self.id_producto, self.cantidad, self.precio_unitario, id_detalle)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_detalle):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM detalles_ventas WHERE id = %s"
            cursor.execute(query, (id_detalle,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()