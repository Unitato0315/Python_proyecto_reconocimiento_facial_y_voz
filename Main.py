from Rec_Voz import Consulta
from Rec_Facial import *

#Consulta()

existe = analisisFacial()

if existe:
    print("Se ha encotrado en los registros")
else:
    print("No se ha encotrado en los registros")

#prueba = obtenerFotos()
#obtenerCamara("prueba", len(prueba))
