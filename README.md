# User Service

## Beschreibung
Der **User Service** ist ein zentraler Bestandteil einer Microservices-basierten E-Commerce-Anwendung. Er bietet eine REST-API zur Verwaltung von Benutzerdaten und Authentifizierung.

### Hauptfunktionen:
- **Benutzerregistrierung**: Erstellung neuer Benutzerkonten.
- **Benutzerauthentifizierung**: Login und Verifizierung via JWT.
- **Benutzerverwaltung**: Abrufen, Aktualisieren und Löschen von Benutzerdaten.

Dieser Service wurde mit **FastAPI** entwickelt und nutzt **MongoDB** zur Speicherung von Benutzerdaten. Die Authentifizierung erfolgt über JWT-Token.

---

## Technologien
- **FastAPI**: Framework für die API-Entwicklung.
- **MongoDB**: NoSQL-Datenbank für die Speicherung von Benutzerdaten.
- **JWT**: Token-basierte Authentifizierung.
- **Docker**: Containerisierung des Services.
- **GitHub Actions**: CI/CD-Pipeline zur Qualitätssicherung.

---

## Verwendete Endpunkte
### Authentication Endpoints:
- **POST** `/login/` - Authentifiziert einen Benutzer und gibt ein JWT zurück.
- **POST** `/token/verify` - Verifiziert ein JWT und gibt die Nutzerdaten zurück.
- **POST** `/logout/` - Invalidiert die Benutzersitzung.

### User Management Endpoints:
- **POST** `/register/` - Erstellt ein neues Benutzerkonto.
- **GET** `/users/me` - Gibt die Daten des aktuell eingeloggten Benutzers zurück.
- **GET** `/users/{user_id}` - Ruft Benutzerdaten anhand der Benutzer-ID ab.
- **PUT** `/users/{user_id}` - Aktualisiert die Benutzerdaten.
- **DELETE** `/users/{user_id}` - Löscht ein Benutzerkonto.

---

## Installation und Verwendung
### Voraussetzungen
- **Python 3.9+**
- **Docker** und **Docker Compose**

### Lokale Ausführung
1. **Repository klonen**:
   ```bash
   git clone <REPOSITORY_URL>
   cd user_service
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Service starten**:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8003
   ```

### Docker-Ausführung
1. **Docker-Image erstellen und starten**:
   ```bash
   docker build -t user_service .
   docker run -p 8003:8003 user_service
   ```

2. **Alternativ mit Docker Compose** (aus dem `Compose`-Repository):
   ```bash
   docker-compose up -d
   ```

### API-Dokumentation
FastAPI bietet eine automatisch generierte API-Dokumentation:
- Swagger UI: [http://localhost:8003/docs](http://localhost:8003/docs)
- ReDoc: [http://localhost:8003/redoc](http://localhost:8003/redoc)

---

## Datenbank
- **MongoDB** wird verwendet, um Benutzerdaten persistent zu speichern.
- Standardmäßig verbindet sich der Service zu `mongodb://localhost:27017`.
- Anpassung der URL über Umgebungsvariablen:
  ```env
  MONGODB_URL=mongodb://<host>:<port>
  ```

---

## Tests
1. **Testumgebung installieren**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Tests ausführen**:
   ```bash
   pytest tests/
   ```

---

## CI/CD
- Der Service verwendet **GitHub Actions**, um Tests und Linting automatisch bei jedem Commit auszuführen.
- Die Konfiguration befindet sich in `.github/workflows/ci.yml`.

---

## Umgebungsvariablen
- `SECRET_KEY`: Geheimer Schlüssel für JWT-Token.
- `ALGORITHM`: JWT-Algorithmus (z. B. `HS256`).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token-Gültigkeitsdauer (in Minuten).
- `MONGODB_URL`: MongoDB-Verbindungs-URL.

---
