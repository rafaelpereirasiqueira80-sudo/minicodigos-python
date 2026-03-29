import pyautogui as py #Botar o nome principal de pyautogui para py
import time

py.sleep(1)
confirmar = py.confirm(text="Deseja entrar no programa", title="", buttons=['Sim', 'Não'])

if confirmar == "Não" :
    print("OK")
else :
    senha = py.password(text="Informe sua senha: ", title="", default="", mask="*")

    print(senha)

    if senha == None :
        print("OK")

    else :
        while senha != "12345678" and senha != None :
            py.alert(text="Errou a senha")
            senha = py.password(text="Informe sua senha: ", title="", default="", mask="*")

        if senha != None :
            py.alert(text="Parabéns, você entrou no programa")