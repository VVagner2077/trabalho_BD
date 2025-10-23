
<p align="center">
  <img src="./assets/banner.jpg" alt="Sistema de Aluguer de Betoneiras" height="500">
</p>

# 🧱 Sistema de Aluguer de Betoneiras

Repositório criado para o desenvolvimento do trabalho da disciplina de **Base de Dados** da **FAESA**.
O projeto consiste num **sistema em Python** para gerir o **aluguer de betoneiras**, controlando **clientes**, **equipamentos** e os **respetivos alugueres**.

---

## 💻 Tecnologias Utilizadas

**Linguagem:**

<img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" alt="Python">

**SGBD:**

<img src="https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white" alt="PostgreSQL">

**Bibliotecas Python:**

* `psycopg2-binary` → Driver de ligação com PostgreSQL
* `python-dotenv` → Gestão de variáveis de ambiente
* `pandas` → Exibição de relatórios formatados

**Containerização:**

<img src="https://img.shields.io/badge/Docker-Suportado-2496ED?logo=docker&logoColor=white" alt="Docker">

---

## 📂 Estrutura do Projeto

```

Sistema_de_aluguel_de_betoneira/
├── .env                  # Ficheiro local com as credenciais
|
│
├── conexion/
│   └── database.py       # Módulo de ligação com a base de dados
│
├── controller/
│   ├── alugueis_controller.py
│   ├── betoneira_controller.py
│   └── cliente_controller.py
│
├── diagrams/
│   └── diagrama_final.mmd
│
├── pesquisa/
│   └── pesquisa.py       # Módulo para consultas e relatórios
│
├── sql/
│   └── banco_dados.sql   # Script SQL para criação das tabelas
│
├── utils/
│   ├── inputs_tratados.py
│   └── menu.py
│
├── Dockerfile            # Ficheiro para criar a imagem Docker
├── main.py               # Ponto de entrada da aplicação
└── requirements.txt      # Lista de dependências Python

````

---

## 🚀 Começando

### 🧩 Pré-requisitos

* Python **3.9+**
* Git
* Docker *(opcional, para execução em container)*

---

### ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/VVagner2077/Sistema_de_aluguel_de_betoneira.git
cd Sistema_de_aluguel_de_betoneira
````

Crie e ative um ambiente virtual:

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux / Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rodar o codigo
```bash
python main.py
```
---

## 🐳 Execução com Docker

**Construir a imagem:**

```bash
docker build -t aluguer-betoneiras .
```

**Executar o container:**

```bash
docker run -it --rm --env-file .env aluguer-betoneiras
```

---

## 👨‍🏫 Orientador

**Professor:** Howard — FAESA

---

## 👥 Autores

* **Gabriel Rodrigo Lapa Rocha**
* **Micael Ribeiro dos Santos**
* **Wagner dos Santos Cristo**

oi