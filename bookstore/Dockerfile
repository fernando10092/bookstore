# Base Python slim image
FROM python:3.8.1-slim as base

# Variáveis de ambiente para comportamento consistente do Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instalar dependências do sistema (PostgreSQL e ferramentas de compilação)
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl build-essential libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY requirements.txt .

# Instalar dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto
COPY . .

# Expor a porta da aplicação
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
