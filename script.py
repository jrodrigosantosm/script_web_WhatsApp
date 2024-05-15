import pandas as pd
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

contatos_df = pd.read_excel("contatos.xlsx")
chrome_driver_path = "C:/Users/rodri/anaconda3/chromedriver.exe"

servico = Service(chrome_driver_path)
navegador = webdriver.Chrome(service=servico)
navegador.get("https://web.whatsapp.com/")
time.sleep(30)

elemento_pesquisa = navegador.find_element(By.XPATH, "//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']")

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    time.sleep(20)
    in_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    in_mensagem.send_keys(Keys.ENTER)
    time.sleep(3)
    print("Texto enviado")
print("Todas as mensagens enviadas!")

while True:
    pass
