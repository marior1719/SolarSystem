import streamlit as st

st.set_page_config(page_title="Solar System Weight Explorer", page_icon="🪐", layout="wide")

# --- CSS MEJORADO ---
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: radial-gradient(1200px 600px at 30% 10%, rgba(255,120,60,0.08), transparent 60%),
                radial-gradient(900px 500px at 80% 30%, rgba(80,160,255,0.08), transparent 55%),
                linear-gradient(180deg, #0b0f17, #0a0d14 60%, #070a10);
    color: #e9eef7;
}

.block-container { 
    padding-top: 3rem; 
    max-width: 1200px; 
}

header {visibility: hidden;}

/* Header */
.header-wrap { 
    display:flex; 
    align-items:center; 
    gap:14px; 
    margin-bottom: 30px; 
}
.logo {
    width:44px; height:44px; border-radius: 14px;
    display:flex; align-items:center; justify-content:center;
    background: rgba(255,120,60,0.12);
    border: 1px solid rgba(255,120,60,0.25);
    font-size: 22px;
}
.title { font-size: 38px; font-weight: 900; margin:0; }
.subtitle { font-size: 14px; color: rgba(233,238,247,0.65); }

/* Estilo de la Card Izquierda (aplicado al contenedor de Streamlit) */
[data-testid="stVerticalBlock"] > div:first-child > [data-testid="stVerticalBlock"] {
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
    margin-bottom: 8px;
}

/* --- FIX RADIO BUTTONS (PILLS) --- */
/* Oculta el label del radio group */
div[data-testid="stRadio"] > label { display: none; }

/* Contenedor de los botones */
div[role="radiogroup"] {
    flex-direction: row !important;
    gap: 10px !important;
}

/* Estilo individual de cada opción */
div[role="radiogroup"] label {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 8px 20px !important;
    color: white !important;
    transition: all 0.3s ease;
}

/* Estilo cuando está seleccionado */
div[role="radiogroup"] label:has(input:checked) {
    border: 1px solid rgba(255,120,60,0.6) !important;
    background: rgba(255,120,60,0.15) !important;
}

/* Quitar el círculo de radio nativo */
div[role="radiogroup"] [data-testid="stWidgetSelectionControl"] {
    display: none;
}

/* Input de número */
.stNumberInput label { display:none !important; }
.stNumberInput input {
    font-size: 32px !important;
    border-radius: 16px !important;
    border: 2px solid rgba(255,120,60,0.4) !important;
    background: rgba(0,0,0,0.2) !important;
    color: white !important;
}

/* Botón */
.stButton button {
    width: 100%;
    padding: 12px;
    border-radius: 14px;
    font-weight: 800;
    border: 0;
    color: #10131a;
    background: linear-gradient(90deg, #ff8a3d, #ff5b62);
}

/* Info box */
.info {
    margin-top: 15px;
    padding: 14px;
    border-radius: 16px;
    border: 1px solid rgba(255,120,60,0.15);
    background: rgba(255,120,60,0.05);
    font-size: 13px;
    color: rgba(233,238,247,0.8);
}

/* Planet cards */
.pcard {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 16px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom: 14px;
}
.p-dot { width: 44px; height: 44px; border-radius: 50%; }
.p-name { font-size: 11px; letter-spacing: 1.2px; text-transform: uppercase; color: rgba(233,238,247,0.5); }
.p-value { font-size: 26px; font-weight: 900; }
.p-unit { font-size: 12px; margin-left: 4px; color: rgba(233,238,247,0.5); }
.p-g { font-size: 11px; color: rgba(233,238,247,0.4); text-align:right; }

</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="header-wrap">
    <div class="logo">🚀</div>
    <div>
        <div class="title">Solar System Weight Explorer</div>
        <div class="subtitle">Discover your weight across the cosmos</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- LÓGICA Y DATOS ---
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

left, right = st.columns([1, 1.5], gap="large")

with left:
    # Usamos un contenedor de Streamlit para que el CSS de la 'card' se aplique correctamente
    with st.container():
        unit = st.radio("Units", ["kg", "lbs"], horizontal=True)
        
        st.markdown('<div class="section-title">Your Earth Weight</div>', unsafe_allow_html=True)
        
        val_default = 50.0 if unit == "kg" else 110.2
        earth_weight = st.number_input("Weight", min_value=0.0, value=val_default, step=0.5)

        st.button("Sync with NASA")

        st.markdown("""
        <div class="info">
            Weight is the force of gravity acting on an object. 
            Your mass remains constant, but weight changes based on the planet's gravity.
        </div>
        """, unsafe_allow_html=True)

with right:
    # Conversiones
    if unit == "kg":
        earth_kg = earth_weight
        out_unit = "KG"
        to_display = lambda x: x
    else:
        earth_kg = earth_weight / 2.20462
        out_unit = "LBS"
        to_display = lambda x: x * 2.20462

    cA, cB = st.columns(2)
    for idx, (name, g, grad) in enumerate(planets):
        factor = g / G_EARTH
        w_out = to_display(earth_kg * factor)
        target = cA if idx % 2 == 0 else cB

        target.markdown(f"""
        <div class="pcard">
            <div style="display:flex; align-items:center; gap:12px;">
                <div class="p-dot" style="background:{grad}; border: 1px solid rgba(255,255,255,0.2);"></div>
                <div>
                    <div class="p-name">{name}</div>
                    <div class="p-value">{w_out:.1f}<span class="p-unit">{out_unit}</span></div>
                </div>
            </div>
            <div class="p-g">Gravity<br>{factor:.3f}G</div>
        </div>
        """, unsafe_allow_html=True)