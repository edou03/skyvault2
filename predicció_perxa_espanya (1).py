import streamlit as st
import pickle
import pandas as pd

# 📥 Carrega el model
with open("model_lr.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎯 Predicció del salt amb perxa")

st.markdown("Introdueix les dades de l'atleta per predir l'alçada estimada del salt.")

# 🧪 Inputs de l'usuari
genero = st.radio("Gènere", ["Home", "Dona"])
talla = st.number_input("Talla (m)", value=1.78, step=0.01)
pes = st.number_input("Pes (kg)", value=68, step=1)
velocitat = st.number_input("Velocitat 10-5m (m/s)", value=8.3, step=0.1)
aceleracio = st.number_input("Acceleració 10-5m (m/s²)", value=0.28, step=0.01)
distancia_batida = st.number_input("Distància de batuda (m)", value=3.5, step=0.1)
grip = st.number_input("Grip (m)", value=4.4, step=0.1)
pole_length = st.number_input("Longitud de la perxa (m)", value=4.6, step=0.1)
pole_flex = st.number_input("Flexió de la perxa", value=18.8, step=0.1)

# Converteix el gènere a numèric
genere_num = 1 if genero == "Home" else 0

# 🧮 Predicció
if st.button("Predir alçada del salt"):
    input_data = {
        'Genero': genere_num,
        'Talla': talla,
        'peso': pes,
        'Velocidad 10-5m': velocitat,
        'Aceleracion 10-5m': aceleracio,
        'Distancia Batida': distancia_batida,
        'grip': grip,
        'pole length': pole_length,
        'pole flex': pole_flex
    }
    input_df = pd.DataFrame([input_data])
    prediccio = model.predict(input_df)[0]
    st.success(f"🎯 Alçada estimada del salt: **{prediccio:.2f} m**")
