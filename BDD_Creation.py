import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle
import sqlite3


#Transfore le résultat en utilisant la fonction arctrangente
def transform_prediction (sin,cos):
    resultat=np.arctan2(sin, cos) * (24 / (2 * np.pi))
    return(resultat)
loaded_df=pd.read_csv("2205_Cycle.csv")
# Charger les modèles depuis le fichier pickle
with open("model_rf.pkl", "rb") as f:
    loaded_model = pickle.load(f)

X=np.array(loaded_df[['df_FS1_10HZ_ML', 'df_PS2_100HZ_ML']])
#Normalisation des données 
scaler = MinMaxScaler()  # Vous pouvez aussi utiliser StandardScaler pour la standardisation 
X_scaled = scaler.fit_transform(X)
profile_ML_pred=loaded_model.predict(X_scaled)
predicted_profile=transform_prediction(profile_ML_pred[:, 0],profile_ML_pred[:, 0])
loaded_df['predictions']=predicted_profile
print(loaded_df)

# Connexion à SQLite
db_file = "Predictions.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Étape 1 : Créer la table avec des colonnes dynamiques
table_name = "table_predication"

# Construire la requête CREATE TABLE en utilisant uniquement les noms de colonnes
columns = loaded_df.columns
columns_query = ", ".join([f"{col}" for col in columns])
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query})"

# Exécuter la requête
cursor.execute(create_table_query)
conn.commit()

# Étape 2 : Insérer les données dans la table
loaded_df.to_sql(table_name, conn, if_exists="append", index=False)

# Vérifier les données insérées
cursor.execute(f"SELECT * FROM {table_name} LIMIT 10")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fermer la connexion
conn.close()