#!/bin/bash

# Démarrer le backend Flask en arrière-plan
cd /app/backend
flask run --host=0.0.0.0 --port=5000 &

# Démarrer le frontend Streamlit
cd /app/frontend
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
