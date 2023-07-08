import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Stress Level Application",
    page_icon="🧊",
    initial_sidebar_state="expanded"
)


st.title('Stress Level Prediction App 💤')

st.markdown('<span style="color:gray">This app predicts the stress level of a person based on the data provided.</span>', unsafe_allow_html=True)

homepage, knowledge, prediction = st.columns(3)


selected = option_menu(
    menu_title=None,
    options=["Home", "Dataset", "Prediction", "Contact"],
    icons=["window", "table", "cpu", "phone"],
    orientation="horizontal",
    default_index=0,
    styles={
        # "container": {"background-color": "white"},
        # "icon": {"color": "white"}, 
        # "nav-link": {"text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#176397"},
    }
)

df = pd.read_csv('./Dataset/dataset.csv')
df.drop(['Person ID'], axis=1, inplace=True)


if selected == "Home":
    with st.container():

        st.image(
            './Images/Homepage.png',
            use_column_width=True
        )

        st.markdown(
            """

            <h2 style="color:#176397">Project Overview</h2>

            <p style="color:#1D4665">
                This project includes the analysis of sleep health and lifestyle dataset and an application for predicting stress levels using machine learning. The dataset consists of 400 rows and 13 columns, encompassing various demographic, health, and lifestyle variables.
            </p>

            <h2 style="color:#176397">Project Objectives</h2>

            <p style="color:#1D4665">
                The main objectives of the project are to analyze and visualize the data related to health, lifestyle, and demographic factors, derive actionable insights from the visualizations, and predict stress levels of individuals using machine learning techniques.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <h2 style="color:#176397">Project Features</h2>

            <p style="color:#1D4665">
                <ul>
                    <li>Sleep health metrics analysis: Explore factors related to sleep duration, quality, and regularity.</li>
                    <li>Lifestyle factors analysis: Investigate physical activity levels, stress levels, and BMI categories.</li>
                    <li>Cardiovascular health analysis: Examine blood pressure and resting heart rate measurements.</li>
                    <li>Sleep disorder analysis: Determine the presence of sleep disorders such as insomnia and sleep apnea.</li>
                </ul>
            </p>
            <hr>
            <p align='right'><a href="https://www.github.com/AshNumpy/Sleep-Health-ML-Project" target="_blank">View on GitHub</a></p>
            """,
            unsafe_allow_html=True
        )


if selected == "Dataset":
    import plotly.graph_objects as go
    import streamlit as st

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='#176397',
            align='left',
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color='white',
            align='left',
            font=dict(color='#1D4665', size=12)
        )
    )])

    fig.update_layout(
        height=800
    )


    st.markdown(
        """
        <h2 style="color:#176397">Dataset Preview</h2>

        <p style="color:#1D4665">
            The dataset consists of 400 rows and 13 columns, encompassing various demographic, health, and lifestyle variables. The dataset is divided into two parts: the first part contains demographic, health, and lifestyle variables, and the second part contains sleep health variables. The dataset contains 13 columns, out of which 12 are features and 1 is the target variable.
        </p>

        <p style="color:#1D4665">
            <a href="https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset" target="_blank">Dataset Source</a>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        theme='streamlit',
        config={
            'displayModeBar': False
        }
    )

    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <a href="data:file/csv;base64,{data}" download="{file_name}" style="padding: 10px; background-color: #176397; color: white; border-radius: 5px; text-decoration: none;">
                {label}
            </a>
        </div>
        """.format(
            data=df.to_csv(index=False).encode().decode('utf-8').replace('\n', '%0A'),
            file_name='dataset.csv',
            label="Download Dataset"
        ),
        unsafe_allow_html=True
    )


if selected == "Prediction":
    features, result = st.columns((3,1))
    
    with features:
        st.write('#### Set The Features ')

    with result:
        st.write('#### Result ⬇️')

if selected == "Contact":

    contact_page_path = './ContactPage/index.html'
    contact_page_css_path ='./ContactPage/style.css' 

    def getContactPage(contact_page_path, contact_page_css_path):
        with open(f'{contact_page_path}', 'r') as file:
            contact_file = file.read()
        
        with open(f'{contact_page_css_path}', 'r') as file:
            contact_css_file = file.read()

        return contact_file, contact_css_file

    contact_file, contact_css_file = getContactPage(contact_page_path, contact_page_css_path)

    st.markdown(
        f"""
        <style>
            {contact_css_file}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        {contact_file}
        """,
        unsafe_allow_html=True
    )