# Utiliser une image Python comme base
FROM python:3.9-slim


# Définir le répertoire de travail
WORKDIR /app

# Installer SQLite3 et ses dépendances
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev
# Copier le fichier SQLite dans l'image Docker
COPY backend/Predictions.db /app/data/Predictions.db
    
# Copier les fichiers de dépendances
COPY backend/requirements.txt /app/backend-requirements.txt
COPY frontend/requirements.txt /app/frontend-requirements.txt

# Installer toutes les dépendances
RUN pip install --no-cache-dir -r /app/backend-requirements.txt
RUN pip install --no-cache-dir -r /app/frontend-requirements.txt

# Copier les codes des applications
COPY backend /app/backend
COPY frontend /app/frontend

# Exposer les ports pour Flask et Streamlit
EXPOSE 5000 8501

# Script pour lancer le back et le front 
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Commande par défaut pour démarrer le script
CMD ["/app/start.sh"]
