# 1 - LISTA DE NÚMEROS
# 2 - ENVIAR INDIVIDUALMENTE UMA MENSAGEM PARA CADA PESSOA
# 3 - PAUSAR ENTRE CADA ENVIO 

# 1 - ESCOLHER UM CONTATO
# 2- ENVIAR MENSAGEM PARA ESSE CONTATO
# 	https://api.whatsapp.com/send?phone=5577988291674
# 3 - REPETIR PARA OUTROS CONTATOS
import webbrowser
import pyautogui
from time import sleep

telefones = [5577988291674, 5577988277482, 557799869938]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1562, 228, duration=1)
    sleep(10)
    pyautogui.typewrite('Essa mensagem é de envio de um bot feito por Junior usando python')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)
