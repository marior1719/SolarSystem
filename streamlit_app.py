import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peso en los Planetas", page_icon="🪐", layout="centered")

# 🎨 Estilos personalizados
st.markdown("""
<style>
.big-title {
    font-size: 54px;
    font-weight: 900;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
    line-height: 1.1;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: gray;
    margin-bottom: 40px;
}

.center-box {
    display: flex;
    justify-content: center;
}

.stNumberInput > div {
    width: 100%;
}

.stNumberInput label {
    text-align: center !important;
    width: 100%;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.stNumberInput input {
    font-size: 34px !important;
    text-align: center !important;
    padding: 12px !important;
    border-radius: 16px !important;
}

.hint {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 10px;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# 🚀 Header
st.markdown('<div class="big-title">🪐 ¿Cuánto pesarías en otros planetas?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">La gravedad cambia en cada planeta, y tu peso también.</div>', unsafe_allow_html=True)

# 🎯 Input perfectamente centrado
col1, col2, col3 = st.columns([1,2,1])

with col2:
    peso_tierra = st.number_input(
        "🌍 Ingresa tu peso en la Tierra (kg)",
        min_value=0.0,
        value=50.0,
        step=0.5
    )

st.markdown('<div class="hint">Prueba diferentes valores y observa cómo cambian los resultados.</div>', unsafe_allow_html=True)

# 🌍 Datos
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

# 📊 Cálculos
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

# ✨ Resultados
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
        st.caption(f"Gravedad: {r['Gravedad']:.2f} m/s²")

st.divider()

# 📈 Gráfica
st.subheader("📊 Comparación visual")
st.bar_chart(df.set_index("Etiqueta")["Peso"])

st.caption(
    "El peso cambia porque cada planeta tiene una gravedad diferente. "
    "Cálculo: peso en planeta = peso en Tierra × (gravedad del planeta / gravedad de la Tierra)."
)