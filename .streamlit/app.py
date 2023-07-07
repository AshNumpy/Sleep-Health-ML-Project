import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

st.title('Stress Level Prediction App 🩺')

st.markdown('<span style="color:gray">This app predicts the stress level of a person based on the data provided.</span>', unsafe_allow_html=True)

homepage, knowledge, prediction = st.columns(3)

selected = option_menu(
        menu_title = None,
        options =["Home","Preview", "Prediction", "Contact"],
        icons=["window", "file", "play", "whatsapp"],
        orientation = "horizontal",
        default_index = 0
)

if selected == "Home":
    pass

if selected == "Preview":
    pass

if selected == "Prediction":
    features, result = st.columns((3,1))
    
    with features:
        st.write('#### Set The Features ')

    with result:
        st.write('#### Result ⬇️')

if selected == "Contact":
    pass