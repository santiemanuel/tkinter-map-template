import json

class Local:
    def __init__(self, nombre, imagen, id_ubicacion,tipo_cocina,id_local, ingredientes, precio_max, precio_min, disponibilidad):
        self.nombre = nombre
        self.imagen = imagen
        self.id_ubicacion = id_ubicacion
        self.tipo_cocina = tipo_cocina
        self.id_local = id_local
        self.ingredientes = ingredientes
        self.precio_max = precio_max
        self.precio_min = precio_min
        self.disponibilidad = disponibilidad



    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_locales(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Local.de_json(json.dumps(dato)) for dato in datos]