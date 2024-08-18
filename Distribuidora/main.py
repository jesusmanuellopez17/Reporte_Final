import tkinter as tk
from tkinter import messagebox,ttk
from modelos import Proveedores, Productos, Ventas, DetallesVentas
from usuarios import Usuarios
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Distribuidora de Equipos Médicos")
        self.geometry("1920x1080")
        self.mostrar_menu_inicio()

    def mostrar_menu_inicio(self):
        self.limpiar_pantalla()
        tk.Label(self, text="..::Sistema de Gestión de Distribuidora de Equipos Médicos::..", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(self, text="Iniciar sesión", command=self.mostrar_login).pack(pady=10)
        tk.Button(self, text="Salir del sistema", command=self.quit).pack(pady=10)

    def mostrar_login(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Inicio de sesión", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Button(self, text="Iniciar sesión", command=self.login).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)

    def login(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        usuario = Usuarios.verificar_credenciales(correo, contrasena)
        if usuario:
            if usuario['rol'] == 'empleado':
                self.mostrar_menu_empleado()
            elif usuario['rol'] == 'cliente':
                self.mostrar_menu_cliente()
        else:
            messagebox.showerror("Error", "Credenciales inválidas.")

    def mostrar_registro(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Registro de Usuario", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Label(self, text="Rol (empleado/cliente):").pack()
        self.rol_entry = tk.Entry(self)
        self.rol_entry.pack(pady=5)
        tk.Button(self, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        rol = self.rol_entry.get()
        nuevo_usuario = Usuarios(nombre, correo, contrasena, rol)
        if nuevo_usuario.crear():
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.mostrar_menu_inicio()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario.")

    def mostrar_menu_empleado(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Menú Empleado", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Gestión de Proveedores", command=self.mostrar_menu_proveedores).pack(pady=10)
        tk.Button(self, text="Gestión de Productos", command=self.mostrar_menu_productos).pack(pady=10)
        tk.Button(self, text="Gestión de Ventas", command=self.mostrar_menu_ventas).pack(pady=10)
        tk.Button(self, text="Gestión de Detalles de Ventas", command=self.mostrar_menu_detalles_ventas).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", command=self.mostrar_menu_inicio).pack(pady=10)

    def mostrar_menu_cliente(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Menú Cliente", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Productos", command=self.ver_productos).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", command=self.mostrar_menu_inicio).pack(pady=10)

    def mostrar_menu_proveedores(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Proveedores", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Proveedores", command=self.ver_proveedores).pack(pady=10)
        tk.Button(self, text="Añadir Proveedor", command=self.anadir_proveedor).pack(pady=10)
        tk.Button(self, text="Actualizar Proveedor", command=self.actualizar_proveedor).pack(pady=10)
        tk.Button(self, text="Eliminar Proveedor", command=self.eliminar_proveedor).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_productos(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Productos", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Productos", command=self.ver_productos).pack(pady=10)
        tk.Button(self, text="Añadir Producto", command=self.anadir_producto).pack(pady=10)
        tk.Button(self, text="Actualizar Producto", command=self.actualizar_producto).pack(pady=10)
        tk.Button(self, text="Eliminar Producto", command=self.eliminar_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_ventas(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Ventas", command=self.ver_ventas).pack(pady=10)
        tk.Button(self, text="Añadir Venta", command=self.anadir_venta).pack(pady=10)
        tk.Button(self, text="Actualizar Venta", command=self.actualizar_venta).pack(pady=10)
        tk.Button(self, text="Eliminar Venta", command=self.eliminar_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_detalles_ventas(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Detalles de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Detalles de Ventas", command=self.ver_detalles_ventas).pack(pady=10)
        tk.Button(self, text="Añadir Detalle de Venta", command=self.anadir_detalle_venta).pack(pady=10)
        tk.Button(self, text="Actualizar Detalle de Venta", command=self.actualizar_detalle_venta).pack(pady=10)
        tk.Button(self, text="Eliminar Detalle de Venta", command=self.eliminar_detalle_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def ver_proveedores(self):
        self.limpiar_pantalla()
        proveedores = Proveedores.obtener_todos()
        tk.Label(self, text="Proveedores", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre Compañía", "Nombre", "Correo", "Teléfono", "Ciudad"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre Compañía", text="Nombre Compañía")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Correo", text="Correo")
        tree.heading("Teléfono", text="Teléfono")
        tree.heading("Ciudad", text="Ciudad")
        tree.pack(expand=True, fill='both')
        for proveedor in proveedores:
            tree.insert("", tk.END, values=(proveedor["id"], proveedor["nombre_compania"], proveedor["nombre"], proveedor["correo"], proveedor["telefono"], proveedor["ciudad"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def ver_productos(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_todos()
        tk.Label(self, text="Productos", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Descripción", "Precio", "ID Proveedor"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Descripción", text="Descripción")
        tree.heading("Precio", text="Precio")
        tree.heading("ID Proveedor", text="ID Proveedor")
        tree.pack(expand=True, fill='both')
        for producto in productos:
            tree.insert("", tk.END, values=(producto["id"], producto["nombre"], producto["descripcion"], producto["precio"], producto["id_proveedor"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_cliente).pack(pady=10)

    def ver_ventas(self):
        self.limpiar_pantalla()
        ventas = Ventas.obtener_todos()
        tk.Label(self, text="Ventas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Fecha", "ID Cliente", "Total"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Fecha", text="Fecha")
        tree.heading("ID Cliente", text="ID Cliente")
        tree.heading("Total", text="Total")
        tree.pack(expand=True, fill='both')
        for venta in ventas:
            tree.insert("", tk.END, values=(venta["id"], venta["fecha"], venta["id_cliente"], venta["total"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def ver_detalles_ventas(self):
        self.limpiar_pantalla()
        detalles = DetallesVentas.obtener_todos()
        tk.Label(self, text="Detalles de Ventas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "ID Venta", "ID Producto", "Cantidad", "Precio Unitario"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("ID Venta", text="ID Venta")
        tree.heading("ID Producto", text="ID Producto")
        tree.heading("Cantidad", text="Cantidad")
        tree.heading("Precio Unitario", text="Precio Unitario")
        tree.pack(expand=True, fill='both')
        for detalle in detalles:
            tree.insert("", tk.END, values=(detalle["id"], detalle["id_venta"], detalle["id_producto"], detalle["cantidad"], detalle["precio_unitario"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def anadir_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre Compañía:").pack()
        self.nombre_compania_entry = tk.Entry(self)
        self.nombre_compania_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.pack(pady=5)
        tk.Label(self, text="Ciudad:").pack()
        self.ciudad_entry = tk.Entry(self)
        self.ciudad_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_proveedor).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def crear_proveedor(self):
        nombre_compania = self.nombre_compania_entry.get()
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        ciudad = self.ciudad_entry.get()
        proveedor = Proveedores(nombre_compania, nombre, correo, telefono, ciudad)
        if proveedor.crear():
            messagebox.showinfo("Éxito", "Proveedor añadido correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo añadir el proveedor.")

    def anadir_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Descripción:").pack()
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def crear_producto(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        id_proveedor = int(self.id_proveedor_entry.get())
        producto = Productos(nombre, descripcion, precio, id_proveedor)
        if producto.crear():
            messagebox.showinfo("Éxito", "Producto añadido correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo añadir el producto.")

    def anadir_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Fecha:").pack()
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.pack(pady=5)
        tk.Label(self, text="ID Cliente:").pack()
        self.id_cliente_entry = tk.Entry(self)
        self.id_cliente_entry.pack(pady=5)
        tk.Label(self, text="Total:").pack()
        self.total_entry = tk.Entry(self)
        self.total_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_ventas).pack(pady=10)

    def crear_venta(self):
        fecha = self.fecha_entry.get()
        id_cliente = int(self.id_cliente_entry.get())
        total = float(self.total_entry.get())
        venta = Ventas(fecha, id_cliente, total)
        if venta.crear():
            messagebox.showinfo("Éxito", "Venta añadida correctamente.")
            self.mostrar_menu_ventas()
        else:
            messagebox.showerror("Error", "No se pudo añadir la venta.")

    def anadir_detalle_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Detalle de Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Venta:").pack()
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.pack(pady=5)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Label(self, text="Cantidad:").pack()
        self.cantidad_entry = tk.Entry(self)
        self.cantidad_entry.pack(pady=5)
        tk.Label(self, text="Precio Unitario:").pack()
        self.precio_unitario_entry = tk.Entry(self)
        self.precio_unitario_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_detalle_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_detalles_ventas).pack(pady=10)

    def crear_detalle_venta(self):
        id_venta = int(self.id_venta_entry.get())
        id_producto = int(self.id_producto_entry.get())
        cantidad = int(self.cantidad_entry.get())
        precio_unitario = float(self.precio_unitario_entry.get())
        detalle = DetallesVentas(id_venta, id_producto, cantidad, precio_unitario)
        if detalle.crear():
            messagebox.showinfo("Éxito", "Detalle de venta añadido correctamente.")
            self.mostrar_menu_detalles_ventas()
        else:
            messagebox.showerror("Error", "No se pudo añadir el detalle de venta.")

    def actualizar_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Label(self, text="Nombre Compañía:").pack()
        self.nombre_compania_entry = tk.Entry(self)
        self.nombre_compania_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.pack(pady=5)
        tk.Label(self, text="Ciudad:").pack()
        self.ciudad_entry = tk.Entry(self)
        self.ciudad_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_proveedor_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def actualizar_proveedor_db(self):
        id_proveedor = int(self.id_proveedor_entry.get())
        nombre_compania = self.nombre_compania_entry.get()
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        ciudad = self.ciudad_entry.get()
        proveedor = Proveedores(nombre_compania, nombre, correo, telefono, ciudad)
        if proveedor.actualizar(id_proveedor):
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el proveedor.")

    def actualizar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Descripción:").pack()
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def actualizar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        id_proveedor = int(self.id_proveedor_entry.get())
        producto = Productos(nombre, descripcion, precio, id_proveedor)
        if producto.actualizar(id_producto):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto.")

    def actualizar_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Venta:").pack()
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.pack(pady=5)
        tk.Label(self, text="Fecha:").pack()
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.pack(pady=5)
        tk.Label(self, text="ID Cliente:").pack()
        self.id_cliente_entry = tk.Entry(self)
        self.id_cliente_entry.pack(pady=5)
        tk.Label(self, text="Total:").pack()
        self.total_entry = tk.Entry(self)
        self.total_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_venta_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_ventas).pack(pady=10)

    def actualizar_venta_db(self):
        id_venta = int(self.id_venta_entry.get())
        fecha = self.fecha_entry.get()
        id_cliente = int(self.id_cliente_entry.get())
        total = float(self.total_entry.get())
        venta = Ventas(fecha, id_cliente, total)
        if venta.actualizar(id_venta):
            messagebox.showinfo("Éxito", "Venta actualizada correctamente.")
            self.mostrar_menu_ventas()
        else:
            messagebox.showerror("Error", "No se pudo actualizar la venta.")

    def actualizar_detalle_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Detalle de Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Detalle:").pack()
        self.id_detalle_entry = tk.Entry(self)
        self.id_detalle_entry.pack(pady=5)
        tk.Label(self, text="ID Venta:").pack()
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.pack(pady=5)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Label(self, text="Cantidad:").pack()
        self.cantidad_entry = tk.Entry(self)
        self.cantidad_entry.pack(pady=5)
        tk.Label(self, text="Precio Unitario:").pack()
        self.precio_unitario_entry = tk.Entry(self)
        self.precio_unitario_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_detalle_venta_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_detalles_ventas).pack(pady=10)

    def actualizar_detalle_venta_db(self):
        id_detalle = int(self.id_detalle_entry.get())
        id_venta = int(self.id_venta_entry.get())
        id_producto = int(self.id_producto_entry.get())
        cantidad = int(self.cantidad_entry.get())
        precio_unitario = float(self.precio_unitario_entry.get())
        detalle = DetallesVentas(id_venta, id_producto, cantidad, precio_unitario)
        if detalle.actualizar(id_detalle):
            messagebox.showinfo("Éxito", "Detalle de venta actualizado correctamente.")
            self.mostrar_menu_detalles_ventas()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el detalle de venta.")

    def eliminar_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_proveedor_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def eliminar_proveedor_db(self):
        id_proveedor = int(self.id_proveedor_entry.get())
        if Proveedores.eliminar(id_proveedor):
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el proveedor.")

    def eliminar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def eliminar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        if Productos.eliminar(id_producto):
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def eliminar_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Venta:").pack()
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_venta_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_ventas).pack(pady=10)

    def eliminar_venta_db(self):
        id_venta = int(self.id_venta_entry.get())
        if Ventas.eliminar(id_venta):
            messagebox.showinfo("Éxito", "Venta eliminada correctamente.")
            self.mostrar_menu_ventas()
        else:
            messagebox.showerror("Error", "No se pudo eliminar la venta.")

    def eliminar_detalle_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Detalle de Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Detalle:").pack()
        self.id_detalle_entry = tk.Entry(self)
        self.id_detalle_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_detalle_venta_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_detalles_ventas).pack(pady=10)

    def eliminar_detalle_venta_db(self):
        id_detalle = int(self.id_detalle_entry.get())
        if DetallesVentas.eliminar(id_detalle):
            messagebox.showinfo("Éxito", "Detalle de venta eliminado correctamente.")
            self.mostrar_menu_detalles_ventas()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el detalle de venta.")

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

# Ejecución de la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
