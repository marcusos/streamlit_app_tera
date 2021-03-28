# camada básica do aplicativo
FROM python:3.8.2-slim

# Setando as variáveis de ambiente,
# Definindo a porta padrão
ENV PORT 8501

# estabelece a pasta raiz na imagem
WORKDIR /app

# COPY: copia os arquivos da máquina física para a imagem docker
COPY requirements.txt ./
COPY app.py ./
COPY models/model_v0.joblib ./models/

# instala as bibliotecas específicas na imagem
RUN pip install -U pip
RUN pip install -r requirements.txt

# código a ser executado no terminal da imagem
CMD streamlit run --server.enableCORS=False --server.port=$PORT app.py