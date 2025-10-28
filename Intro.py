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

# --- Estilos perfeccionados ---
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
  margin: 0 !important;
  padding: 0 !important;
  background: linear-gradient(180deg,#e8eaff 0%,#f3f8ff 100%);
  font-family:'Poppins',sans-serif;
  color:#1e2a55;
  overflow-x: hidden !important;
}

/* Barra superior */
[data-testid="stHeader"] {
  background: #d9e1ff !important;
  border: none !important;
  box-shadow: 0 2px 10px rgba(100,120,200,0.15);
  height: 3.5rem;
  padding: 0;
  margin: 0;
  width: 100vw !important;
}
[data-testid="stToolbar"] {
  justify-content: flex-end;
  width: 100%;
  padding-right: 1.5rem;
}
[data-testid="stToolbar"] button {
  background-color: rgba(255,255,255,0.8);
  border-radius: 10px;
  padding: 6px;
  margin-left: 6px;
  transition: all 0.2s ease;
}
[data-testid="stToolbar"] button:hover {
  background-color: rgba(255,255,255,1);
  transform: scale(1.08);
}

/* Título principal */
h1 {
  color:#2b2e83;
  text-align:center;
  font-weight:700;
  margin-top:4.5rem;
  margin-bottom:3rem;
}

/* Tarjeta */
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
