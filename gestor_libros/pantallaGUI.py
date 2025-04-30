import tkinter as tk
import tkinter.ttk as ttk
from gestor_libros.librereria import Libreria
import random
from tkinter import messagebox

libreria = Libreria()

libreria.agregar_libro('Cien Años de Soledad', 'Gabriel García Márquez', 'Ficción')
libreria.agregar_libro('Breve Historia del Tiempo', 'Stephen Hawking', 'Ciencia')
libreria.registrar_usuario(1, 'Ana Pérez')

# Modernize the interface using ttk widgets and styles
def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Gestión de Biblioteca")
    ventana.geometry("600x400")  # Set a modern window size

    style = ttk.Style()
    style.theme_use("clam")  # Use a modern theme

    etiqueta_bienvenida = ttk.Label(ventana, text="Bienvenido a la Biblioteca", font=("Arial", 16))
    etiqueta_bienvenida.pack(pady=10)

    boton_prestamo = ttk.Button(ventana, text="Realizar Préstamo", command=realizar_prestamo)
    boton_prestamo.pack(pady=5)

    boton_devolucion = ttk.Button(ventana, text="Registrar Devolución", command=registrar_devolucion)
    boton_devolucion.pack(pady=5)

    boton_consulta = ttk.Button(ventana, text="Consultar Disponibilidad", command=consultar_disponibilidad)
    boton_consulta.pack(pady=5)

    boton_agregar_libro = ttk.Button(ventana, text="Agregar Nuevo Libro", command=agregar_libro)
    boton_agregar_libro.pack(pady=5)

    boton_agregar_usuario = ttk.Button(ventana, text="Agregar Nuevo Usuario", command=agregar_usuario)
    boton_agregar_usuario.pack(pady=5)

    boton_salir = ttk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=20)

    ventana.mainloop()

# Updated realizar_prestamo to select a random user and book, and display the result in the same window
def realizar_prestamo():
    usuarios = libreria.listar_usuarios()
    libros_disponibles = libreria.listar_libros_disponibles()

    if not usuarios or not libros_disponibles:
        messagebox.showinfo("Error", "No hay usuarios o libros disponibles para realizar un préstamo.")
        return

    usuario = random.choice(usuarios)
    libro = random.choice(libros_disponibles)

    exito = libreria.prestar_libro(usuario.id_usuario, libro.titulo)
    if exito:
        messagebox.showinfo("Préstamo Exitoso", f"{usuario.nombre} ha cogido el libro '{libro.titulo}'.")
    else:
        messagebox.showinfo("Error", "No se pudo realizar el préstamo.")

# Updated registrar_devolucion to return a book and display the result in the same window
def registrar_devolucion():
    usuarios = libreria.listar_usuarios()
    prestamos = [libro for usuario in usuarios for libro in libreria.listar_prestamos_usuario(usuario.id_usuario)]

    if not prestamos:
        messagebox.showinfo("Error", "No hay libros prestados para devolver.")
        return

    libro = random.choice(prestamos)
    usuario = next(u for u in usuarios if libro in libreria.listar_prestamos_usuario(u.id_usuario))

    exito = libreria.devolver_libro(usuario.id_usuario, libro.titulo)
    if exito:
        messagebox.showinfo("Devolución Exitosa", f"{usuario.nombre} ha devuelto el libro '{libro.titulo}'.")
    else:
        messagebox.showinfo("Error", "No se pudo realizar la devolución.")

# Updated consultar_disponibilidad to display available books in a messagebox
def consultar_disponibilidad():
    disponibles = [libro.titulo for libro in libreria.listar_libros_disponibles()]
    if disponibles:
        messagebox.showinfo("Libros Disponibles", f"Libros disponibles: {', '.join(disponibles)}")
    else:
        messagebox.showinfo("Libros Disponibles", "No hay libros disponibles.")

# Updated agregar_libro to open a new window for user input
def agregar_libro():
    def guardar_libro():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        if titulo and autor:
            libreria.agregar_libro(titulo, autor, None)  # Removed genre
            messagebox.showinfo("Éxito", "Libro agregado exitosamente.")
            ventana_nueva.destroy()
        else:
            messagebox.showinfo("Error", "Todos los campos son obligatorios.")

    ventana_nueva = tk.Toplevel()
    ventana_nueva.title("Agregar Nuevo Libro")

    ttk.Label(ventana_nueva, text="Título:").pack()
    entry_titulo = ttk.Entry(ventana_nueva)
    entry_titulo.pack()

    ttk.Label(ventana_nueva, text="Autor:").pack()
    entry_autor = ttk.Entry(ventana_nueva)
    entry_autor.pack()

    ttk.Button(ventana_nueva, text="Guardar", command=guardar_libro).pack()

# Updated agregar_usuario to open a new window for user input
def agregar_usuario():
    def guardar_usuario():
        nombre = entry_nombre.get()
        if nombre:
            nuevo_id = max([usuario.id_usuario for usuario in libreria.listar_usuarios()] + [0]) + 1
            libreria.registrar_usuario(nuevo_id, nombre)
            messagebox.showinfo("Éxito", "Usuario agregado exitosamente.")
            ventana_nueva.destroy()
        else:
            messagebox.showinfo("Error", "El nombre es obligatorio.")

    ventana_nueva = tk.Toplevel()
    ventana_nueva.title("Agregar Nuevo Usuario")

    ttk.Label(ventana_nueva, text="Nombre:").pack()
    entry_nombre = ttk.Entry(ventana_nueva)
    entry_nombre.pack()

    ttk.Button(ventana_nueva, text="Guardar", command=guardar_usuario).pack()