import Rec_Voz
from Rec_Facial import *

# Consulta()
#
existe = analisisFacial()

if existe:
    Rec_Voz.talk("Bienvenido")
    print("Se ha encotrado en los registros")
else:
    Rec_Voz.talk("No se ha encontrado en los registros")
    Rec_Voz.NuevoUsuario()
    print("No se ha encontrado en los registros")
# Rec_Voz.NuevoUsuario()
# prueba = obtenerFotos()
# obtenerCamara("prueba", len(prueba))
