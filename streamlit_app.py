import streamlit as st

st.set_page_config(page_title="Solar System Weight Explorer", page_icon="🪐", layout="wide")

# ---------- Helpers ----------
def set_unit(u: str):
    st.session_state["unit"] = u

def init_state():
    if "unit" not in st.session_state:
        st.session_state["unit"] = "kg"
    if "earth_kg" not in st.session_state:
        st.session_state["earth_kg"] = 50.0  # valor inicial en kg

init_state()

# ---------- CSS ----------
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

/* Panel izquierdo */
.card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 22px;
  padding: 26px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

.section-title {
  font-size: 13px;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: rgba(233,238,247,0.65);
  margin-bottom: 10px;
}

.section-gap { height: 18px; }

/* Toggle (sin st.radio) */
.toggle-wrap {
  display:flex;
  gap: 12px;
  margin-bottom: 18px;
}
.toggle-wrap .stButton button {
  width: 110px;
  padding: 10px 14px;
  border-radius: 14px;
  font-weight: 800;
  border: 1px solid rgba(255,255,255,0.14);
  background: rgba(255,255,255,0.04);
  color: rgba(233,238,247,0.80);
  box-shadow: none;
}
.toggle-wrap .stButton button:hover {
  border-color: rgba(255,255,255,0.22);
  filter: none;
}

/* Botón activo */
.toggle-wrap .stButton button.active {
  border: 0 !important;
  color: #10131a !important;
  background: linear-gradient(90deg, #ff8a3d, #ff5b62) !important;
}

/* Input */
.stNumberInput label { display:none !important; }
.stNumberInput input {
  font-size: 36px !important;
  padding: 16px !important;
  border-radius: 16px !important;
  border: 2px solid rgba(255,120,60,0.6) !important;
  background: rgba(255,255,255,0.03) !important;
}

/* Botón principal */
.primary .stButton button {
  width: 100%;
  padding: 14px 16px;
  border-radius: 16px;
  font-size: 16px;
  font-weight: 800;
  border: 0;
  color: #10131a;
  background: linear-gradient(90deg, #ff8a3d, #ff5b62);
  box-shadow: 0 12px 30px rgba(255,100,80,0.25);
}
.primary .stButton button:hover { filter: brightness(1.05); }

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

#MainMenu, footer { visibility: hidden; }

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="header-wrap">
  <div class="logo">🚀</div>
  <div>
    <div class="title">Solar System Weight Explorer</div>
    <div class="subtitle">Discover your weight across the cosmos</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- Data ----------
G_EARTH = 9.80665
LB_PER_KG = 2.2046226218

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

# ---------- Layout ----------
left, right = st.columns([1.05, 1.45], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Toggle sin st.radio (sin barra fea)
    st.markdown('<div class="toggle-wrap">', unsafe_allow_html=True)
    b1, b2, _ = st.columns([0.18, 0.18, 0.64])
    with b1:
        if st.button("kg", key="btn_kg"):
            set_unit("kg")
    with b2:
        if st.button("lbs", key="btn_lbs"):
            set_unit("lbs")
    st.markdown("</div>", unsafe_allow_html=True)

    # Marca visual de botón activo (CSS class "active") usando un pequeño truco
    # Streamlit no permite setear class en botones directamente, así que lo hacemos con JS mínimo.
    active = st.session_state["unit"]
    st.markdown(f"""
    <script>
      const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
      // Busca los botones por texto exacto y les pone clase "active" al seleccionado
      buttons.forEach(b => {{
        if (b.innerText.trim() === "kg") b.classList.toggle("active", "{active}" === "kg");
        if (b.innerText.trim() === "lbs") b.classList.toggle("active", "{active}" === "lbs");
      }});
    </script>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Your Earth Weight</div>', unsafe_allow_html=True)

    # Mantener SIEMPRE un solo valor fuente en kg en session_state
    if st.session_state["unit"] == "kg":
        shown = st.session_state["earth_kg"]
        val = st.number_input("Earth weight", min_value=0.0, value=float(shown), step=0.5, label_visibility="collapsed")
        st.session_state["earth_kg"] = float(val)
    else:
        shown_lbs = st.session_state["earth_kg"] * LB_PER_KG
        val_lbs = st.number_input("Earth weight", min_value=0.0, value=float(shown_lbs), step=0.5, label_visibility="collapsed")
        st.session_state["earth_kg"] = float(val_lbs) / LB_PER_KG

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    st.markdown('<div class="primary">', unsafe_allow_html=True)
    st.button("Sync with NASA")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info">
      Weight is the force of gravity acting on an object. Because planets have different
      masses and sizes, their surface gravity varies.<br><br>
      Your mass remains constant everywhere, but your weight changes based on where you stand.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    earth_kg = st.session_state["earth_kg"]

    if st.session_state["unit"] == "kg":
        out_unit = "KG"
        to_display = lambda xkg: xkg
    else:
        out_unit = "LBS"
        to_display = lambda xkg: xkg * LB_PER_KG

    cA, cB = st.columns(2, gap="large")

    for idx, (name, g, grad) in enumerate(planets):
        factor = g / G_EARTH
        w_out = to_display(earth_kg * factor)
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