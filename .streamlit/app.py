from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import pickle
import time 


st.set_page_config(
    page_title="Stress Level Application",
    page_icon="💤",
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

df = pd.read_csv('./.streamlit/Dataset/dataset.csv')
df.drop(['Person ID', 'Sick'], axis=1, inplace=True)
df = df[['Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep',
       'Physical Activity Level', 'BMI Category', 'Heart Rate',
       'Daily Steps', 'Sleep Disorder', 'BP High', 'BP Low', 'Stress Level']]

if selected == "Home":
    with st.container():

        # Resme tıklanınca yönlendirilecek URL
        target_url = "https://public.tableau.com/app/profile/ramazan.erduran1816/viz/StressLevelHealth/Overview"
        image_url = "https://raw.githubusercontent.com/AshNumpy/Sleep-Health-ML-Project/main/Imgs/Homepage.png"
        
        st.markdown(
            f'<a href="{target_url}" target="_blank"><img src="{image_url}" alt="Homepage Image" width="100%"></a>',
            unsafe_allow_html=True
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
            <br>
            <p align='right'>
                <a href="https://www.github.com/AshNumpy/Sleep-Health-ML-Project" target="_blank">View on GitHub</a>
                <br>
                <a href="https://public.tableau.com/app/profile/ramazan.erduran1816/viz/StressLevelHealth/Overview" target="_blank">See Dashboard on Tableau</a>
            </p>
            """,
            unsafe_allow_html=True
        )
    

if selected == "Dataset":

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

    accuracies = dict(
        mape=0.04,
        rmse=0.37,
        r2=0.97
    )

    st.markdown(
    f"""
    <h2 style="color:#176397">Prediction Model Accuracy Metrics</h2>

    A machine learning study was conducted, and as a result, the Linear Regression model was chosen as the main model. 
    The accuracy of the model was evaluated using **MAPE** (Mean Absolute Percentage Error), **RMSE** (Root Mean Square Error), and **R2** (R Squared) values. 
    Based on the test results, the accuracy of the model was calculated as follows.

    <div class="kpi-container">
        <div class="kpi-box">
            <span class="kpi-title">MAPE</span>
            <span class="kpi-value">{accuracies['mape']*100}%</span>
        </div>
        <div class="kpi-box">
            <span class="kpi-title">RMSE</span>
            <span class="kpi-value">{accuracies['rmse']}</span>
        </div>
        <div class="kpi-box">
            <span class="kpi-title">R2</span>
            <span class="kpi-value">{accuracies['r2']*100}%</span>
        </div>
    </div>

    <style>
    .kpi-container {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
    }}

    .kpi-box {{
    flex-grow: 0.25;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0px;
    border-radius: 100px;
    background-color: #F2F2F2;
    transition: box-shadow 0.3s;
    }}

    .kpi-box:hover {{
    box-shadow: 0 0 10px #1D4665;
    }}

    .kpi-title {{
    color: #176397;
    font-size: 20px;
    font-weight: bold;
    font-family: 'Poppins', sans-serif;
    margin-bottom: 0px;
    }}

    .kpi-value {{
    color: #1D4665;
    font-size: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True)


    st.write("---")

    features, result = st.columns((4,2))

    with features:
        st.markdown(
            """
                <h3 style="color:#176397">Set Features</h3>
            """,unsafe_allow_html=True
        )

        def load_model():
            """
            The function `load_model()` loads a linear regression model from a pickle file.
            
            Returns:
              a loaded linear regression model.
            """
            with open('./.streamlit/Models/model.pkl', 'rb') as f:
                model = pickle.load(f)
            return model

        gender_le = joblib.load('./.streamlit/Models/gender_encoder.pkl')
        occupation_le = joblib.load('./.streamlit/Models/occupation_encoder.pkl')
        bmiCategory_le = joblib.load('./.streamlit/Models/bmi_category_encoder.pkl')
        sleepDisorder_le = joblib.load('./.streamlit/Models/sleep_disorder_encoder.pkl')
        scaler = joblib.load('./.streamlit/Models/scaler.pkl')

        col1, col2 = st.columns(2)

        with col1:
            Gender = st.selectbox(
                "Gender",
                ("Male", "Female"),
                label_visibility='collapsed',
            )

            age = st.slider(
                "Age",
                min_value=18,
                max_value=65,
                value=30,
                step=1
            )

            Occupation = st.selectbox(
                "Occupation",
                (df['Occupation'].unique()),
                label_visibility='collapsed',
            )

            sleepDuration = st.slider(
                "Sleep Duration (Hours)",
                min_value=0.0,
                max_value=24.0,
                value=7.0,
                step=0.1,
                format="%.1f"
            )

            sleepQuality = st.slider(
                "Sleep Quality (1-10)",
                min_value=0,
                max_value=10,
                value=3,
                step=1
            )

            physicalActivity = st.slider(
                "Physical Activity Level (%)",
                min_value=0.0,
                max_value=100.0,
                value=50.0,
                step=1.0,
                format="%.1f"
            )

        with col2:
            bmi = st.selectbox(
                "BMI Category",
                (df['BMI Category'].unique()),
                label_visibility='collapsed',
            )
            restingHeartRate = st.slider(
                "Resting Heart Rate",
                min_value=60.0,
                max_value=120.0,
                value=60.0,
                step=0.1,
                format="%.1f"
            )

            sleepDisorder = st.selectbox(
                "Sleep Disorder",
                (df['Sleep Disorder'].unique()),
                label_visibility='collapsed',
            )

            dailySteps = st.slider(
                "Daily Steps",
                min_value=0,
                max_value=10000,
                value=5000,
                step=1
            )

            bloodPressureHigh = st.slider(
                "High Blood Pressure",
                min_value=90.0,
                max_value=180.0,
                value=120.0,
                step=0.1,
                format="%.1f"
            )

            bloodPressureLow = st.slider(
                "Low Blood Pressure",
                min_value=50.0,
                max_value=120.0,
                value=80.0,
                step=0.1,
                format="%.1f"
            )


    with result:
        st.markdown(
            """
                <h3 style="color:#176397" align="center">Prediction</h3>
            """,unsafe_allow_html=True
        )

        def get_user_input():
            """
            The function `get_user_input()` collects various user inputs related to health and returns
            them as a dictionary.
            """

            prediction = {
            'Gender': Gender,
            'Age': age,
            'Occupation': Occupation,
            'Sleep Duration': sleepDuration,
            'Quality of Sleep': sleepQuality,
            'Physical Activity Level': physicalActivity,
            'BMI Category': bmi,
            'Heart Rate': restingHeartRate,
            'Daily Steps': dailySteps,
            'Sleep Disorder': sleepDisorder,
            'BP High': bloodPressureHigh,
            'BP Low': bloodPressureLow
            }

            prediction = pd.DataFrame(prediction, index=[0])
            
            return prediction

        prediction = get_user_input()

        prediction['Gender'] = gender_le.transform(prediction['Gender'])
        prediction['Occupation'] = occupation_le.transform(prediction['Occupation'])
        prediction['BMI Category'] = bmiCategory_le.transform(prediction['BMI Category'])
        prediction['Sleep Disorder'] = sleepDisorder_le.transform(prediction['Sleep Disorder'])

        numerical_features = ['Age',
                            'Sleep Duration',
                            'Quality of Sleep',
                            'Physical Activity Level',
                            'Heart Rate',
                            'Daily Steps',
                            'BP High',
                            'BP Low']

        prediction[numerical_features] = scaler.transform(prediction[numerical_features])

        with st.spinner('Wait for prediction...'):
            model = load_model()
            y_pred = model.predict(prediction)
            time.sleep(1)
            
        st.markdown(
        f"""
        <p align="center">
            The predicted stress level based on your selections on the left-hand side is as follows.
        </p>
        <div class="kpi-container1">
            <div class="kpi-box1">
                <span class="kpi-title1">Stress Level</span>
                <span class="kpi-value1">{np.round(y_pred[0],2)}/10</span>
            </div>
        </div>

        <style>
        .kpi-container1 {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 10vh;
        }}

        .kpi-box1 {{
        flex-grow: 0.25;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 0px;
        border-radius: 10px;
        background-color: #F2F2F2;
        transition: box-shadow 0.3s;
        }}

        .kpi-box:hover1 {{
        box-shadow: 0 0 10px #1D4665;
        }}

        .kpi-title1 {{
        color: #176397;
        font-size: 14px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 0px;
        }}

        .kpi-value1 {{
        color: #1D4665;
        font-size: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True)       

    st.write('---') 


if selected == "Contact":

    html_path = './.streamlit/ContactPage/index.html'
    css_path ='./.streamlit/ContactPage/style.css' 

    def get_contact_page(css_path, html_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            contact_page_css = f.read()
        
        with open(html_path, 'r', encoding='utf-8') as f:
            contact_page = f.read()

        return contact_page_css, contact_page

    contact_page, contact_css_file = get_contact_page(html_path, css_path)

    st.markdown(
        f"""
        <style>
            {contact_css_file}
        </style>
        {contact_page}
        """,
        unsafe_allow_html=True
    )