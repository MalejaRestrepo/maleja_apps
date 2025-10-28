import os
import streamlit as st
from PIL import Image

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", page_icon="🤖", layout="wide")

# -----------------------------
# Estilos (sin sidebar y sin espacios blancos)
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg,#e8eaff 0%,#f3f8ff 100%);
  font-family:'Poppins',sans-serif; 
  color:#1e2a55;
  padding-left: 3rem;
  padding-right: 3rem;
}
h1,h2,h3{
  color:#2b2e83; 
  text-align:center; 
  font-weight:700; 
  margin-top:0px;
}
.block-container{
  padding-top:1rem; 
  padding-bottom:2rem;
}
.stImage img{
  border-radius:18px; 
  box-shadow:0 4px 12px rgba(0,0,0,.1);
}
.card{
  background:#f8faff;
  border-radius:18px; 
  padding:20px; 
  box-shadow:0 6px 20px rgba(80,100,200,.12);
  transition: transform 0.25s ease;
}
.card:hover{
  transform: scale(1.02);
}
a.btn{
  display:inline-block; 
  margin-top:.6rem; 
  padding:.5rem 1.2rem; 
  border-radius:10px;
  background:linear-gradient(90deg,#a28df4,#8ed9ff); 
  color:white; 
  font-weight:600; 
  text-decoration:none;
}
a.btn:hover{
  transform:scale(1.05); 
  background:linear-gradient(90deg,#8b7af1,#7ed1ff);
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Aplicaciones de Inteligencia Artificial")

# -----------------------------
# Datos de las apps (13)
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
# Mostrar tarjetas sin márgenes extra
# -----------------------------
def show_card(slot, app):
    with slot:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if os.path.exists(app["img"]):
            st.image(Image.open(app["img"]), use_container_width=True)
        else:
            st.markdown("<div style='height:150px;background:#f0f2ff;border-radius:12px;'></div>", unsafe_allow_html=True)
        st.subheader(app["titulo"])
        st.write(app["desc"])
        st.markdown(f"<a class='btn' href='{app['url']}' target='_blank'>Abrir app</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Render
# -----------------------------
cols = st.columns(3, gap="large")
for i, app in enumerate(apps):
    show_card(cols[i % 3], app)
