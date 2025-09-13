import streamlit as st
from streamlit_card import card

# Dos columnas con ancho 1:1
col1, col2 = st.columns(2)

with col1:
    card(
        title="Ejemplo 1",
        text="Esto ya viene con borde y sombra",
        url="https://streamlit.io"
    )
    card(
        title="Ejemplo 2",
        text="Otro card dentro de la misma columna",
        url="https://streamlit.io"
    )

with col2:
    card(
        title="Ejemplo 3",
        text="Card en la segunda columna",
        url="https://streamlit.io"
    )
    card(
        title="Ejemplo 4",
        text="Otro más en col2",
        url="https://streamlit.io"
    )
