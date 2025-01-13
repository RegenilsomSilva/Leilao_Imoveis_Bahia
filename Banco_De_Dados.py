
'''Para saber qual é o seu Servidor Local, 
você precisa entra no Windows +R, CMD -> e digitar -> Hostname 
serv = o seu servidor da sua máquina local 
MTZ-TI-DESK-RE\SQLEXPRESS01'
'''

# Primeiro instalar o Driver que faz a conexão com o Banco de Dado - SQLserver
#  pip install pyodbc
# Banco de Dados que criamos = BD_Python
# MSSQLSERVER
import pyodbc
import os

# Backup="Driver={SQL Server};" \SQLEXPRESS




Dados_Da_Conexao = (
    "Driver={SQL Server};"
    "Server=MTZ-TI-DESK-RE\\SQLEXPRESS01;"
    "Database=BD_Python;"
    "Trusted_Connection=yes;" 
    
    # trusted_connection=yes siguinifica que não precisa de senha para acessar o banco de dados, ele utilizar as configurações do windows para se autenticar
)
    
    
try:
    Conexao = pyodbc.connect(Dados_Da_Conexao)

    print(os.linesep)
    print('Obrigado...Conexão Bem Sucedida\n')
except pyodbc.Error as err:

      print(os.linesep)
      print(f'Connection Error: {err}') 
      print('Erro na conexão com o banco de dados... verifique se o trused_connection está ativado')

# vamos inserir informações no banco de dados
cursor = Conexao.cursor()

# Vamos utilizar o conceito de Cursor
# Cursor é um objeto que permite que você interaja com o banco de dados
# Vamos criar dinamicamente os valores para inserir no banco de dados
# comando =""" 
# INSERT INTO venda( cliente, produto, data_venda, preco, quantidade)
# VALUES('Maiara', 'Bicicleta','01-01-2025','1500', '1');
# """ 
try:
    
    cliente ="Marcos"
    produto ="Caro"
    data_venda ="02-01-2025"
    preco ="2500"
    quantidade =1


    comando =f""" 
    INSERT INTO venda( cliente, produto, data_venda, preco, quantidade)
    VALUES('{cliente}','{produto}', '{data_venda}', {preco}, {quantidade});
    """ 
    cursor.execute(comando)
    cursor.commit()
    print('Dados Inseridos com Sucesso\n')
except pyodbc.Error as err:
    print(f'Error: {err}')
    print('Erro ao inserir os dados no banco de dados\n')