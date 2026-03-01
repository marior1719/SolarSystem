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

.block-container { 
  padding-top: 4.5rem; 
  padding-bottom: 2.5rem; 
  max-width: 1250px; 
}

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
  margin-bottom: 12px;
}

.section-gap { height: 18px; }

/* Toggle personalizado */
.toggle {
  display:flex;
  gap:12px;
  margin-bottom:20px;
}
.toggle button {
  padding:10px 20px;
  border-radius:14px;
  border:1px solid rgba(255,255,255,0.15);
  background:rgba(255,255,255,0.05);
  color:white;
  font-weight:600;
  cursor:pointer;
}
.toggle button.active {
  background: linear-gradient(90deg, #ff8a3d, #ff5b62);
  border: none;
  color:#10131a;
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

G_EARTH = 9.80665

planets = [
    ("Mercury", 3.70, "#8a95a6"),
    ("Venus", 8.87, "#ffb25a"),
    ("Earth", 9.80665, "#2bd0ff"),
    ("Mars", 3.71, "#ff8b4a"),
    ("Jupiter", 24.79, "#ffb15a"),
    ("Saturn", 10.44, "#ffd56a"),
    ("Uranus", 8.69, "#7de7ff"),
    ("Neptune", 11.15, "#6b86ff"),
]

left, right = st.columns([1.05, 1.45], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Toggle manual limpio
    unit = st.radio("", ["kg", "lbs"], horizontal=True)

    st.markdown('<div class="section-title">Your Earth Weight</div>', unsafe_allow_html=True)

    if unit == "kg":
        earth_weight = st.number_input("", min_value=0.0, value=50.0, step=0.5)
    else:
        earth_weight = st.number_input("", min_value=0.0, value=110.2, step=0.5)

    st.button("Sync with NASA")

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if unit == "kg":
        earth_kg = earth_weight
        out_unit = "KG"
        to_display = lambda xkg: xkg
    else:
        earth_kg = earth_weight / 2.2046226218
        out_unit = "LBS"
        to_display = lambda xkg: xkg * 2.2046226218

    col1, col2 = st.columns(2, gap="large")

    for idx, (name, g, color) in enumerate(planets):
        factor = g / G_EARTH
        w_out = to_display(earth_kg * factor)
        target = col1 if idx % 2 == 0 else col2

        with target:
            st.markdown(f"""
            <div class="pcard">
              <div class="p-left">
                <div class="p-dot" style="background:{color};"></div>
                <div>
                  <div class="p-name">{name}</div>
                  <div class="p-value">{w_out:.1f}<span class="p-unit">{out_unit}</span></div>
                </div>
              </div>
              <div class="p-g">Gravity:<br>{factor:.3f}G</div>
            </div>
            """, unsafe_allow_html=True)