import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Peso en los Planetas",
    page_icon="🪐",
    layout="centered"
)

st.title("🪐 Calculadora de peso en los planetas")
st.write("Ingresa tu peso en la Tierra y descubre cuánto pesarías en cada planeta del Sistema Solar.")

# Gravedad en cada planeta (m/s^2)
g_tierra = 9.80665

gravedades = {
    "Mercurio": 3.7,
    "Venus": 8.87,
    "Tierra": 9.80665,
    "Marte": 3.71,
    "Júpiter": 24.79,
    "Saturno": 10.44,
    "Urano": 8.69,
    "Neptuno": 11.15,
}

# Entrada del usuario
peso_tierra = st.number_input(
    "Peso en la Tierra (kg)",
    min_value=0.0,
    value=50.0,
    step=0.5
)

st.subheader("Resultados")

# Cálculo y tabla
resultados = []

for planeta, gravedad in gravedades.items():
    factor = gravedad / g_tierra
    peso_planeta = peso_tierra * factor
    resultados.append((planeta, peso_planeta))

st.table({
    "Planeta": [r[0] for r in resultados],
    "Peso aproximado (kg)": [f"{r[1]:.2f}" for r in resultados]
})

st.caption(
    "El peso depende de la gravedad. Si un planeta tiene menor gravedad que la Tierra, pesarás menos. "
    "Si tiene mayor gravedad, pesarás más."
)