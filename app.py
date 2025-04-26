import streamlit as st
import pandas as pd

#SETUP DE LA APP
# De layout podemos usar wide or centered
st.set_page_config(page_title="Mi primera app", page_icon=":tada:", layout="centered")

st.title("Mi primera app") # Titulo de la app

st.header("Encabezado de la app") # Encabezado de la app
st.subheader("Subtitulo de la app") # Subtitulo de la app

st.text("Texto de la app") # Texto de la app
st.markdown("Hello **mundo**") # Texto en markdown

st.latex(r"""a^2 + b^2 = c^2""") # Ecuacion en latex
st.code("print('Hello world')", language="python") # Codigo en python

st.info("Esto es un mensaje de info") # Mensaje de info
st.success("Esto es un mensaje de exito") # Mensaje de exito 
st.warning("Esto es un mensaje de advertencia") # Mensaje de advertencia
st.error("Esto es un mensaje de error") # Mensaje de error
st.exception("Esto es un mensaje de excepcion") # Mensaje de excepcion



st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit") # Imagen de streamlit
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_container_width=True) # Imagen de streamlit con ancho de columna




st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3") # Audio de streamlit
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") # Video de streamlit



df = pd.DataFrame({
    "Nombre": ["Juan", "Pedro", "Maria", "Ana"],
    "Edad": [20, 30, 25, 35],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}) # Dataframe de pandas    

st.dataframe(df) # Dataframe de pandas



# Sidebar de streamlit 
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) # Imagen de streamlit en el sidebar
st.sidebar.text("Desliza") # Texto en el sidebar