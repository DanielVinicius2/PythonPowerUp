import pyautogui
import time
import pandas as pd
# pyautogui.click -> clica em qualquer lugar
# pyautogui.press -> aperta uma tecla
# pyautogui.write -> Escrever um texto
# pyautogui.hotkey -> Executa um comando

pyautogui.PAUSE = 1

#1 Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")
pyautogui.write("Brave")
pyautogui.press("enter")
# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#2 Fazer o login
time.sleep(3)
pyautogui.click(x=829, y=462)
pyautogui.write("daniel.mille34@gmail.com")

time.sleep(1)
pyautogui.press("tab")
pyautogui.write("futebol3")

pyautogui.press("tab")
pyautogui.press("enter")
#3 Importar a base de dados
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

print(tabela)
#4 Cadastrar um produto
time.sleep(3) 
for linha in tabela.index:
    pyautogui.click(x=838, y=315)

    #Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #Preço Unitario
    preco_unit =  tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unit))
    pyautogui.press("tab")
    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #Observações
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)
#5 Repetir para todos os produtos


# pyautogui -> fazer automações com python