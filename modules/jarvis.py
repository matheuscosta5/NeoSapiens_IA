import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def falar(texto):
    print("Jarvis:", texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language='pt-BR')
            print("Você disse:", comando)
            return comando.lower()
        except sr.UnknownValueError:
            falar("Desculpe, não entendi.")
            return ""
        except sr.RequestError:
            falar("Erro na conexão com o serviço de reconhecimento.")
            return ""

def responder(comando):
    if "bom dia" in comando:
        falar("Bom dia, senhor. Pronto para mais um dia de revolução?")
    elif "horas" in comando:
        agora = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "toca música" in comando or "coloca música" in comando:
        falar("Qual música você quer ouvir?")
        # Aqui conectaremos à API depois
    elif "sair" in comando:
        falar("Encerrando. Até logo.")
        exit()
    else:
        falar("Ainda estou aprendendo, mas posso tentar te ajudar com isso.")

def iniciar_jarvis():
    falar("Bom dia, chefe. A revolução começou.")
    while True:
        comando = ouvir_comando()
        if comando:
            responder(comando)
