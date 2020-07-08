class Contacto:

    def __init__(self, info):
        if isinstance(info, str):
            self.nombre = info
            self.empresa = ""
            self.correo = ""
            self.telefono = ""
            self.nota = ""
        elif isinstance(info, dict):
            self.nombre = info['nombre']
            self.empresa = info['empresa']
            self.correo = info['correo']
            self.telefono = info['telefono']
            self.nota = info['nota']
        else:
            raise TypeError

    def obtenerDatos(self):
        return self.__dict__
