import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("crop_model.joblib")

st.set_page_config(
    page_title="Recomendação de Culturas",
)

st.title("Recomendação de Culturas Agrícolas")

st.write(
    "Informe os dados do solo e do clima para receber uma previsãoda cultura mais compatível com as condições informadas."
)

st.subheader("Dados do solo")

n = st.number_input(
    "Nitrogênio (N)",
    min_value=0.0,
    step=1.0
)

p = st.number_input(
    "Fósforo (P)",
    min_value=0.0,
    step=1.0
)

k = st.number_input(
    "Potássio (K)",
    min_value=0.0,
    step=1.0
)

ph = st.number_input(
    "pH do solo",
    min_value=0.0,
    max_value=14.0,
    value=6.5,
    step=0.1
)

st.subheader("Condições climáticas")

temperatura = st.number_input(
    "Temperatura (°C)",
    value=25.0,
    step=0.1
)

umidade = st.number_input(
    "Umidade (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=0.1
)

chuva = st.number_input(
    "Precipitação (mm)",
    min_value=0.0,
    value=100.0,
    step=1.0
)

if st.button("Gerar Recomendação"):

    entrada = pd.DataFrame([{
        "N": n,
        "P": p,
        "K": k,
        "temperature": temperatura,
        "humidity": umidade,
        "ph": ph,
        "rainfall": chuva
    }])

    previsao = modelo.predict(entrada)[0]

    st.success(
        f"Cultura com maior taxa de recomendação sob previsão: **{previsao.upper()}**"
    )

    st.info(
        "Esta previsão possui finalidade acadêmica e foi gerada com base "
        "nos padrões presentes no dataset utilizado. O resultado não substitui "
        "uma avaliação agronômica profissional."
    )