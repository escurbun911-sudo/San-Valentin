import streamlit as st

st.title("¿Quieres ser mi San Valentín? ❤️")

# 1. Variables de estado
if 'size_si' not in st.session_state:
    st.session_state.size_si = 16
if 'size_no' not in st.session_state:
    st.session_state.size_no = 16

# 2. Botón SÍ
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

# 3. Botón NO
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
    if st.button("No", key="no"):
        st.session_state.size_si += 20 # Aumenta el Sí
        if st.session_state.size_no > 6:
            st.session_state.size_no -= 2 # Achica el No
        st.rerun()