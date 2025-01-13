


-------------------1° Tabela------------------------------------------------------------------------------
Cidade_Estado---> Id_cidade:	= int primary key indentity,
		          Cidade:       = Vachar(60), 
                  Endereço:     =Vachar(200)

-----------------2° Tabela------------------------------------------------------------------------------------------------
Preço:---------->  Id_preço:        = primary key indentity,
		           Preço:           = Vachar(20), 
                   Desconto_imovel: = Vachar(4)

-----------------3° Tabela-------------------------------------------------------------------------------------------------
Modalidade_de_Compra ------> Id_modalidade:     = primary key indentity,
			                 Modalidades:       = Vachar(100),
                             Data_encerramento: = Vachar(50)

==========================================================================
<!-- Tabela de Estados -->
CREATE TABLE Estados(
    id_estado = int PRIMAY KEY IDENTITY(1,1),
    nome = vachar(50) NOT NULL,
    uf = char(2), 

);

<!-- Tabela de cidade  -->
CREATE TABLE Cidade (
    id_cidade  int PRIMARY KEY IDENTITY(1,1),
    nome  varchar(60),
    id_estado  int NOT NULL,
    FOREIGN KEY (id_estado) REFERENCES Estados (id_estado)

);

<!-- Tabela de Endereço -->
CREATE TABLE Enderecos(
    id_endereco int PRIMARY KEY IDENTITY(1,1),
    logradouro  varchar(100),
    numero varchar(10),
    compremento varchar(50),
    bairro varchar(50),
    cep   char(8),
    id_cidade int not null
    FOREIGN KEY (id_cidade) REFERENCES Cidades(id_cidade)
);

<!-- Tabela de Modalidade de Compra -->
CREATE TABLE Modalidade_Compra(
id_modalidade int PRIMARY KEY IDENTITY(1,1),
nome varchar(100),
descricao Text,
data_inicio date,
data_encerramento date,
status Char(1) NOT NULL DEFAULT 'A'
CHECK (status IN('A','I')), --Ativo ou Inativo o Leilão
CHECK (data_encerramento >= data_inicio)
);
===================================================================FEITO POR IA=========================
-- Tabela de Estados
CREATE TABLE Estados (
    id_estado INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL UNIQUE
);

-- Tabela de Cidades
CREATE TABLE Cidades (
    id_cidade INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(60) NOT NULL,
    id_estado INT NOT NULL,
    FOREIGN KEY (id_estado) REFERENCES Estados(id_estado)
);

-- Tabela de Endereços
CREATE TABLE Enderecos (
    id_endereco INT PRIMARY KEY IDENTITY(1,1),
    logradouro VARCHAR(100) NOT NULL,
    numero VARCHAR(10),
    complemento VARCHAR(50),
    bairro VARCHAR(50) NOT NULL,
    cep CHAR(8) NOT NULL,
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES Cidades(id_cidade)
);

-- Tabela de Preços
CREATE TABLE Precos (
    id_preco INT PRIMARY KEY IDENTITY(1,1),
    valor DECIMAL(10,2) NOT NULL,
    desconto_percentual DECIMAL(5,2),
    data_vigencia_inicial DATE NOT NULL,
    data_vigencia_final DATE,
    CHECK (desconto_percentual >= 0 AND desconto_percentual <= 100)
);

-- Tabela de Modalidades de Compra
CREATE TABLE Modalidades_Compra (
    id_modalidade INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_encerramento DATE,
    status CHAR(1) NOT NULL DEFAULT 'A',
    CHECK (status IN ('A', 'I')), -- Ativo ou Inativo
    CHECK (data_encerramento >= data_inicio)
);
