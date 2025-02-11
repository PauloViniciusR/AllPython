import pyautogui
import time

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (crtl c)

# Passo 1: Abrir sistema   

pyautogui.PAUSE = 0.5

#Apertar tecla win
pyautogui.press('win')

#Digitar chrome
pyautogui.write('edge')

#Apertar tecla
pyautogui.press('enter')

#pyautogui.click(x=772, y=350)


#Entrar link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')

time.sleep(2)

# Passo 2: Fazer login

pyautogui.click(x=621, y=366)

pyautogui.write('thedevelopervini@gmail.com')

pyautogui.press('tab') 
pyautogui.write('senha123')

pyautogui.press('tab') 
pyautogui.press('enter')

# Passo 3: Importar base de dados

import pandas 

tabela = pandas.read_csv('produtos.csv')

print(tabela)

time.sleep(2)

# Passos 3: Cadastrar 1 produto

for linha in tabela.index:

    pyautogui.click(x=735, y=238)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')


    obs = str(tabela.loc[linha, 'obs'])
    
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')

    # numero positivo para cima
    pyautogui.scroll(10000)