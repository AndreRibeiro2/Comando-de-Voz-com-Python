import speech_recognition as sr
import webbrowser
import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #Usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo para redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase - O Usuário deve falar algo
        print("Qual app você deseja abrir? Excel, Navegador, PowerPoint ou Word? ")
        #Armazena o que foi dito dentro de uma variável
        audio = microfone.listen(source)

    try:
        #Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "Navegador" in frase:
            os.startfile("start c:\Program Files\Google\Chrome\Application\chrome.exe")  # Altere para o site desejado
            return False

        if "Excel" in frase:
            os.startfile("start c:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")  # Altere o caminho se necessário
            return False

        if "Word" in frase:
            os.startfile("C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE")  # Altere o caminho se necessário
            return False

        if "PowerPoint" in frase:
            os.startfile("start c:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")  # Altere o caminho se necessário
            return False

        elif "Fechar" in frase:
            return True

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se não reconheceu o padrão de fala, exibe a mensagem:
    except sr.UnknownValueError:
        print("Não consegui entender :( ")

    return frase

while True:
    if ouvir_microfone():
        break