# 1. Immagine base
FROM python:3.11-slim

# 2. Imposta la cartella di lavoro DENTRO il container
WORKDIR /app

# 3. Copia il file (percorso relativo al repo -> percorso relativo a WORKDIR)
COPY modules/hello_docker.py .

# 4. Esecuzione (ora il file è direttamente in /app/hello_docker.py)
CMD ["python", "hello_docker.py"]
