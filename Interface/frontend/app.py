import streamlit as st
import requests

# Crée l'interface utilisateur Streamlit
st.title("Cycle Data Predictor")

# Demande à l'utilisateur de saisir l'ID du cycle
cycle_id = st.number_input("Entrez l'ID du cycle", min_value=1, step=1)

if cycle_id:
    # Faire une requête GET vers l'API backend
    response = requests.get(f'http://127.0.0.1:5000/get_cycle_data?id={cycle_id}')

    if response.status_code == 200:
        data = response.json()
        st.write(f"**Valeur prédite pour l'ID {cycle_id}:** {data['predicted_value']}")
        st.write(f"**Valeur réelle pour l'ID {cycle_id}:** {data['actual_value']}")
    else:
        st.write("Erreur : " + response.json().get('error', 'Unknown error'))
