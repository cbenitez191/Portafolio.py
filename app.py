import streamlit as st
import streamlit_shadcn_ui as ui

resume_file = "assets/pdf/CV_Carlos-Benitez.pdf"
resume_file_name = "CV_Carlos-Benitez.pdf"
profile_pic = "assets/img/Perfil.jpeg"
ccs_file = "styles/main.css"
layout = "centered"
page_title = "Portafolio| Carlos Benitez"
page_icon = ""
name = "Carlos Benitez"
description = """
Más de 6 años de experiencia en la administración y soporte de infraestructuras de redes de datos,
 con un sólido dominio en entornos Windows Server y Linux. He liderado el diseño, desarrollo e 
 implementación de sistemas críticos, garantizando su estabilidad, seguridad y rendimiento. Mi 
 trayectoria incluye la implementación de soluciones para proteger información sensible y mitigar 
 amenazas digitales. Altamente comprometido con el aprendizaje continuo, aportando valor y mejorando 
 mis habilidades para contribuir al éxito de cada proyecto en el que participo. 
"""
email = "📨 cbenitez191@gmail.com"
social_media = {
    "Youtube": "https://www.youtube.com/watch?v=RP_bO_IzQ5k",
    "LinkedIn": "",
    "Github": "",
    "Instagram": "",
}

proyectos = {
    "🏆 Aplicación de facturación - Aplicación web para automatizar la facturación de negocios":
    "https://www.youtube.com/waxajdljd",
    "🏆 Aplicación de facturación frwgwrb - Aplicación web para automatizar la facturación de negocios":
    "https://www.youtube.com/waxajdljdfwergew",
    "🏆 Aplicación de diccionario y password":
    "https://google.com",
}

# --- CONF PAGINA ---
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# --- Cargar css y lectura pdf ---
with open(ccs_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Links redes sociales ---
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn_{platform}")

# --- Cabecera ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=300, use_column_width=False)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Descargar CV",
        data=PDFbyte,
        file_name=resume_file_name,
    )
    st.write("", email)

# --- Proyectos ---
st.write('##')
st.subheader("Proyectos")
st.write("---")

for project, link in proyectos.items():
    st.write(f"[{project}]({link})")

# --- Habilidades ---
st.write('##')
st.subheader("Habilidades técnicas")
st.write("---")
st.write(
    """
- 🖥️ Programación: Python, Javascript, VBA, C#
- 🧑‍💻 Software: UiPath, Blue Prism, Power Automate
-
"""
)

# --- Experiencia ---
st.write('##')
st.subheader("Experiencia")
st.write("---")

# --- Trabajo 1 ---
st.write("💼", "**Ingeniero de proyectos**")
st.write("09/2018 - Actual")
st.write(
    """
- ▶️ Automatización de procesos con Python y Power
- ▶️ Desarrollo de APIs
- ▶️ Optimización de procesos con desarrollo en aplicaciones
- ▶️ Visualización de datos Power BI
"""
)

# --- Trabajo 2 ---
st.write('##')
st.write("💼", "**Ingeniero de proyectos**")
st.write("09/2018 - Actual")
st.write(
    """
- ▶️ Automatización de procesos con Python y Power
- ▶️ Desarrollo de APIs
- ▶️ Optimización de procesos con desarrollo en aplicaciones
- ▶️ Visualización de datos Power BI
"""
)
