class Usuario(object):
    def __init__(self, nombre, id, telefono, imagen):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.imagen = imagen

    def __dict__(self):
        usuarios = {

            "nombre": self.nombre,
            "id": self.id,
            "telefono": self.telefono,
            "imagen": self.imagen
        }
        return usuarios
    def __str__(self):
        return "Nombre: " + self.nombre + "\nID: " + self.id + "\nTelefono: " + self.telefono

    def  from_dict(dictionary):
        return Usuario(dictionary['nombre'], dictionary['id'], dictionary['telefono'], dictionary['imagen'])
