from views.vista_principal import VistaPrincipal
from models.local import Local
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = VistaPrincipal(root, self.seleccionar_local, seleccionar_ubicacion)
        self.locales = Local.cargar_locales("app/data/locales.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.marcadores = []
        self.imagenes = []

        self.cargar_locales()
        self.cargar_imagenes()
        self.cargar_marcadores()
        
    def cargar_locales(self):
        for local in self.locales:
            self.vista.agregar_local(local)
        
    def cargar_imagenes(self):
        for local in self.locales:
            imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{local.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, local in zip(self.ubicaciones, self.locales):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, local.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_local(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_locales.curselection()
        # Obtiene el local seleccionado
        local_seleccionado = self.locales[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al local seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == local_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)