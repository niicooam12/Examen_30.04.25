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

    def prestar_libro(self, usuario_id):
        """Presta un libro aleatorio disponible a un usuario."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario:
            return False
        libros_disponibles = self.listar_libros_disponibles()
        if not libros_disponibles:
            return False
        libro = random.choice(libros_disponibles)
        libro.disponible = False
        usuario.prestados.append(libro)
        return True

    def devolver_libro(self, usuario_id):
        """Devuelve un libro aleatorio prestado por el usuario."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario or not usuario.prestados:
            return False
        libro = random.choice(usuario.prestados)
        libro.disponible = True
        usuario.prestados.remove(libro)
        return True

    def listar_prestamos_usuario(self, usuario_id):
        """Lista los libros prestados a un usuario."""
        usuario = self.usuarios.get(usuario_id)
        return usuario.prestados if usuario else []
