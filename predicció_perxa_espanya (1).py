import pickle
import pandas as pd
import streamlit as st

# 📥 Carrega el model guardat
with open("model_lr.pkl", "rb") as f:
    model = pickle.load(f)

# 🧪 Exemple de dades d’entrada (modifica-ho per provar diferents atletes)
input_data = {
    'Genero':1 ,  # 1 = Home, 0 = Dona
    'Talla': 1.78,
    'peso':68,
    'Velocidad 10-5m':8.3 ,
    'Aceleracion 10-5m': 0.3,
    'Distancia Batida': 3.5,
    'grip': 4.4,
    'pole length':4.6,
    'pole flex':18.8 
}

# 🧮 Converteix a DataFrame i prediu
input_df = pd.DataFrame([input_data])
prediccio = model.predict(input_df)[0]

# 📢 Resultat
print(f"🎯 Alçada estimada del salt: {prediccio:.2f} m")
