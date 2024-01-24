import os

import cv2
import face_recognition as fr
from PIL import Image



def analisisFacial():
    existe = False
    rutafotos = obtenerFotos()
    frame = obtenerCamara()
    fotos = cargar_imagenes(rutafotos)
    fotos = asignar_perfil_color(fotos)
    fotos.append(frame)
    cod_faces = get_cod_faces(fotos)
    results = compare_all_with_control(cod_faces)
    show_results(results)

    for r in results:
        if r[0]:
            existe = True

    if not existe:
        ubicacion = ".\\fotos\\"
        imagen_pil = Image.fromarray(frame)
        imagen_pil.save(ubicacion + "prueba" + str(len(fotos)) + ".jpg")
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
    for foto in fotos:
        print(foto)
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
            # Con fr.compare_faces([control_cod], cara_cod_comparar, 0.3) podemos modificar el límite por el que determinaría si es true
            results.append(fr.compare_faces([cara_cod_list[len(cara_cod_list) - 1]], fc))
    return results


def show_results(results):
    for r in results:
        print(r)


def obtenerCamara():
    captura = cv2.VideoCapture(0)
    print("Pulsa la letra l para hacer la captura")
    while True:
        ok, frame = captura.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('l'):
            break

    captura.release()
    cv2.destroyAllWindows()

    if not ok:
        print('No se a podido recoger la imagen')
    else:
        cv2.imshow('frame', frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
