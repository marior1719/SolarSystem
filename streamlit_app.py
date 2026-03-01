import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peso en los Planetas", page_icon="🪐", layout="centered")

st.title("🪐 Peso en los Planetas")
st.write("Descubre cuánto pesarías en cada planeta del Sistema Solar según la gravedad.")

G_TIERRA = 9.80665

planetas = [
    {"Planeta": "Mercurio", "Emoji": "☿️", "Gravedad": 3.70},
    {"Planeta": "Venus", "Emoji": "♀️", "Gravedad": 8.87},
    {"Planeta": "Tierra", "Emoji": "🌍", "Gravedad": 9.80665},
    {"Planeta": "Marte", "Emoji": "♂️", "Gravedad": 3.71},
    {"Planeta": "Júpiter", "Emoji": "🟠", "Gravedad": 24.79},
    {"Planeta": "Saturno", "Emoji": "🪐", "Gravedad": 10.44},
    {"Planeta": "Urano", "Emoji": "🧊", "Gravedad": 8.69},
    {"Planeta": "Neptuno", "Emoji": "🔵", "Gravedad": 11.15},
]

peso_tierra = st.number_input(
    "Tu peso en la Tierra (kg)",
    min_value=0.0,
    value=50.0,
    step=0.5
)

# Crear datos
rows = []
for p in planetas:
    factor = p["Gravedad"] / G_TIERRA
    peso_planeta = peso_tierra * factor
    rows.append({
        "Planeta": p["Planeta"],
        "Emoji": p["Emoji"],
        "Gravedad": p["Gravedad"],
        "Factor": factor,
        "Peso": peso_planeta
    })

df = pd.DataFrame(rows)
df["Etiqueta"] = df["Emoji"] + " " + df["Planeta"]

max_peso = max(df["Peso"].max(), 0.0001)

st.subheader("✨ Resultados")

cols = st.columns(2)

for i, r in df.iterrows():
    with cols[i % 2]:
        st.markdown(f"### {r['Etiqueta']}")
        st.metric(
            label="Peso estimado",
            value=f"{r['Peso']:.2f} kg",
            delta=f"{(r['Factor'] - 1) * 100:+.1f}% vs Tierra"
        )
        st.progress(float(r["Peso"] / max_peso))
        st.caption(f"Gravedad: {r['Gravedad']} m/s²")

st.divider()

st.subheader("📊 Comparación Visual")

chart = df.set_index("Etiqueta")["Peso"]
st.bar_chart(chart)

st.caption(
    "El peso cambia porque cada planeta tiene una gravedad diferente. "
    "Para calcularlo usamos la proporción entre la gravedad del planeta y la gravedad de la Tierra."
)