import tkinter as tk
from controller.controlador_principal import ControladorPrincipal

root = tk.Tk()
root.title("Locales en la Zona")
controlador = ControladorPrincipal(root)
root.mainloop()
