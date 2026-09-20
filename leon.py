import streamlit as st
from datetime import datetime

# Configuración de la página (Limpia y profesional)
st.set_page_config(page_title="Grupo León - Tartagal", page_icon="🦁", layout="wide")

# 🚨 DEFINICIÓN GLOBAL SEGURA DEL WHATSAPP
NUMERO_WHATSAPP_OFICINA = "5493873000000"

# --- ESTILOS GENERALES COMPACTOS ---
st.markdown("""
    <style>
    header[data-testid="stHeader"], footer { display: none !important; }
    .main .block-container { padding-top: 2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CONTROL DE NAVEGACIÓN (SESIÓN VIVA) ---
if "seccion_activa" not in st.session_state:
    st.session_state["seccion_activa"] = "Portal Central"

def cambiar_seccion(nombre_seccion):
    st.session_state["seccion_activa"] = nombre_seccion

# =========================================================================
# 🏛️ 1. PORTAL CENTRAL: GRUPO LEÓN
# =========================================================================
if st.session_state["seccion_activa"] == "Portal Central":
    
    # Encabezado Corporativo Sobrio
    st.write("<h1 style='text-align: center; color: #1E293B; font-family: sans-serif; font-size: 3rem; margin-bottom: 0;'>GRUPO LEÓN</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; color: #64748B; font-size: 1.2rem; font-style: italic;'>Un sello de confianza, salud y sabor en Tartagal.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("<h3 style='text-align: center; color: #475569;'>Seleccione la unidad de negocio que desea consultar:</h3>", unsafe_allow_html=True)
    st.write("")
    
    # Dibujamos las 3 Tarjetas en Fila Prolija
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background-color: #F8FAFC; border-left: 5px solid #2563EB; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); height: 260px;'>
                <h3 style='color: #1E40AF; margin-top:0;'>⚕️ FARMACIA LEÓN</h3>
                <p style='color: #475569; font-size: 0.95rem; line-height: 1.4;'>Compromiso con el cuidado de tu salud. Atención profesional, Obras Sociales y recepción digital de recetas en Tartagal.</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Ingresar a Farmacia ➡️", key="btn_farmacia", use_container_width=True):
            cambiar_seccion("Farmacia")
            st.rerun()

    with col2:
        st.markdown("""
            <div style='background-color: #F8FAFC; border-left: 5px solid #D97706; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); height: 260px;'>
                <h3 style='color: #92400E; margin-top:0;'>🥖 PANADERÍA LEÓN</h3>
                <p style='color: #475569; font-size: 0.95rem; line-height: 1.4;'>La tradición artesanal en tu mesa. Elaboración diaria de panificación fresca, facturas, masas finas y servicio de catering para eventos.</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Ingresar a Panadería ➡️", key="btn_panaderia", use_container_width=True):
            cambiar_seccion("Panadería")
            st.rerun()

    with col3:
        st.markdown("""
            <div style='background-color: #F8FAFC; border-left: 5px solid #DB2777; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); height: 260px;'>
                <h3 style='color: #9D174D; margin-top:0;'>🫖 CEREZO (Casa de Té)</h3>
                <p style='color: #475569; font-size: 0.95rem; line-height: 1.4;'>Un rincón pensado para pausar el día. Disfrutá de nuestra exclusiva selección de tés, pastelería boutique y meriendas únicas.</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Ingresar a Cerezo ➡️", key="btn_cerezo", use_container_width=True):
            cambiar_seccion("Cerezo")
            st.rerun()

    st.write("")
    st.write("")
    st.markdown("---")
    st.caption("<p style='text-align: center; color: #94A3B8;'>© 2026 Grupo León - Desarrollado por Soluciones Digitales Tartagal.</p>", unsafe_allow_html=True)

# =========================================================================
# ⚕️ 2. SUBPÁGINA: FARMACIA LEÓN (Estilo Limpio / Azul)
# =========================================================================
elif st.session_state["seccion_activa"] == "Farmacia":
    
    if st.button("⬅️ Volver al Portal General", key="back_f"):
        cambiar_seccion("Portal Central")
        st.rerun()
        
    st.write("<h1 style='color: #1E40AF; font-family: sans-serif;'>⚕️ Farmacia León</h1>", unsafe_allow_html=True)
    st.write("### Cuidamos lo más importante: Tu Salud.")
    st.markdown("---")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.info("🕒 **Horarios de Atención:**\n\nLunes a Sábados: 08:00 a 13:00 y 17:00 a 21:00 hs.\n\n*Consulte turnos de guardia los fines de semana.*")
        st.write("📍 **Ubicación:** Centro, Tartagal, Salta.")
        st.write("💳 **Medios de Pago:** Efectivo, Tarjetas de Crédito/Débito y Transferencias.")
        
    with col_f2:
        st.subheader("📲 Ventanilla Digital de Recetas")
        st.write("Ganale tiempo al día. Mandanos la foto de tu receta u orden médica por WhatsApp, te cotizamos los medicamentos y te los dejamos separados para que solo pases a retirar.")
        
        link_wa = f"https://wa.me{NUMERO_WHATSAPP_OFICINA}?text=Hola%20Farmacia%20León,%20quiero%20enviar%20una%20receta"
        st.link_button("💬 ENVIAR RECETA POR WHATSAPP", link_wa, type="primary")

# =========================================================================
# 🥖 3. SUBPÁGINA: PANADERÍA LEÓN (Estilo Cálido / Marrón)
# =========================================================================
elif st.session_state["seccion_activa"] == "Panadería":
    
    if st.button("⬅️ Volver al Portal General", key="back_p"):
        cambiar_seccion("Portal Central")
        st.rerun()
        
    st.write("<h1 style='color: #92400E; font-family: sans-serif;'>🥖 Panadería León</h1>", unsafe_allow_html=True)
    st.write("### El sabor de la tradición, horneado fresco cada mañana.")
    st.markdown("---")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write("🥐 **Nuestras Especialidades del Día:**")
        st.markdown("* Pan Casero e Industrial calentito\n* Facturas de manteca y grasa hechas a mano\n* Masas finas y Tortas de cumpleaños por encargo\n* Sándwiches de miga triples especiales")
        st.write("")
        st.write("📍 **Encontranos en:** Tartagal, Salta.")
        
    with col_p2:
        st.subheader("🎂 Pedidos para Eventos y Confitería")
        st.write("¿Tenés un cumpleaños, bautismo o reunión familiar? Hacé tu pedido de catering (sándwiches, pizzetas y masas) de forma anticipada y retiralo listo para servir.")
        
        link_wa_pan = f"https://wa.me{NUMERO_WHATSAPP_OFICINA}?text=Hola%20Panadería%20León,%20quiero%20hacer%20un%20pedido"
        st.link_button("🍞 ENCARGAR PEDIDO POR WHATSAPP", link_wa_pan, type="secondary")

# =========================================================================
# 🫖 4. SUBPÁGINA: CEREZO CASA DE TÉ (Estilo Elegante / Rosa Viejo)
# =========================================================================
elif st.session_state["seccion_activa"] == "Cerezo":
    
    if st.button("⬅️ Volver al Portal General", key="back_c"):
        cambiar_seccion("Portal Central")
        st.rerun()
        
    st.write("<h1 style='color: #9D174D; font-family: sans-serif;'>🫖 Cerezo • Casa de Té</h1>", unsafe_allow_html=True)
    st.write("### Un rincón exclusivo pensado para pausar el día y compartir.")
    st.markdown("---")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.write("☕ **La Experiencia Cerezo:**")
        st.write("Diseñamos un ambiente tranquilo, climatizado y con música suave para que disfrutes de un momento único en la ciudad.")
        st.markdown("🍰 *Pastelería fina boutique, blends de té en hebras nacionales e importados, cafetería de especialidad y opciones saladas gourmet.*")
        st.write("")
        st.write("📍 **Ubicación del Salón:** Tartagal, Salta.")
        
    with col_c2:
        st.subheader("📅 Reserva tu Mesa Especial")
        st.write("Nuestros cupos en el salón son limitados para garantizar la tranquilidad de la experiencia. Reservá tu mesa para merendar o celebrar una tarde especial con amigas.")
        
        link_wa_te = f"https://wa.me{NUMERO_WHATSAPP_OFICINA}?text=Hola%20Cerezo,%20quiero%20reservar%20una%20mesa"
        st.link_button("🌸 RESERVAR MESA POR WHATSAPP", link_wa_te)
