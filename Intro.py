import os
import streamlit as st
from PIL import Image

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", page_icon="🤖", layout="wide")

# -----------------------------
# ESTILOS DEFINITIVOS
# -----------------------------
st.markdown("""
<style>
/* Fondo general */
[data-testid="stAppViewContainer"] {
  background: linear-gradient(180deg, #e8eaff 0%, #f3f8ff 100%);
  font-family: 'Poppins', sans-serif;
  color: #1e2a55;
  padding: 0 3rem 3rem 3rem;
}

/* Barra superior */
[data-testid="stHeader"] {
  background: rgba(250, 248, 255, 0.6);
  backdrop-filter: blur(10px);
  height: 3.2rem;
  border-bottom: 1px solid rgba(180,180,255,0.25);
  box-shadow: 0 2px 6px rgba(100,120,200,0.1);
}

/* Íconos de la barra superior */
[data-testid="stToolbar"] button {
  background-color: rgba(220,230,255,0.85);
  border-radius: 8px;
  padding: 6px;
  transition: all 0.2s ease;
}
[data-testid="stToolbar"] button:hover {
  background-color: rgba(180,200,255,1);
  transform: scale(1.08);
}

/* Título principal */
h1 {
  color: #2b2e83;
  text-align: center;
  font-weight: 700;
  margin-top: 3.5rem;
  margin-bottom: 2.2rem;
}

/* Tarjeta contenedora (todo adentro) */
.card {
  background: #ffffff;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 6px 18px rgba(80, 100, 200, 0.12);
  text-align: center;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100%;
}
.card:hover {
  transform: scale(1.02);
}

/* Imagen dentro del contenedor */
.card img {
  width: 100%;
  border-radius: 16px;
  box-shadow: 0 3px 10px rgba(0,0,0,.08);
  margin-bottom: 14px;
}

/* Título dentro del contenedor */
.card h3 {
  color: #2e2f7f;
  font-weight: 700;
  font-size: 1.05rem;
  margin: 8px 0;
}

/* Descripción dentro del contenedor */
.card p {
  color: #374785;
  font-size: 0.93rem;
  margin-bottom: 12px;
}

/* Botón */
a.btn {
  display: inline-block;
  padding: 0.5rem 1.2rem;
  border-radius: 10px;
  background: linear-gradient(90deg, #a28df4, #8ed9ff);
  color: white;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}
a.btn:hover {
  transform: scale(1.05);
  background: linear-gradient(90deg, #8b7af1, #7ed1ff);
}

/* 🚫 Elimina espacios fantasma encima de las tarjetas */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
  box-shadow: none !important;
  border: none !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TÍTULO PRINCIPAL
# -----------------------------
st.title("🤖 Aplicaciones de Inteligencia Artificial")

# -----------------------------
# DATOS DE LAS 13 APPS
# -----------------------------
apps = [
    {"titulo": "Análisis de datos con agentes", "desc": "Explora cómo los agentes de IA analizan conjuntos de datos.", "img": "cinna5.jpeg", "url": "https://csaj2dyg9tfegdnmzazoku.streamlit.app/"},
    {"titulo": "App de presentación (Intro)", "desc": "Bienvenida y explicación del ecosistema de apps.", "img": "cinna6.jpeg", "url": "https://app1intro-magranador.streamlit.app/"},
    {"titulo": "Control por Voz (MQTT)", "desc": "Envía comandos por voz a sistemas conectados.", "img": "cinna7.jpeg", "url": "https://ctrlvoice-nkp8gyiaogmmye6j8amnpv.streamlit.app/"},
    {"titulo": "Reconocimiento de Dibujos", "desc": "Clasificación/interpretación de trazos a mano alzada.", "img": "cinna8.jpeg", "url": "https://drawrecog-3tp8ojz2qxxpz7vms6nvqm.streamlit.app/"},
    {"titulo": "Texto a Voz (TTS)", "desc": "Convierte texto en audio natural.", "img": "cinna9.jpeg", "url": "https://imm1audio-magranador.streamlit.app/"},
    {"titulo": "Transcriptor Audio/Video", "desc": "Convierte audio o video a texto automáticamente.", "img": "cinna10.jpeg", "url": "https://ocr-audio-ctjjrhqotjwqqgzrvccmaa.streamlit.app/"},
    {"titulo": "Envío MQTT (Remoto)", "desc": "Publica mensajes o valores a dispositivos externos.", "img": "cinna11.jpeg", "url": "https://sendcmqtt-zgsx37r5kvsr7jhhb8nenq.streamlit.app/"},
    {"titulo": "Tablero Inteligente (Canvas IA)", "desc": "Dibuja en lienzo y deja que la IA lo interprete.", "img": "cinna12.jpeg", "url": "https://tablero-naqjzhqlam5e8tjrfjr3pa.streamlit.app/"},
    {"titulo": "Clasificador / ML", "desc": "Modelos de aprendizaje automático para clasificación.", "img": "cinna13.jpeg", "url": "https://tdfesp-pcq8forxath5k242hitumc.streamlit.app/"},
    {"titulo": "Entrenamiento de Modelos", "desc": "Prueba tu modelo entrenado directamente en la app.", "img": "cinna14.jpeg", "url": "https://rw3hbefgecoajdktfhogkq.streamlit.app/"},
    {"titulo": "Detección de Objetos (YOLOv5)", "desc": "Detecta objetos en imágenes en tiempo real.", "img": "cinna15.jpeg", "url": "https://yolov5-ayderaxxdugnijcaux835v.streamlit.app/"},
    {"titulo": "Chat con PDF (RAG)", "desc": "Haz preguntas a tus PDFs y obtén respuestas contextuales.", "img": "cinna16.jpeg", "url": "https://chatpdf-hdadat82ittwff68s5nij8.streamlit.app/"},
    {"titulo": "Traductor Voz ↔ Texto", "desc": "Escucha, traduce y reproduce el resultado.", "img": "cinna17.jpeg", "url": "https://traductor-a6xdrnuxmuxdmjhr3padyv.streamlit.app/"}
]

# -----------------------------
# TARJETAS EN CONTENEDORES (ya sin espacios blancos)
# -----------------------------
cols = st.columns(3, gap="large")

for i, app in enumerate(apps):
    with cols[i % 3]:
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            if os.path.exists(app["img"]):
                st.image(app["img"], use_container_width=True)
            st.markdown(f"<h3>{app['titulo']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{app['desc']}</p>", unsafe_allow_html=True)
            st.markdown(f"<a class='btn' href='{app['url']}' target='_blank'>Abrir app</a>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
