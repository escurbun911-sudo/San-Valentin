import streamlit as st

st.title("¿Quieres ser mi San Valentín? ❤️")

# 1. Variables de estado
if 'size_si' not in st.session_state:
    st.session_state.size_si = 16
if 'size_no' not in st.session_state:
    st.session_state.size_no = 16
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0

# 2. Lista de frases para el botón NO
frases_no = [
    "No",
    "¿Segura? 🥺",
    "¿Muy segura? 🧐",
    "Piénsalo bien...",
    "¡Te daré chocolates! 🍫",
    "¿Y si te lo pido por favor? ✨",
    "¡Anda, di que sí!",
    "Última oportunidad..."
]

# Seleccionamos la frase según el número de clics
texto_no = frases_no[st.session_state.intentos % len(frases_no)]

# 3. Botón SÍ
with st.container():
    st.markdown(f"""
        <style>
        div[data-testid="stVerticalBlock"] > div:nth-child(2) button {{
            font-size: {st.session_state.size_si}px !important;
            background-color: #28a745 !important;
            color: white !important;
            width: 100%;
        }}
        </style>
    """, unsafe_allow_html=True)
    if st.button("SÍ, ACEPTO 😍", key="si"):
        st.balloons()
        st.success("¡SABÍA QUE DIRÍAS QUE SÍ!")

st.write(" ")

# 4. Botón NO
with st.container():
    st.markdown(f"""
        <style>
        div[data-testid="stVerticalBlock"] > div:nth-child(4) button {{
            font-size: {st.session_state.size_no}px !important;
            background-color: #dc3545 !important;
            color: white !important;
            width: 100%;
        }}
        </style>
    """, unsafe_allow_html=True)
    if st.button(texto_no, key="no"):
        st.session_state.size_si += 20 # Aumenta el Sí
        if st.session_state.size_no > 6:
            st.session_state.size_no -= 2 # Achica el No
        
        # Incrementamos el contador para cambiar la frase
        st.session_state.intentos += 1
        st.rerun()
