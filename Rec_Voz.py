import pyttsx3
import speech_recognition as sr

from Rec_Facial import analisisFacial
from Usuario import Usuario
from PIL import Image


def audio_to_text():
	# Recognizer
	r = sr.Recognizer()

	# Configurar el micro
	with sr.Microphone() as origen:
		# Tiempo de espera desde que se activa el micro
		r.pause_threshold = 0.8

		# Informar que comenzó la grabación
		print('Esperando instrucción')

		# Guardar audio
		audio = r.listen(origen)

		try:
			# Buscar en google lo escuchado
			text = r.recognize_google(audio, language='es-es')
			print(text)
			return text
		except sr.UnknownValueError:
			print('No he entendido lo que has dicho, prueba de nuevo')
			return 'Esperando'

		except sr.RequestError:
			print('Ups, sin servicio')
			return 'Esperando'

		except:
			print('Ups, algo ha salido mal')
			return 'Esperando'


def talk(msg):
	# Encender el motor pyttsx3
	engine = pyttsx3.init()
	engine.say(msg)
	engine.runAndWait()
	print(msg)


def print_voices():
	engine = pyttsx3.init()
	for voz in engine.getProperty('voices'):
		print(voz.id, voz)


def RegistroUsuario():
	talk("Acercate a la cámara para comenzar el registro")

	if analisisFacial():
		talk("Bienvenido, puedes avanzar al sistema principal")
	else:
		talk("No haz podido ser identificado, Quieres comenzar con el registro?")
		nuevoUser = audio_to_text().lower()
		if nuevoUser=="si":
			# NuevoUsuario()
			print("Desarrollo")


def NuevoUsuario(frame):
	talk("Vamos a comenzar por proporcionar tu información persona, ¿Cómo te llamas?")
	nombre = audio_to_text().lower()
	talk(f"Encantado de conocerte {nombre}, Ahora dime cual es identificacion")
	id = audio_to_text().lower()
	talk(f"Si Tu identificacion es: {id}, di confirmar?")
	# confirmacion = audio_to_text().lower()
	# print(confirmacion)
	if  "confirmar" in audio_to_text().lower():
		preguntarDenuevo(id)
	talk("Ya casi, dime tu numero teléfonico")
	telefono = audio_to_text().lower()
	talk(f"Tu telefono es: {telefono}, si es correcto di confirmar?")
	confirmacion = audio_to_text()
	if "confirmar" in confirmacion:
		preguntarDenuevo(telefono)
	imagen = nombre + id
	ubicacion = ".\\fotos\\"
	imagen_pil = Image.fromarray(frame)
	imagen_pil.save(ubicacion + nombre.replace(" ", "") + id.replace(" ", "") + ".jpg")
	user = Usuario(nombre, id, telefono, imagen)
	talk(f"Bienvenido {nombre} haz sido registrado con exito")
	return user


def preguntarDenuevo(dato):
	talk(f"Lo lamento, puedes repetir tu {dato} porfavor?")
	id = audio_to_text().lower()
	talk(f"Haz dicho: {dato}, es correcto? si es asi di 'confirmar'")
	confirmacion = audio_to_text().lower()
	if confirmacion=="confirmar":
		return id
	else:
		preguntarDenuevo(dato)


def Consulta():
	stop = False
	while not stop:
		request = audio_to_text().lower()
		if 'iniciar' in request:
			RegistroUsuario()
