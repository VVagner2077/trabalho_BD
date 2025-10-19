# Sistema de Aluguel de Betoneiras

![Status](https://img.shields.io/badge/status-em%20andamento-yellow)

Repositório criado para o desenvolvimento do trabalho da disciplina de Banco de Dados, da faculdade FAESA. O projeto consiste em um sistema em Python para gerenciar o aluguel de betoneiras, controlando clientes, equipamentos e os respectivos aluguéis.

## 💻 Tecnologias Utilizadas

-   **Linguagem:** Python
-   **SGBD:** PostgreSQL
-   **Hospedagem DB:** Aiven (Banco de Dados como Serviço - DBaaS)
-   **Bibliotecas Python:**
    -   `psycopg2-binary`: Driver de conexão para o PostgreSQL.
    -   `python-dotenv`: Para gerenciamento de variáveis de ambiente (credenciais do banco).

## 📂 Estrutura do Projeto

```
/
├── .env.example            # Arquivo de exemplo para variáveis de ambiente
├── conex/
│   └── database.py           # Módulo de conexão (lê as variáveis do .env)
├── controller/
│   ├── alugueis_controller.py
│   ├── betoneira_controller.py
│   └── cliente_controller.py
├── diagrams/
│   ├── Diagrama.png
│   └── diagrama.mmd
├── model/
│   ├── Alugueis.py
│   ├── Betoneiras.py
│   └── Cliente.py
├── reports/
│   └── relatorios.py
├── sql/
│   └── banco_dados.sql       # Script SQL para criação das tabelas
└── requirements.txt        # Lista de dependências Python
```

## 🚀 Começando

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

-   Python 3.x
-   Git

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/trabalho_BD.git](https://github.com/seu-usuario/trabalho_BD.git)
    cd trabalho_BD
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente:**
    -   Crie um arquivo chamado `.env` na pasta raiz do projeto (no mesmo nível de `requirements.txt`).
    -   Adicione ao arquivo `.env` as suas credenciais do banco de dados do Aiven, seguindo o exemplo abaixo:

    ```ini
    DB_HOST=seu-host-do-aiven.aivencloud.com
    DB_PORT=sua_porta
    DB_NAME=seu_banco_de_dados
    DB_USER=seu_usuario
    DB_PASS=sua_senha
    ```
    -   O arquivo `conex/database.py` utilizará a biblioteca `python-dotenv` para ler essas credenciais com segurança.

5.  **Execute o programa:**
    ```bash
    python nome_do_arquivo_principal.py
    ```

### 🔒 Segurança (Importante)

Para garantir que suas credenciais secretas do banco de dados não sejam enviadas ao GitHub, crie um arquivo chamado `.gitignore` na raiz do projeto (se ainda não existir) e adicione a seguinte linha a ele:

```
.env
```

## 👨‍🏫 Orientador

-   **Professor Howard** - FAESA

## 👥 Autores

-   Gabriel Rodrigo Lapa Rocha
-   Micael Ribeiro dos Santos
-   Wagner dos Santos Cristo
