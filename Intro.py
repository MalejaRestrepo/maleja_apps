import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #e8eaff 0%, #f3f8ff 100%);
        font-family: 'Poppins', sans-serif;
        color: #1e2a55;
    }
    h1, h2, h3 {
        color: #3a3d9a;
        text-align: center;
        font-weight: 700;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stImage img {
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background: linear-gradient(90deg, #a28df4, #8ed9ff);
        border: none;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.4rem 1.2rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        background: linear-gradient(90deg, #8b7af1, #7ed1ff);
    }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO PRINCIPAL ---
st.title("🤖 Aplicaciones de Inteligencia Artificial")

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("🌐 Aplicaciones con Inteligencia Artificial")
    st.write("""
    La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos,
    automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real,
    logrando mayor eficiencia y precisión en diversos campos.
    """)
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"📘 [Ejercicios prácticos y páginas complementarias]({url_ia})")

# --- COLUMNAS ---
col1, col2, col3 = st.columns(3, gap="large")

# --- COLUMNA 1 ---
with col1:
    st.subheader("🗣️ Conversión de texto a voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=200)
    st.write("Convierte texto en voz natural con inteligencia artificial.")
    st.markdown("[Abrir app](https://imm1audio-magranador.streamlit.app/)")

    st.subheader("🎯 Reconocimiento de objetos (YOLO)")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Detecta objetos en imágenes con visión por computadora.")
    st.markdown("[Abrir app](https://yolov5-ayderaxxdugnijcaux835v.streamlit.app/)")

    st.subheader("🤖 Entrenando modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Entrena y prueba modelos personalizados de IA.")
    st.markdown("[Abrir app](https://rw3hbefgecoajdktfhogkq.streamlit.app/)")

# --- COLUMNA 2 ---
with col2:
    st.subheader("🎧 Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Transcribe lo que hablas en texto en tiempo real.")
    st.markdown("[Abrir app](https://traductor-a6xdrnuxmuxdmjhr3padyv.streamlit.app/)")

    st.subheader("📊 Análisis de datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=200)
    st.write("Explora cómo los agentes de IA analizan conjuntos de datos.")
    st.markdown("[Abrir app](https://csaj2dyg9tfegdnmzazoku.streamlit.app/)")

    st.subheader("📝 Transcriptor de audio y video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Convierte audio o video en texto automáticamente.")
    st.markdown("[Abrir app](https://ocr-audio-ctjjrhqotjwqqgzrvccmaa.streamlit.app/)")

# --- COLUMNA 3 ---
with col3:
    st.subheader("📚 Generación en contexto (RAG)")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=200)
    st.write("Pregunta a tus documentos PDF y obtén respuestas inteligentes.")
    st.markdown("[Abrir app](https://chatpdf-hdadat82ittwff68s5nij8.streamlit.app/)")

    st.subheader("🧠 Análisis de imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Analiza e interpreta imágenes mediante modelos visuales avanzados.")
    st.markdown("[Abrir app](https://drawrecog-3tp8ojz2qxxpz7vms6nvqm.streamlit.app/)")

    st.subheader("⚙️ Sistema ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Control e interacción entre sistemas físicos e inteligencia artificial.")
    st.markdown("[Abrir app](https://ctrlvoice-nkp8gyiaogmmye6j8amnpv.streamlit.app/)")
