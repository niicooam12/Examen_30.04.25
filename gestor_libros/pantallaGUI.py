import tkinter as tk
from gestor_libros.librereria import Libreria
import random

libreria = Libreria()

libreria.agregar_libro('Cien Años de Soledad', 'Gabriel García Márquez', 'Ficción')
libreria.agregar_libro('Breve Historia del Tiempo', 'Stephen Hawking', 'Ciencia')
libreria.registrar_usuario(1, 'Ana Pérez')

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Gestión de Biblioteca")

    etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido a la Biblioteca", font=("Arial", 16))
    etiqueta_bienvenida.pack(pady=10)

    boton_prestamo = tk.Button(ventana, text="Realizar Préstamo", command=realizar_prestamo)
    boton_prestamo.pack(pady=5)

    boton_devolucion = tk.Button(ventana, text="Registrar Devolución", command=registrar_devolucion)
    boton_devolucion.pack(pady=5)

    boton_consulta = tk.Button(ventana, text="Consultar Disponibilidad", command=consultar_disponibilidad)
    boton_consulta.pack(pady=5)

    boton_agregar_libro = tk.Button(ventana, text="Agregar Nuevo Libro", command=agregar_libro)
    boton_agregar_libro.pack(pady=5)

    boton_agregar_usuario = tk.Button(ventana, text="Agregar Nuevo Usuario", command=agregar_usuario)
    boton_agregar_usuario.pack(pady=5)

    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=20)

    ventana.mainloop()

def realizar_prestamo():
    libro_a_prestar = random.choice(['Cien Años de Soledad', 'Breve Historia del Tiempo'])
    exito = libreria.prestar_libro(1, libro_a_prestar)
    print("¿Préstamo exitoso?", exito)
    print("Libros prestados a Ana:", [libro.titulo for libro in libreria.listar_prestamos_usuario(1)])

def registrar_devolucion():
    libro_a_devolver = random.choice(['Cien Años de Soledad', 'Breve Historia del Tiempo'])
    exito = libreria.devolver_libro(1, libro_a_devolver)
    print("¿Devolución exitosa?", exito)
    print("Libros disponibles:", [libro.titulo for libro in libreria.listar_libros_disponibles()])

def consultar_disponibilidad():
    disponibles = [libro.titulo for libro in libreria.listar_libros_disponibles()]
    print("Libros disponibles:", disponibles)

def agregar_libro():
    # Example: Add a new book (this can be extended to take user input via Tkinter)
    libreria.agregar_libro('Nuevo Libro', 'Autor Desconocido', 'Género')
    print("Libro agregado exitosamente.")

def agregar_usuario():
    # Example: Add a new user (this can be extended to take user input via Tkinter)
    libreria.registrar_usuario(2, 'Juan López')
    print("Usuario agregado exitosamente.")