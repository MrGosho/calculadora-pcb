import streamlit as st
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora de Ancho de Pista PCB", page_icon="⚡", layout="centered")

st.title("⚡ Calculadora de Ancho de Pista PCB (IPC-2221)")
st.write("Herramienta rápida para ingenieros y diseñadores de hardware. Calcula el grosor de cobre ideal para evitar sobrecalentamiento.")

# --- BARRA LATERAL: PARÁMETROS ---
st.sidebar.header("Parámetros del Circuito")
corriente = st.sidebar.slider("Corriente (Amperes):", min_value=0.1, max_value=15.0, value=2.0, step=0.1)
delta_temp = st.sidebar.slider("Aumento máx. de temperatura (°C):", min_value=5, max_value=50, value=10, step=1)
peso_cobre = st.sidebar.selectbox("Grosor del cobre (Peso):", options=["0.5 oz (17.5 µm)", "1.0 oz (35 µm)", "2.0 oz (70 µm)"], index=1)
capa = st.sidebar.radio("Ubicación de la pista:", options=["Capa Externa", "Capa Interna"])

# --- CÁLCULOS TÉCNICOS (Norma IPC-2221) ---
k = 0.048 if capa == "Capa Externa" else 0.024
if "1.0" in peso_cobre:
    espesor_mil = 1.378
elif "0.5" in peso_cobre:
    espesor_mil = 0.689
else:
    espesor_mil = 2.756

area_mils2 = (corriente / (k * (delta_temp ** 0.44))) ** (1 / 0.725)
ancho_mils = area_mils2 / espesor_mil
ancho_mm = ancho_mils * 0.0254

# --- CUERPO PRINCIPAL: RESULTADOS ---
st.markdown("---")
st.subheader("📊 Resultados del Cálculo")

col1, col2 = st.columns(2)
col1.metric(label="Ancho Mínimo Recomendado", value=f"{ancho_mm:.3f} mm", delta=f"{ancho_mils:.1f} mils")
col2.metric(label="Área de la sección transversal", value=f"{area_mils2:.1f} mil²")

# Cuadro informativo de ayuda visual
if ancho_mm < 0.2:
    st.warning("⚠️ **Precaución:** El ancho calculado es menor a 0.2 mm. Asegúrate de que las capacidades de tu fabricante de PCB soporten pistas tan finas.")
else:
    st.success("✅ **Diseño seguro:** Este ancho de pista cumple con los parámetros estándar de seguridad térmica.")

st.info("💡 **Referencia rápida:** 1 mil = 0.0254 mm (10 mils ≈ 0.25 mm).")

# --- SECCIÓN DE MONETIZACIÓN / AFILIADOS ---
st.markdown("---")
st.markdown("### 🛠️ ¿Listo para mandar a fabricar tu tarjeta?")
st.write("Envía tus archivos Gerber a producción con fabricantes recomendados y obtén descuentos exclusivos para nuevos usuarios:")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 🟢 JLCPCB")
    st.write("Fabricación rápida de PCBs y prototipos SMT.")
    # Aquí irá tu enlace de referido personal de JLCPCB
    st.link_button("Cotizar en JLCPCB", "https://jlcpcb.com/promotions/referral", type="secondary")

with col_b:
    st.markdown("#### 🔵 PCBWay")
    st.write("Excelente calidad en circuitos multicapa y servicio CNC.")
    # Aquí irá tu enlace de referido personal de PCBWay
    st.link_button("Cotizar en PCBWay", "https://www.pcbway.com", type="secondary")

st.markdown("---")
st.caption("Desarrollado para la comunidad de ingeniería electrónica 🚀")