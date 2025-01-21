# Basis-Image
FROM python:3.9-slim

# Systemabhängigkeiten installieren
RUN apt-get update && \
    apt-get install -y build-essential gcc libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Anforderungen kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . .

# Port und Startbefehl festlegen
EXPOSE 8003
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]

