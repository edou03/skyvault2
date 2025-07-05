import pickle
import pandas as pd
import streamlit as st



# 📥 Carrega el model guardat
with open("model_lr.pkl", "rb") as f:
    model = pickle.load(f)

# 🧪 Exemple de dades d’entrada (modifica-ho per provar diferents atletes)
input_data = {
    'Genero': ,  # 1 = Home, 0 = Dona
    'Talla': ,
    'peso':,
    'Velocidad 10-5m': ,
    'Aceleracion 10-5m': ,
    'Distancia Batida': ,
    'grip': ,
    'pole length': ,
    'pole flex': 
}

# 🧮 Converteix a DataFrame i prediu
input_df = pd.DataFrame([input_data])
prediccio = model.predict(input_df)[0]

# 📢 Resultat
print(f"🎯 Alçada estimada del salt: {prediccio:.2f} m")
