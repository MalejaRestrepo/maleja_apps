import os
import streamlit as st
import base64

st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", page_icon="🤖", layout="wide")

# --- Función para convertir imágenes ---
def img_to_base64(img_path):
    if not os.path.exists(img_path):
        return ""
    with open(img_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# --- Estilos mejorados ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background: linear-gradient(180deg,#e8eaff 0%,#f3f8ff 100%);
  font-family:'Poppins',sans-serif;
  color:#1e2a55;
  padding:0 3rem 3rem 3rem;
}

/* Barra superior */
[data-testid="stHeader"] {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(190,190,255,0.3);
  height: 3rem;
  box-shadow: 0 2px 6px rgba(150,150,200,0.1);
}

/* Título principal */
h1 {
  color:#2b2e83;
  text-align:center;
  font-weight:700;
  margin-top:4rem;
  margin-bottom:3rem;
}

/* Tarjeta general */
.card {
  background:#ffffff;
  border-radius:20px;
  box-shadow:0 6px 20px rgba(80,100,200,0.12);
  padding:25px 20px 30px 20px;
  text-align:center;
  transition:all 0.25s ease;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:space-between;
  height:100%;
}
.card:hover { transform:scale(1.02); }

/* Imagen */
.card img {
  width:100%;
  border-radius:16px;
  margin-bottom:18px;
  box-shadow:0 3px 10px rgba(0,0,0,0.08);
}

/* Título */
.card h3 {
  color:#2b2e83;
  font-weight:700;
  font-size:1.1rem;
  margin-bottom:10px;
  line-height:1.3;
}

/* Descripción */
.card p {
  color:#374785;
  font-size:0.93rem;
  margin-bottom:20px;
  line-height:1.5;
  text-align:center;
}

/* Botón */
.card a {
  display:inline-block;
  padding:0.55rem 1.4rem;
  border-radius:12px;
  background:linear-gradient(90deg,#a28df4,#8ed9ff);
  color:white;
  font-weight:600;
  text-decoration:none;
  transition:all 0.2s ease;
}
.card a:hover {
  transform:scale(1.06);
  background:linear-gradient(90deg,#8b7af1,#7ed1ff);
}

/* Separación entre filas */
[data-testid="stHorizontalBlock"] {
  margin-bottom: 2.5rem !important;
}

/* Elimina contenedores fantasmas */
[data-testid="stVerticalBlockBorderWrapper"], [data-testid="stVerticalBlock"] > div:first-child {
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
  border: none !important;
  box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# --- Título principal ---
st.markdown("<h1>🤖 Aplicaciones de Inteligencia Artificial</h1>", unsafe_allow_html=True)

# --- Lista de apps ---
apps = [
    ("Análisis de datos con agentes", "Explora cómo los agentes de IA analizan conjuntos de datos.", "cinna5.jpeg", "https://csaj2dyg9tfegdnmzazoku.streamlit.app/"),
    ("App de presentación (Intro)", "Bienvenida y explicación del ecosistema de apps.", "cinna6.jpeg", "https://app1intro-magranador.streamlit.app/"),
    ("Control por Voz (MQTT)", "Envía comandos por voz a sistemas conectados.", "cinna7.jpeg", "https://ctrlvoice-nkp8gyiaogmmye6j8amnpv.streamlit.app/"),
    ("Reconocimiento de Dibujos", "Clasificación/interpretación de trazos a mano alzada.", "cinna8.jpeg", "https://drawrecog-3tp8ojz2qxxpz7vms6nvqm.streamlit.app/"),
    ("Texto a Voz (TTS)", "Convierte texto en audio natural.", "cinna9.jpeg", "https://imm1audio-magranador.streamlit.app/"),
    ("Transcriptor Audio/Video", "Convierte audio o video a texto automáticamente.", "cinna10.jpeg", "https://ocr-audio-ctjjrhqotjwqqgzrvccmaa.streamlit.app/"),
    ("Envío MQTT (Remoto)", "Publica mensajes o valores a dispositivos externos.", "cinna11.jpeg", "https://sendcmqtt-zgsx37r5kvsr7jhhb8nenq.streamlit.app/"),
    ("Tablero Inteligente (Canvas IA)", "Dibuja en lienzo y deja que la IA lo interprete.", "cinna12.jpeg", "https://tablero-naqjzhqlam5e8tjrfjr3pa.streamlit.app/"),
    ("Clasificador / ML", "Modelos de aprendizaje automático para clasificación.", "cinna13.jpeg", "https://tdfesp-pcq8forxath5k242hitumc.streamlit.app/"),
    ("Entrenamiento de Modelos", "Prueba tu modelo entrenado directamente en la app.", "cinna14.jpeg", "https://rw3hbefgecoajdktfhogkq.streamlit.app/"),
    ("Detección de Objetos (YOLOv5)", "Detecta objetos en imágenes en tiempo real.", "cinna15.jpeg", "https://yolov5-ayderaxxdugnijcaux835v.streamlit.app/"),
    ("Chat con PDF (RAG)", "Haz preguntas a tus PDFs y obtén respuestas contextuales.", "cinna16.jpeg", "https://chatpdf-hdadat82ittwff68s5nij8.streamlit.app/"),
    ("Traductor Voz ↔ Texto", "Escucha, traduce y reproduce el resultado.", "cinna17.jpeg", "https://traductor-a6xdrnuxmuxdmjhr3padyv.streamlit.app/")
]

# --- Renderizado en filas con espaciado ---
for start in range(0, len(apps), 3):
    cols = st.columns(3, gap="large")
    for i, (titulo, desc, img, url) in enumerate(apps[start:start + 3]):
        img64 = img_to_base64(img)
        with cols[i]:
            st.markdown(f"""
            <div class='card'>
                <img src='{img64}' alt='{titulo}'>
                <h3>{titulo}</h3>
                <p>{desc}</p>
                <a href='{url}' target='_blank'>Abrir app</a>
            </div>
            """, unsafe_allow_html=True)
