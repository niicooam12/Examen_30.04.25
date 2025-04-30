import random
from gestor_libros.librereria import Libreria

if __name__ == '__main__':
    biblioteca = Libreria()

    biblioteca.agregar_libro('Cien Años de Soledad', 'Gabriel García Márquez', 'Ficción')
    biblioteca.agregar_libro('Breve Historia del Tiempo', 'Stephen Hawking', 'Ciencia')
    
    biblioteca.registrar_usuario(1, 'Ana Pérez')

    libro_a_prestar = random.choice(['Cien Años de Soledad', 'Breve Historia del Tiempo'])
    print("¿Préstamo exitoso?", biblioteca.prestar_libro(libro_a_prestar, 1))
    print("Libros prestados a Ana:", [libro.titulo for libro in biblioteca.listar_prestamos_usuario(1)])

    print("¿Devolución exitosa?", biblioteca.devolver_libro(libro_a_prestar, 1))
    print("Libros disponibles:", [libro.titulo for libro in biblioteca.listar_libros_disponibles()])