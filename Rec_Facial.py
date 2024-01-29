import os

import cv2
import face_recognition as fr
from PIL import Image

from Rec_Voz import talk


def analisisFacial():
    existe = False
    rutafotos = obtenerFotos()
    frame = obtenerCamara()
    fotos = cargar_imagenes(rutafotos)
    fotos = asignar_perfil_color(fotos)
    fotos.append(frame)
    cod_faces = get_cod_faces(fotos)
    results = compare_all_with_control(cod_faces)
    i = 0
    for r in results:
        if r[0]:
            existe = [True, rutafotos[i].split('.')[1].split('\\')[2]]
        i = +1

    if not existe:
        existe = [False, frame]
    return existe


def cargar_imagenes(path_list):
    # La primera será una foto de control, el resto de pruebas
    fotos = []
    for path in path_list:
        fotos.append(fr.load_image_file(path))
    return fotos


def asignar_perfil_color(fotos_list):
    for i in range(len(fotos_list)):
        fotos_list[i] = cv2.cvtColor(fotos_list[i], cv2.COLOR_BGR2RGB)
    return fotos_list


def obtenerFotos():
    ubicacion = ".\\fotos\\"
    archivos = os.listdir(ubicacion)
    fotos = [os.path.join(ubicacion, archivo) for archivo in archivos]
    return fotos


def localizar_cara(fotos_list):
    locations = []
    for i in fotos_list:
        locations.append(fr.face_locations(i)[0])
    return locations


def get_cod_faces(fotos_list):
    cod_faces = []
    for i in fotos_list:
        cod_faces.append(fr.face_encodings(i)[0])
    return cod_faces


def compare_all_with_control(cara_cod_list):
    results = []
    for i, fc in enumerate(cara_cod_list):
        if i != len(cara_cod_list) - 1:
            results.append(fr.compare_faces([cara_cod_list[len(cara_cod_list) - 1]], fc))
    return results


def obtenerCamara():
    captura = cv2.VideoCapture(0)
    ok, frame = captura.read()
    captura.release()
    cv2.destroyAllWindows()
    if not ok:
        talk('No se a podido recoger la imagen')
    else:
        cv2.imshow('frame', frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.destroyAllWindows()
        return frame
