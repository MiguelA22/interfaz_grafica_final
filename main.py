import streamlit as st
import pandas as pd
import requests
import Sintatico
import  Semantica
from Lexico import analizar_ip
import Lexico
from Semantica import clasificar_direcciones_ip
st.set_page_config(page_title="Proyecto Final", page_icon=":robot_face:", layout='wide')

# Función para cargar animaciones
def cargar_animacion(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Animaciones
animacion_uno = "https://lottie.host/97831e48-5eef-498f-979d-49d78dd99d14/10UScZDo1R.json"

# Inicializar la lista de entradas del usuario en la primera ejecución
if 'entradas_usuario' not in st.session_state:
    st.session_state.entradas_usuario = []
# Nuevo contenedor
with st.container():
    st.title('ANALIZADORES LÉXICO Y SINTÁCTICO')

    # Agregar opción para cargar un archivo de texto
    uploaded_file = st.file_uploader("Cargar archivo de texto (.txt)", type=["txt"])

    if uploaded_file is not None:
        # Leer el contenido del archivo de texto y convertirlo a una lista
        content = uploaded_file.read().decode("utf-8")
        entradas_desde_archivo = content.splitlines()

        # Agregar las entradas del archivo a la lista de entradas del usuario
        st.session_state.entradas_usuario.extend(entradas_desde_archivo)
        # Mostrar la lista de entradas del usuario
st.write("Lista de entradas del usuario:")
st.write(st.session_state.entradas_usuario)

# Crear un nuevo contenedor para la tabla
with st.container():
    st.write("Analizador lexico:")

    # Crear un DataFrame a partir de la lista de entradas del usuario
    df = pd.DataFrame(st.session_state.entradas_usuario, columns=["LEXEMAS"])

    # Crear una nueva columna "TABLA DE SIMBOLOS"
    df["TABLA DE SIMBOLOS"] = df["LEXEMAS"].apply((lambda x: analizar_ip(x)[0]))
    # Mostrar el DataFrame como una tabla
    st.table(df)

    st.write("Manejador de errores:")
    df2=pd.DataFrame(st.session_state.entradas_usuario, columns=["LEXEMAS"])
    df2["ERRORES"] = df2["LEXEMAS"].apply((lambda x:analizar_ip(x)[1]))
    st.table(df2)
with (st.container()):
    st.write("Analizador Semantico:")
    #df2=pd.DataFrame(st.session_state.entradas_usuario, columns=["LEXEMAS"])
    #df3 = pd.DataFrame(st.session_state.entradas_usuario, columns=["CLASIFICACION"])
    #from Lexico import evaluarsemantica
    #direccion_ip=[]

    #direccion_ip.append(evaluarsemantica)
    #df3["DIRECCION_IP"]=df3["CLASIFICACION"].apply(lambda x:clasificar_direcciones_ip(evaluarsemantica))
    #st.table(df3)
