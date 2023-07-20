import json

class Ubicacion:
    def __init__(self, id, latitud, longitud, direccion):
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_ubicaciones(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]