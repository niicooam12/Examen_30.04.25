import random
from gestor_libros.libro import Libro
from gestor_libros.usuario import Usuario

class Libreria:
    """Sistema básico de gestión de biblioteca."""
    def __init__(self):
        self.catalogo = []
        self.usuarios = {}

    def agregar_libro(self, titulo, autor, genero):
        """Añade un nuevo libro al catálogo con disponibilidad aleatoria."""
        disponible = random.choice([True, False])
        self.catalogo.append(Libro(titulo, autor, genero, disponible))

    def listar_libros_disponibles(self):
        """Devuelve los libros disponibles."""
        return [libro for libro in self.catalogo if libro.disponible]

    def registrar_usuario(self, usuario_id, nombre):
        """Registra un nuevo usuario."""
        self.usuarios[usuario_id] = Usuario(usuario_id, nombre)

    def prestar_libro(self, usuario_id, titulo=None):
        """Presta un libro a un usuario. Si se especifica un título, intenta prestar ese libro."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario:
            return False
        
        if titulo:
            libro = next((libro for libro in self.catalogo if libro.titulo == titulo and libro.disponible), None)
            if not libro:
                return False
        else:
            libros_disponibles = self.listar_libros_disponibles()
            if not libros_disponibles:
                return False
            libro = random.choice(libros_disponibles)
        
        libro.disponible = False
        usuario.prestados.append(libro)
        return True

    def devolver_libro(self, usuario_id, titulo=None):
        """Devuelve un libro prestado por el usuario. Si se especifica un título, intenta devolver ese libro."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario or not usuario.prestados:
            return False
        
        if titulo:
            libro = next((libro for libro in usuario.prestados if libro.titulo == titulo), None)
            if not libro:
                return False
        else:
            libro = random.choice(usuario.prestados)
        
        libro.disponible = True
        usuario.prestados.remove(libro)
        return True

    def listar_prestamos_usuario(self, usuario_id):
        """Lista los libros prestados a un usuario."""
        usuario = self.usuarios.get(usuario_id)
        return usuario.prestados if usuario else []
