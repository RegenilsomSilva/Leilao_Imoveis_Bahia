# COMO CRIAR UM AMBIENTE VIRTUAL
# https://www.youtube.com/watch?v=m1TYpvIYm74&ab_channel=Ot%C3%A1vioMiranda
# python -m venv env
            #  DESBLOQUEAR POLITICA DE SEGURANÇA NO POWESHELL
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# Ative o Ambiente Virtual = .\env\Scripts\activate.ps1
# pip install webdriver-manager
# ip install -r requirements.txt.
# python -m pip install --upgrade  pip
# antivando o Ambiente :
# .\Scripts\Activate.ps1
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
from docx import Document
from datetime import datetime

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
        self.webdriver.get(primeira_pagina)
        time.sleep(3)
        pyautogui.scroll(-500)
        time.sleep(3)
        pyautogui.scroll(-00)
        self.Endereco_Do_imovel()
    '''
    |Como iremos fazer o webscrapin do site de Leilão

    1°) iremos acessar com o selenium o link do site, já com as configurações necessárias:
    Ex: Filtro de Cidade, Filtro de Casa, na cidade de Salvador 
    3°) Iremos encontra a localização daquele imóvel 
    4°Iremos encontra o preço do imóvel a ser leiloado,
    5° Iremos encontra qual a porcentagem de desconto está este imóvel para poder avaliar se vale a pena ou não.
    6°) Iremos encontra se este Leilão é venda direta, venda online ou Financiamento.
    7°) Iremos saber até que dia podemos dá lance, ou até que dia o leilão se encera.

    No final, iremos colocar tudo no banco de Dados 


    '''

   
    def Endereco_Do_imovel(self):
        # time.sleep(10)
        print(os.linesep)
        Cidade_UF = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="address"]/p/b')
            )
        )
        if Cidade_UF is not None:
            print('Varrendo Site----- Cidade do Leilão ')

        print(f'🏘️ Iremos encontra o Endereço do Imóvel 🏘️')
        Endereco = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="address"]')
            )
        )
        if Endereco is not None:
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

        Modalidade_de_Compra = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//div[@class="categories"]')
            )
        )
        if Modalidade_de_Compra is not None:
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
        
        # Crie o documento antes do loop
        documento_Word = Document()
        documento_Word.add_heading('Scrapping Automação leilão em Salvador.',level=0)
        #  Agora iremos iterar sobre cada valor buscado no Xpath 
        # Itere pelos itens e adicione o conteúdo ao documento
        try:
            data_ano = datetime.now().strftime('%d-%m-%Y')
            segundos = datetime.now().strftime('-%S')
        except:
            print('Erro de tada e Hora e segundos')    
        for Cidade_UFs, Enderecos, Valores_Do_Anuncio, Desconto_Imovel, Modalidade_de_Compras, Encerramento_Do_Leilao in zip(Cidade_UF, Endereco, Valor_Do_Anuncio, Pocentagem_de_Desconto_Imovel, Modalidade_de_Compra,Data_do_Encerramento_Do_Leilao):
            # print(Produtos.text)
            
            print(os.linesep)
            #| ---------------------------------------|
            print(f'Localização do Estado: {Cidade_UFs.text}')
            #| ---------------------------------------|
            print(Enderecos.text)
            #| ---------------------------------------|
            print(Valores_Do_Anuncio.text)
            #| ---------------------------------------|
            print(Desconto_Imovel.text)
            #| ---------------------------------------|
            
            Resultados = Modalidade_de_Compras.text.split()  # Isso vai separar o texto em palavras
            print('  '.join(Resultados))
            #| ---------------------------------------|
            print(Encerramento_Do_Leilao.text)
            #| ---------------------------------------|
            print(os.linesep)
        
        #Iremos utilizar o docx - Documento word para salvar as informações do webscraping 
        # Adicione o conteúdo ao documento
            documento_Word.add_heading(f'{os.linesep}',level=1)
            documento_Word.add_paragraph(f'Localização do Estado: {Cidade_UFs.text}')
            documento_Word.add_paragraph(f'{Enderecos.text}')
            documento_Word.add_paragraph(f'{Valores_Do_Anuncio.text}')
            documento_Word.add_paragraph(f'{Desconto_Imovel.text}')
            documento_Word.add_paragraph(f"{'  '.join(Resultados)}")
            documento_Word.add_paragraph(f'{Encerramento_Do_Leilao.text}')

        # Salve o documento apenas uma vez, após o loop
        documento_Word.save(f'Automação_leilão{segundos}.docx')


            

        
        
        
        
        # Botao_Para_Ir_Ao_Proximo

        # Botao_Para_Ir_Ao_Proximo = self.wait.until(
        #     expected_conditions.presence_of_all_elements_located(
        #         (By.XPATH,'//button[@class="button borderd round"]')
        #     )
        # )    



         




Abertura = DescontoImoveis()
Abertura.Inicio() 
time.sleep(60)


