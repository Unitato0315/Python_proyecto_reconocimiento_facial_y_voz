import pyttsx3
import speech_recognition as sr

from Rec_Facial import analisisFacial
from Usuario import Usuario


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


def print_voices():
	engine = pyttsx3.init()
	for voz in engine.getProperty('voices'):
		print(voz.id, voz)

def RegistroUsuario():
	talk("Acercate a la cámara para comenzar el registro")
	confirmacion = analisisFacial();
	if confirmacion:
		talk("Bienvenido, puedes avanzar al sistema principal")
	else:
		talk("No haz podido ser identificado, Quieres comenzar con el registro?")


def NuevoUsuario():
	talk("Vamos a comenzar por proporcionar tu información persona, ¿Cómo te llamas?")
	nombre = audio_to_text().lower()
	talk(f"Encantado de conocerte {nombre}, Ahora dime cual es identificacion")
	id= audio_to_text().lower()
	talk(f"Tu identificacion es: {id}, es correcto?")
	confirmacion = audio_to_text().lower()
	if confirmacion != "si":
		preguntarDenuevo(id)
	talk("Ya casi, dime tu numero telefonico")
	telefono = audio_to_text().lower
	talk(f"Tu telefono es: {telefono}, es correcto?")
	confirmacion = audio_to_text()
	if confirmacion != "si":
		preguntarDenuevo()
	user = Usuario(nombre,id,telefono)

def preguntarDenuevo(dato):
	talk("Lo lamento, puedes repetirlo porfavor?")
	id = audio_to_text().lower()
	talk(f"Dijiste: {dato}, es correcto?")
	confirmacion = audio_to_text().lower()
	if confirmacion == "si":
		return True
	else:
		confirmacion(dato)

def Consulta():
	stop = False
	while not stop:
		request = audio_to_text().lower()
		if 'Iniciar' in request:
			RegistroUsuario()

