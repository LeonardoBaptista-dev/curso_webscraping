# instalar selenium
# instalar webdriver_manager

from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.google.com")

# importar base de dados

'''tabela = pd.read_excel('planilha de dados/commodities.xlsx')
print(tabela)'''

# pegar preço cotação de cada produto



