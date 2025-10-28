import os
import streamlit as st
from PIL import Image

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", page_icon="🤖", layout="wide")

# -----------------------------
# Estilos (pasteles fríos)
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg,#e8eaff 0%,#f3f8ff 100%);
  font-family:'Poppins',sans-serif; color:#1e2a55;
}
h1,h2,h3{color:#3a3d9a; text-align:center; font-weight:700;}
.block-container{padding-top:2rem; padding-bottom:2rem;}
.stImage img{border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,.1);}
.card{background:#ffffff; border:1px solid #cfe0ff; border-radius:14px; padding:14px;
      box-shadow:0 8px 18px rgba(62,76,131,.08);}
a.btn{display:inline-block; margin-top:.35rem; padding:.45rem 1rem; border-radius:10px;
      background:linear-gradient(90deg,#a28df4,#8ed9ff); color:white; font-weight:600; text-decoration:none;}
a.btn:hover{transform:scale(1.03); background:linear-gradient(90deg,#8b7af1,#7ed1ff);}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Aplicaciones de Inteligencia Artificial")

# Sidebar
with st.sidebar:
    st.subheader("🌐 Sobre estas aplicaciones")
    st.write(
        "La inteligencia artificial mejora la toma de decisiones con datos, automatiza tareas y "
        "ofrece análisis avanzados en tiempo real para aumentar la eficiencia y la precisión."
    )
    st.markdown("📘 [Ejercicios y páginas complementarias](https://sites.google.com/view/aplicacionesdeia/inicio)")

# -----------------------------
# Datos de las apps (13)
# -----------------------------
apps = [
    {
        "titulo": "Análisis de datos con agentes",
        "desc":   "Explora cómo los agentes de IA analizan conjuntos de datos.",
        "img":    "cinna5.jpeg",
        "url":    "https://csaj2dyg9tfegdnmzazoku.streamlit.app/"
    },
    {
        "titulo": "App de presentación (Intro)",
        "desc":   "Bienvenida y explicación del ecosistema de apps.",
        "img":    "cinna6.jpeg",
        "url":    "https://app1intro-magranador.streamlit.app/"
    },
    {
        "titulo": "Control por Voz (MQTT)",
        "desc":   "Envía comandos por voz a sistemas conectados.",
        "img":    "cinna7.jpeg",
        "url":    "https://ctrlvoice-nkp8gyiaogmmye6j8amnpv.streamlit.app/"
    },
    {
        "titulo": "Reconocimiento de Dibujos",
        "desc":   "Clasificación/interpretación de trazos a mano alzada.",
        "img":    "cinna8.jpeg",
        "url":    "https://drawrecog-3tp8ojz2qxxpz7vms6nvqm.streamlit.app/"
    },
    {
        "titulo": "Texto a Voz (TTS)",
        "desc":   "Convierte texto en audio natural.",
        "img":    "cinna9.jpeg",
        "url":    "https://imm1audio-magranador.streamlit.app/"
    },
    {
        "titulo": "Transcriptor Audio/Video",
        "desc":   "Convierte audio o video a texto automáticamente.",
        "img":    "cinna10.jpeg",
        "url":    "https://ocr-audio-ctjjrhqotjwqqgzrvccmaa.streamlit.app/"
    },
    {
        "titulo": "Envío MQTT (Remoto)",
        "desc":   "Publica mensajes o valores a dispositivos externos.",
        "img":    "cinna11.jpeg",
        "url":    "https://sendcmqtt-zgsx37r5kvsr7jhhb8nenq.streamlit.app/"
    },
    {
        "titulo": "Tablero Inteligente (Canvas IA)",
        "desc":   "Dibuja en lienzo y deja que la IA lo interprete.",
        "img":    "cinna12.jpeg",
        "url":    "https://tablero-naqjzhqlam5e8tjrfjr3pa.streamlit.app/"
    },
    {
        "titulo": "Clasificador / ML",
        "desc":   "Modelos de aprendizaje automático para clasificación.",
        "img":    "cinna13.jpeg",
        "url":    "https://tdfesp-pcq8forxath5k242hitumc.streamlit.app/"
    },
    {
        "titulo": "Entrenamiento de Modelos",
        "desc":   "Prueba tu modelo entrenado directamente en la app.",
        "img":    "cinna14.jpeg",
        "url":    "https://rw3hbefgecoajdktfhogkq.streamlit.app/"
    },
    {
        "titulo": "Detección de Objetos (YOLOv5)",
        "desc":   "Detecta objetos en imágenes en tiempo real.",
        "img":    "cinna15.jpeg",
        "url":    "https://yolov5-ayderaxxdugnijcaux835v.streamlit.app/"
    },
    {
        "titulo": "Chat con PDF (RAG)",
        "desc":   "Haz preguntas a tus PDFs y obtén respuestas contextuales.",
        "img":    "cinna16.jpeg",
        "url":    "https://chatpdf-hdadat82ittwff68s5nij8.streamlit.app/"
    },
    {
        "titulo": "Traductor Voz ↔ Texto",
        "desc":   "Escucha, traduce y reproduce el resultado.",
        "img":    "cinna17.jpeg",
        "url":    "https://traductor-a6xdrnuxmuxdmjhr3padyv.streamlit.app/"
    },
]

# -----------------------------
# Helper para tarjetas
# -----------------------------
def show_card(slot, app):
    with slot:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(app["titulo"])
        if os.path.exists(app["img"]):
            st.image(Image.open(app["img"]), use_container_width=True)
        else:
            # Fondo degradado si falta la imagen
            st.markdown("""
                <div style='height:140px; border-radius:12px;
                            background:linear-gradient(90deg,#e8ebff,#f3f5ff);
                            display:flex; align-items:center; justify-content:center;
                            color:#5c6bc0; font-weight:600; font-size:14px;'>
                    Imagen no disponible
                </div>
            """, unsafe_allow_html=True)
        st.write(app["desc"])
        st.markdown(f"<a class='btn' href='{app['url']}' target='_blank'>Abrir app</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Render en 3 columnas (13 items)
# -----------------------------
cols = st.columns(3, gap="large")
for i, app in enumerate(apps):
    show_card(cols[i % 3], app)
