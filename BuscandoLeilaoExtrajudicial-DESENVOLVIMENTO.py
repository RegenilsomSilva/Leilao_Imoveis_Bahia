
# COMO CRIAR UM AMBIENTE VIRTUAL
# https://www.youtube.com/watch?v=m1TYpvIYm74&ab_channel=Ot%C3%A1vioMiranda
# python -m venv meu_ambiente_virtual
# Ative o Ambiente Virtual = meu_ambiente_virtual\Scripts\activate
# ip install -r requirements.txt.
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import time
import os

class DescontoImoveis:
    def __init__(self):

        eder_options = Options()
        eder_options.add_argument('--lang=pt-BR')
        eder_options.add_argument('--disable-notifications')
        eder_options.add_argument('--ignore-ssl-erros')

        self.webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=eder_options)
        self.wait      =WebDriverWait(
            driver=self.webdriver,
            timeout=10,
            poll_frequency=1
        )
        
    def Inicio(self):
        self.webdriver.maximize_window()
        primeira_pagina='https://www.leilaoimovel.com.br/encontre-seu-imovel?s=&tipo=1&cidade=2927408&pag=1'   
        pyautogui.scroll(-500)
        self.webdriver.get(primeira_pagina)
        self.Endereco_Do_imovel()


   
    def Endereco_Do_imovel(self):
        # time.sleep(10)
        print(os.linesep)
        print(f'🏘️ Iremos encontra o Endereço do Imóvel 🏘️')
        Bairro_e_Endereco = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="address"]')
            )
        )
        if Bairro_e_Endereco is not None:
            print(os.linesep)
            print(f' 👏Encontramos o Bairro e Endereço do Anuncio do Leilão 👏')
        
        
        Valor_Do_Anuncio = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="prices"]')
            )
        )
        if Valor_Do_Anuncio is not None:
            print(f'👏 Encontramos os Valores do anuncio também.......👏')

        Pocentagem_de_Desconto_Imovel = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//span[@class="down"]')
            )
        )
        if Pocentagem_de_Desconto_Imovel is not None:
            print(os.linesep)
            print(f'👏 Encontramos o desconto deste Imóvel também.......👏')

        Este_imovel_aceita_Qual_Recurso = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="categories"]')
            )
        )
        if Este_imovel_aceita_Qual_Recurso is not None:
            print(os.linesep)
            print(f'👏 Este Imóvel aceita Qual Finaciamento ?=->|FGTS|->|VENDA DIRETA|->|VENDA ONLINE CAIXA|->|FINANCIAMENTO|.👏')

        Data_do_Encerramento_Do_Leilao = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="tag"]')
            )
        )
        if Data_do_Encerramento_Do_Leilao is not None:
            print(os.linesep)
            print(f'👏 Encontramos a Data do Encerramento do Leilão esta informação tem quer ir ao banco de Dados.......👏')
        # Botao_Para_Ir_Ao_Proximo

        # Botao_Para_Ir_Ao_Proximo = self.wait.until(
        #     expected_conditions.presence_of_all_elements_located(
        #         (By.XPATH,'//button[@class="button borderd round"]')
        #     )
        # )    



         




Abertura = DescontoImoveis()
Abertura.Inicio() 
time.sleep(60) 


