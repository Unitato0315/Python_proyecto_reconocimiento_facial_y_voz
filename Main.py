import json
import os

import Rec_Voz
from Rec_Facial import *
from Usuario import Usuario


# Consulta()
#

def save_json(lista_usuarios, name_fich):
    dict_film = []
    for u in lista_usuarios:
        dict_film.append(u.__dict__())

    resul = {'Usuarios': dict_film}
    with open(name_fich, "w") as file:
        json.dump(resul, file)


# Se encarga de leer un fichero JSON
def reader_json(name_fich):
    lista_usuarios = []
    with open(name_fich, "r") as archivo:
        reader = json.load(archivo)
    if len(reader) == 1:
        for u in reader['Usuarios']:
            lista_usuarios.append(Usuario.from_dict(u))  # Llama al metodo que tranforma un diccionario en un objeto
    return lista_usuarios


ubicacion = ".\\usuarios\\usuarios.json"

if os.path.exists(ubicacion):
    listaUsuario = reader_json(ubicacion)
else:
    listaUsuario = []


while True:
    Rec_Voz.talk("Para comenzar con el reconocimiento di: iniciar")
    start =Rec_Voz.audio_to_text().lower()
    if "iniciar" in start:
        Rec_Voz.talk("Iniciando el reconocimiento facial")
        existe = analisisFacial()
        if existe[0]:
            Rec_Voz.talk("Bienvenido")
            for u in listaUsuario:
                if u.imagen == existe[1]:
                    u.__str__()
                    Rec_Voz.talk("Bienvenido "+u.nombre)
            Rec_Voz.Consulta()
        else:
            Rec_Voz.talk("No se ha encontrado en los registros")
            listaUsuario.append(Rec_Voz.NuevoUsuario(existe[1]))
            save_json(listaUsuario, ubicacion)
            print("Usuario Registrado")
            Rec_Voz.Consulta()
    elif "salir" in start:
        exit()
# Rec_Voz.NuevoUsuario()
# prueba = obtenerFotos()
# obtenerCamara("prueba", len(prueba))
