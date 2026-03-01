import streamlit as st

st.set_page_config(page_title="Solar System Weight Explorer", page_icon="🪐", layout="wide")

st.markdown("""
<style>

/* Fondo */
.stApp {
  background: radial-gradient(1200px 600px at 30% 10%, rgba(255,120,60,0.08), transparent 60%),
              radial-gradient(900px 500px at 80% 30%, rgba(80,160,255,0.08), transparent 55%),
              linear-gradient(180deg, #0b0f17, #0a0d14 60%, #070a10);
  color: #e9eef7;
}

/* MÁS espacio arriba */
.block-container { 
  padding-top: 4.5rem; 
  padding-bottom: 2.5rem; 
  max-width: 1250px; 
}

/* Oculta línea gris superior */
header {visibility: hidden;}
#MainMenu, footer { visibility: hidden; }

/* Header */
.header-wrap { 
  display:flex; 
  align-items:center; 
  gap:14px; 
  margin-bottom: 40px; 
}
.logo {
  width:44px; height:44px; border-radius: 14px;
  display:flex; align-items:center; justify-content:center;
  background: rgba(255,120,60,0.12);
  border: 1px solid rgba(255,120,60,0.25);
  font-size: 22px;
}
.title { font-size: 42px; font-weight: 900; margin:0; }
.subtitle { font-size: 14px; color: rgba(233,238,247,0.65); }

/* ✅ Card REAL: estiliza la columna izquierda (sin HTML abierto/cerrado) */
div[data-testid="stHorizontalBlock"] > div:first-child div[data-testid="stVerticalBlock"] > div:first-child {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 22px;
  padding: 26px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

/* Texto secciones */
.section-title {
  font-size: 13px;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: rgba(233,238,247,0.65);
  margin-bottom: 10px;
}
.section-gap { height: 18px; }

/* Input */
.stNumberInput label { display:none !important; }
.stNumberInput input {
  font-size: 36px !important;
  padding: 16px !important;
  border-radius: 16px !important;
  border: 2px solid rgba(255,120,60,0.6) !important;
  background: rgba(255,255,255,0.03) !important;
}

/* Botón */
.stButton button {
  width: 100%;
  padding: 14px 16px;
  border-radius: 16px;
  font-size: 16px;
  font-weight: 800;
  border: 0;
  color: #10131a;
  background: linear-gradient(90deg, #ff8a3d, #ff5b62);
}

/* Info box */
.info {
  margin-top: 20px;
  padding: 16px;
  border-radius: 18px;
  border: 1px solid rgba(255,120,60,0.18);
  background: rgba(255,120,60,0.06);
  font-size: 14px;
  line-height: 1.45;
}

/* Planet cards */
.pcard {
  background: rgba(255,255,255,0.035);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 10px 26px rgba(0,0,0,0.30);
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 18px;
}
.p-left { display:flex; align-items:center; gap:14px; }
.p-dot {
  width: 48px; height: 48px; border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.16);
}
.p-name {
  font-size: 12px;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  color: rgba(233,238,247,0.70);
}
.p-value { font-size: 30px; font-weight: 900; }
.p-unit { font-size: 12px; color: rgba(233,238,247,0.65); margin-left: 6px; }
.p-g { font-size: 12px; color: rgba(233,238,247,0.55); text-align:right; }

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-wrap">
  <div class="logo">🚀</div>
  <div>
    <div class="title">Solar System Weight Explorer</div>
    <div class="subtitle">Discover your weight across the cosmos</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Datos
G_EARTH = 9.80665
planets = [
    ("Mercury", 3.70, "linear-gradient(145deg, #8a95a6, #2f3540)"),
    ("Venus", 8.87, "linear-gradient(145deg, #ffb25a, #b85a11)"),
    ("Earth", 9.80665, "linear-gradient(145deg, #2bd0ff, #1f3cff)"),
    ("Mars", 3.71, "linear-gradient(145deg, #ff8b4a, #b2321f)"),
    ("Jupiter", 24.79, "linear-gradient(145deg, #ffb15a, #8a3a14)"),
    ("Saturn", 10.44, "linear-gradient(145deg, #ffd56a, #b78522)"),
    ("Uranus", 8.69, "linear-gradient(145deg, #7de7ff, #1b6b7a)"),
    ("Neptune", 11.15, "linear-gradient(145deg, #6b86ff, #1430b3)"),
]

left, right = st.columns([1.05, 1.45], gap="large")

with left:
    st.markdown('<div class="section-title">Your Earth Weight (kg)</div>', unsafe_allow_html=True)

    earth_weight = st.number_input(
        "Earth weight",
        min_value=0.0,
        value=50.0,
        step=0.5,
        label_visibility="collapsed"
    )

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    st.button("Sync with NASA")

    st.markdown("""
    <div class="info">
      Weight is the force of gravity acting on an object. Because planets have different
      masses and sizes, their surface gravity varies.<br><br>
      Your mass remains constant everywhere, but your weight changes based on where you stand.
    </div>
    """, unsafe_allow_html=True)

with right:
    earth_kg = earth_weight
    out_unit = "KG"

    cA, cB = st.columns(2, gap="large")

    for idx, (name, g, grad) in enumerate(planets):
        factor = g / G_EARTH
        w_out = earth_kg * factor
        target = cA if idx % 2 == 0 else cB

        with target:
            st.markdown(f"""
            <div class="pcard">
              <div class="p-left">
                <div class="p-dot" style="background:{grad};"></div>
                <div>
                  <div class="p-name">{name}</div>
                  <div class="p-value">{w_out:.1f}<span class="p-unit">{out_unit}</span></div>
                </div>
              </div>
              <div class="p-g">Gravity:<br>{factor:.3f}G</div>
            </div>
            """, unsafe_allow_html=True)