from .libro import Libro
from .usuario import Usuario

class Libreria:
    """Sistema básico de gestión de biblioteca."""
    def __init__(self):
        self.catalogo = []
        self.usuarios = {}


    def agregar_libro(self, titulo, autor, genero):
        """Añade un nuevo libro al catálogo."""
        self.catalogo.append(Libro(titulo, autor, genero))


    def listar_libros_disponibles(self):
        """Devuelve los libros disponibles."""
        return [libro for libro in self.catalogo if libro.disponible]


    def registrar_usuario(self, usuario_id, nombre):
        """Registra un nuevo usuario."""
        self.usuarios[usuario_id] = Usuario(usuario_id, nombre)


    def prestar_libro(self, titulo, usuario_id):
        """Presta un libro disponible a un usuario."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario:
            return False
        for libro in self.catalogo:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                usuario.prestamos.append(libro)
                return True
        return False


    def devolver_libro(self, titulo, usuario_id):
        """Devuelve un libro prestado por el usuario."""
        usuario = self.usuarios.get(usuario_id)
        if not usuario:
            return False
        for libro in usuario.prestamos:
            if libro.titulo == titulo:
                libro.disponible = True
                usuario.prestamos.remove(libro)
                return True
        return False


    def listar_prestamos_usuario(self, usuario_id):
        """Lista los libros prestados a un usuario."""
        usuario = self.usuarios.get(usuario_id)
        return usuario.prestamos if usuario else []