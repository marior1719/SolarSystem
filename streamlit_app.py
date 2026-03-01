import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Solar System Weight Explorer", page_icon="🪐", layout="wide")

# --- TODO EL CSS INTEGRADO Y CORREGIDO ---
st.markdown("""
<style>
/* 1. Fondo y Base */
.stApp {
    background: radial-gradient(1200px 600px at 30% 10%, rgba(255,120,60,0.08), transparent 60%),
                radial-gradient(900px 500px at 80% 30%, rgba(80,160,255,0.08), transparent 55%),
                linear-gradient(180deg, #0b0f17, #0a0d14 60%, #070a10);
    color: #e9eef7;
}

.block-container { 
    padding-top: 3rem; 
    max-width: 1250px; 
}

header {visibility: hidden;}
#MainMenu, footer { visibility: hidden; }

/* 2. Header Style */
.header-wrap { 
    display:flex; 
    align-items:center; 
    gap:14px; 
    margin-bottom: 35px; 
}
.logo {
    width:44px; height:44px; border-radius: 14px;
    display:flex; align-items:center; justify-content:center;
    background: rgba(255,120,60,0.12);
    border: 1px solid rgba(255,120,60,0.25);
    font-size: 22px;
}
.title { font-size: 38px; font-weight: 900; margin:0; line-height: 1.2; }
.subtitle { font-size: 14px; color: rgba(233,238,247,0.65); }

/* 3. Estilo de la "Card" Izquierda (Contenedor de Inputs) */
[data-testid="stVerticalBlock"] > div:first-child > [data-testid="stVerticalBlock"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 24px;
    padding: 26px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

.section-title {
    font-size: 12px;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: rgba(233,238,247,0.5);
    margin-bottom: 10px;
    font-weight: 700;
}

/* 4. FIX RADIO BUTTONS (PILLS + TEXTO BLANCO) */
div[data-testid="stRadio"] > label { display: none; } /* Oculta label superior */

div[role="radiogroup"] {
    flex-direction: row !important;
    gap: 12px !important;
}

div[role="radiogroup"] label {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 14px !important;
    padding: 10px 22px !important;
    transition: all 0.3s ease;
    cursor: pointer;
}

/* Forzar texto blanco en kg/lbs */
div[role="radiogroup"] label p {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    margin: 0 !important;
}

/* Estado seleccionado */
div[role="radiogroup"] label:has(input:checked) {
    border: 1px solid rgba(255,120,60,0.7) !important;
    background: rgba(255,120,60,0.18) !important;
    box-shadow: 0 0 15px rgba(255,120,60,0.1);
}

/* Ocultar circulito nativo */
div[role="radiogroup"] [data-testid="stWidgetSelectionControl"] {
    display: none;
}

/* 5. Input de peso */
.stNumberInput label { display:none !important; }
.stNumberInput input {
    font-size: 36px !important;
    font-weight: 700 !important;
    border-radius: 16px !important;
    border: 2px solid rgba(255,120,60,0.5) !important;
    background: rgba(0,0,0,0.2) !important;
    color: white !important;
    padding: 15px !important;
}

/* 6. Botón Sync */
.stButton button {
    width: 100%;
    padding: 14px;
    border-radius: 16px;
    font-size: 16px;
    font-weight: 800;
    border: 0;
    color: #0b0f17;
    background: linear-gradient(90deg, #ff8a3d, #ff5b62);
    transition: transform 0.2s ease;
}
.stButton button:hover {
    transform: translateY(-2px);
    color: #000;
}

/* 7. Cuadro de Info */
.info-box {
    margin-top: 20px;
    padding: 18px;
    border-radius: 20px;
    border: 1px solid rgba(255,120,60,0.15);
    background: rgba(255,120,60,0.06);
    font-size: 14px;
    line-height: 1.5;
    color: rgba(233,238,247,0.85);
}

/* 8. Planet cards (Derecha) */
.pcard {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 18px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom: 16px;
    transition: border 0.3s ease;
}
.pcard:hover { border: 1px solid rgba(255,255,255,0.15); }
.p-dot { width: 48px; height: 48px; border-radius: 50%; }
.p-name { font-size: 12px; letter-spacing: 1.4px; text-transform: uppercase; color: rgba(233,238,247,0.5); }
.p-value { font-size: 28px; font-weight: 900; }
.p-unit { font-size: 13px; margin-left: 5px; color: rgba(233,238,247,0.5); }
.p-g { font-size: 12px; color: rgba(233,238,247,0.4); text-align:right; }

</style>
""", unsafe_allow_html=True)

# --- CONTENIDO DE LA APP ---

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

# Datos de Planetas (Nombre, Gravedad m/s2, Gradiente Color)
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

# Layout principal
col_left, col_right = st.columns([1.1, 1.4], gap="large")

with col_left:
    # Este contenedor vacío recibirá el estilo de la "Card" vía CSS
    with st.container():
        # Selección de unidades
        unit = st.radio("Units", ["kg", "lbs"], horizontal=True)
        
        st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Your Earth Weight</div>', unsafe_allow_html=True)
        
        # Input de peso
        default_val = 50.0 if unit == "kg" else 110.2
        earth_weight = st.number_input("Weight Input", min_value=0.0, value=default_val, step=0.5)

        st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)
        st.button("Sync with NASA")

        # Info Box
        st.markdown("""
        <div class="info-box">
            <b>Weight</b> is the force of gravity acting on an object. 
            Because planets have different masses and sizes, their surface gravity varies.<br><br>
            Your <b>mass</b> remains constant everywhere, but your weight changes based on where you stand.
        </div>
        """, unsafe_allow_html=True)

with col_right:
    # Lógica de conversión
    if unit == "kg":
        earth_kg = earth_weight
        out_label = "KG"
        convert = lambda x: x
    else:
        earth_kg = earth_weight / 2.20462
        out_label = "LBS"
        convert = lambda x: x * 2.20462

    # Grid de planetas
    cA, cB = st.columns(2, gap="medium")
    
    for i, (name, g_val, grad) in enumerate(planets):
        factor = g_val / G_EARTH
        w_final = convert(earth_kg * factor)
        
        # Decidir en qué columna va
        target_col = cA if i % 2 == 0 else cB
        
        target_col.markdown(f"""
        <div class="pcard">
            <div style="display:flex; align-items:center; gap:14px;">
                <div class="p-dot" style="background:{grad}; border: 1px solid rgba(255,255,255,0.2);"></div>
                <div>
                    <div class="p-name">{name}</div>
                    <div class="p-value">{w_final:.1f}<span class="p-unit">{out_label}</span></div>
                </div>
            </div>
            <div class="p-g">Gravity<br>{factor:.3f}G</div>
        </div>
        """, unsafe_allow_html=True)