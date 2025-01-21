from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(
    title="User Service API",
    description="API für Benutzeroperationen",
    version="1.0.0",
    docs_url='/docs',
    redoc_url='/docs',
    openapi_url='/openapi.json',
    root_path='/api/user',
)

# CORS-Middleware hinzufügen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Erlaube Anfragen von deinem Frontend
    allow_credentials=True,  # Erlaube das Setzen von Cookies
    allow_methods=["*"],  # Erlaube alle HTTP-Methoden (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Erlaube alle Header
)

# Binde den API-Router an die App
app.include_router(router)
