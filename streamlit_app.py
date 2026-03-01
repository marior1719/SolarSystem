import streamlit as st

st.set_page_config(page_title="Solar System Weight Explorer", page_icon="🪐", layout="wide")

st.markdown("""
<style>
.stApp {
  background: radial-gradient(1200px 600px at 30% 10%, rgba(255,120,60,0.08), transparent 60%),
              radial-gradient(900px 500px at 80% 30%, rgba(80,160,255,0.08), transparent 55%),
              linear-gradient(180deg, #0b0f17, #0a0d14 60%, #070a10);
  color: #e9eef7;
}

/* Baja todo un poco más */
.block-container { 
  padding-top: 3.8rem; 
  padding-bottom: 2.6rem; 
  max-width: 1250px; 
}

/* Header */
.header-wrap { display:flex; align-items:center; gap:14px; margin-bottom: 26px; }
.logo {
  width:44px; height:44px; border-radius: 14px;
  display:flex; align-items:center; justify-content:center;
  background: rgba(255,120,60,0.12);
  border: 1px solid rgba(255,120,60,0.25);
  box-shadow: 0 0 0 1px rgba(255,120,60,0.10) inset;
  font-size: 22px;
}
.title { font-size: 42px; font-weight: 900; line-height:1.0; margin:0; }
.subtitle { margin-top: 2px; font-size: 14px; color: rgba(233,238,247,0.65); }

/* Cards */
.card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 22px;
  padding: 18px 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}
.card-title {
  font-size: 13px;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: rgba(233,238,247,0.70);
  display:flex; align-items:center; gap:10px;
  margin-bottom: 14px;
}
.section-gap { height: 14px; }

/* Radio pills (kg / lbs) */
div[role="radiogroup"] { gap: 10px; }
div[role="radiogroup"] label {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 14px;
  padding: 10px 14px;
}
div[role="radiogroup"] label:hover { border-color: rgba(255,255,255,0.18); }

/* Input grande y sin label para evitar desacomodos */
.stNumberInput label { display:none !important; }
.stNumberInput input {
  font-size: 34px !important;
  text-align: left !important;
  padding: 14px 14px !important;
  border-radius: 16px !important;
  border: 2px solid rgba(255,120,60,0.55) !important;
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
  box-shadow: 0 12px 30px rgba(255,100,80,0.25);
}
.stButton button:hover { filter: brightness(1.05); }

/* Caja info */
.info {
  margin-top: 14px;
  padding: 14px 14px;
  border-radius: 18px;
  border: 1px solid rgba(255,120,60,0.18);
  background: rgba(255,120,60,0.06);
  color: rgba(233,238,247,0.82);
  font-size: 14px;
  line-height: 1.45;
}

/* Planet cards con separación */
.pcard {
  background: rgba(255,255,255,0.035);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 18px;
  padding: 14px 16px;
  box-shadow: 0 10px 26px rgba(0,0,0,0.30);
  display:flex;
  align-items:center;
  justify-content:space-between;
  min-height: 84px;
  margin-bottom: 16px;
}
.p-left { display:flex; align-items:center; gap:14px; }
.p-dot {
  width: 46px; height: 46px; border-radius: 999px;
  box-shadow: 0 10px 22px rgba(0,0,0,0.35);
  border: 1px solid rgba(255,255,255,0.16);
}
.p-name {
  font-size: 12px;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  color: rgba(233,238,247,0.70);
  margin-bottom: 4px;
}
.p-value { font-size: 30px; font-weight: 900; line-height: 1.0; }
.p-unit { font-size: 12px; color: rgba(233,238,247,0.65); font-weight: 700; margin-left: 6px; }
.p-g {
  font-size: 12px;
  color: rgba(233,238,247,0.55);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  text-align: right;
}

/* Limpia menú/footer */
#MainMenu, footer { visibility: hidden; }
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
    ("Mercury", 3.70,    "linear-gradient(145deg, #8a95a6, #2f3540)"),
    ("Venus",   8.87,    "linear-gradient(145deg, #ffb25a, #b85a11)"),
    ("Earth",   9.80665, "linear-gradient(145deg, #2bd0ff, #1f3cff)"),
    ("Mars",    3.71,    "linear-gradient(145deg, #ff8b4a, #b2321f)"),
    ("Jupiter", 24.79,   "linear-gradient(145deg, #ffb15a, #8a3a14)"),
    ("Saturn",  10.44,   "linear-gradient(145deg, #ffd56a, #b78522)"),
    ("Uranus",  8.69,    "linear-gradient(145deg, #7de7ff, #1b6b7a)"),
    ("Neptune", 11.15,   "linear-gradient(145deg, #6b86ff, #1430b3)"),
]

# Layout
left, right = st.columns([1.05, 1.45], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="card-title">🧮 <span>Your Earth Weight</span></div>', unsafe_allow_html=True)

    unit = st.radio("Units", ["kg", "lbs"], horizontal=True, label_visibility="collapsed")

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    if unit == "kg":
        earth_weight = st.number_input("Earth weight", min_value=0.0, value=50.0, step=0.5, label_visibility="collapsed")
    else:
        earth_weight = st.number_input("Earth weight", min_value=0.0, value=110.2, step=0.5, label_visibility="collapsed")

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    st.button("Sync with NASA")

    st.markdown("""
    <div class="info">
      <b>Weight</b> is the force of gravity acting on an object. Because planets have different
      masses and sizes, their surface gravity varies.<br><br>
      Your <b>mass</b> remains constant everywhere, but your <b>weight</b> changes based on where you stand.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    # Convertir a kg base
    if unit == "kg":
        earth_kg = earth_weight
        out_unit = "KG"
        to_display = lambda xkg: xkg
    else:
        earth_kg = earth_weight / 2.2046226218
        out_unit = "LBS"
        to_display = lambda xkg: xkg * 2.2046226218

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