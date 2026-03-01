import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peso en los Planetas", page_icon="🪐", layout="centered")

st.title("🪐 Peso en los Planetas")
st.write("Ingresa tu peso en la Tierra y descubre cuánto pesarías en cada planeta del Sistema Solar.")

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

peso_tierra = st.number_input("Tu peso en la Tierra (kg)", min_value=0.0, value=50.0, step=0.5)

# Controles visuales
c1, c2 = st.columns([1, 1])
with c1:
    orden = st.radio("Ordenar resultados por:", ["Planeta", "Tu peso"], horizontal=True)
with c2:
    mostrar_grafica = st.toggle("Mostrar gráfica", value=True)

# Construir DataFrame
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

# Orden
if orden == "Tu peso":
    df = df.sort_values("Peso", ascending=False).reset_index(drop=True)
else:
    df = df.sort_values("Planeta", ascending=True).reset_index(drop=True)

# Para barras visuales: normalizar con el máximo
max_peso = max(df["Peso"].max(), 0.0001)
min_peso = df["Peso"].min()

# Identificar extremos
idx_max = df["Peso"].idxmax()
idx_min = df["Peso"].idxmin()

st.subheader("✨ Resultados")
st.caption("Cada tarjeta muestra tu peso estimado y una barra visual para comparar rápidamente.")

# Tarjetas en columnas
cols = st.columns(2)
for i, r in df.iterrows():
    etiqueta = r["Etiqueta"]
    peso = r["Peso"]
    factor_pct = (r["Factor"] - 1) * 100

    # Barra visual (0 a 1)
    nivel = float(peso / max_peso) if peso_tierra > 0 else 0.0

    # Mensaje corto para extremos (sin sección aparte)
    extra = ""
    if i == idx_max:
        extra = "  ⭐ Más pesado"
    elif i == idx_min:
        extra = "  🪶 Más ligero"

    with cols[i % 2]:
        st.markdown(f"### {etiqueta}{extra}")
        st.metric(
            label="Peso estimado",
            value=f"{peso:.2f} kg",
            delta=f"{factor_pct:+.1f}% vs Tierra"
        )
        st.progress(nivel)
        st.caption(f"Factor: {r['Factor']:.3f}  |  Gravedad: {r['Gravedad']:.2f} m/s²")

st.divider()

# Gráfica (impactante y fácil)
if mostrar_grafica:
    st.subheader("📊 Comparación visual")
    chart = df.set_index("Etiqueta")["Peso"]
    st.bar_chart(chart)

st.caption(
    "Idea clave: el peso cambia porque la gravedad no es igual en todos los planetas. "
    "Calculamos: peso en planeta = peso en Tierra × (gravedad del planeta / gravedad de la Tierra)."
)