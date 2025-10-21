# Usa uma imagem oficial do Python 3.10 como base.
FROM python:3.10-slim

# Define o diretório onde nosso código ficará dentro do contêiner.
WORKDIR /app

# Copia o arquivo de dependências para dentro do contêiner.
COPY requirements.txt .
# Instala as bibliotecas listadas no requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os outros arquivos do seu projeto (o ".") para a pasta /app dentro do contêiner.
COPY . .

# Define o comando que será executado quando o contêiner iniciar.
# Altere esta linha:
CMD ["python", "main.py"]