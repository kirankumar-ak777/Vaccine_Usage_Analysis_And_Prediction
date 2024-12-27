import streamlit as st
import requests
import json
import base64

logo_path = "Medical.jpg"

# Function to encode the image as base64 and set it as background
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }}
        .restaurant-analysis {{
            background-color: #3498db;
        }}
        .city-analysis {{
            background-color: #e74c3c;
        }}
        .restaurants-per-city {{
            background-color: #2ecc71;
        }}
        button[data-baseweb="button"][id="previous"] {{
            position: fixed;
            bottom: 20px;
            left: 20px;
            background-color: #3498db;
            color: white;
            font-size: 16px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the background
set_background(logo_path)

st.title('H1N1 Vaccination Prediction App')

# Collect user inputs
h1n1_worry = st.selectbox('H1N1 Worry (0 - Not worried, 1 - Somewhat worried, 2 - Very worried)', [0, 1, 2])
h1n1_awareness = st.selectbox('H1N1 Awareness (0 - Not aware, 1 - Aware)', [0, 1])
bought_face_mask = st.selectbox('Bought Face Mask (0 - No, 1 - Yes)', [0, 1])
avoid_large_gatherings = st.selectbox('Avoid Large Gatherings (0 - No, 1 - Yes)', [0, 1])
dr_recc_h1n1_vacc = st.selectbox('Doctor Recommended H1N1 Vaccine (0 - No, 1 - Yes)', [0, 1])
dr_recc_seasonal_vacc = st.selectbox('Doctor Recommended Seasonal Vaccine (0 - No, 1 - Yes)', [0, 1])
cont_child_undr_6_mnths = st.selectbox('Contact with Child under 6 Months (0 - No, 1 - Yes)', [0, 1])
is_health_worker = st.selectbox('Is Health Worker (0 - No, 1 - Yes)', [0, 1])
has_health_insur = st.selectbox('Has Health Insurance (0 - No, 1 - Yes)', [0, 1])
is_h1n1_vacc_effective = st.selectbox('Belief in H1N1 Vaccine Effectiveness (0 - No, 1 - Yes)', [0, 1])
is_h1n1_risky = st.selectbox('Belief that H1N1 is Risky (0 - No, 1 - Yes)', [0, 1])
is_seas_risky = st.selectbox('Belief that Seasonal Flu is Risky (0 - No, 1 - Yes)', [0, 1])
age_bracket = st.number_input('Age Bracket (Enter age)', min_value=0, max_value=120)
sex = st.selectbox('Sex (0 - Female, 1 - Male)', [0, 1])
marital_status = st.selectbox('Marital Status (0 - Not Married, 1 - Married)', [0, 1])

# Make a prediction request when the user clicks the button
if st.button('Predict'):
    # Create payload
    payload = {
        'h1n1_worry': h1n1_worry,
        'h1n1_awareness': h1n1_awareness,
        'bought_face_mask': bought_face_mask,
        'avoid_large_gatherings': avoid_large_gatherings,
        'dr_recc_h1n1_vacc': dr_recc_h1n1_vacc,
        'dr_recc_seasonal_vacc': dr_recc_seasonal_vacc,
        'cont_child_undr_6_mnths': cont_child_undr_6_mnths,
        'is_health_worker': is_health_worker,
        'has_health_insur': has_health_insur,
        'is_h1n1_vacc_effective': is_h1n1_vacc_effective,
        'is_h1n1_risky': is_h1n1_risky,
        'is_seas_risky': is_seas_risky,
        'age_bracket': age_bracket,
        'sex': sex,
        'marital_status': marital_status
    }

    # Display payload to confirm input values
    st.write("Payload Sent to API:", payload)

    # Send request to Flask API
    response = requests.post('http://127.0.0.1:5000/predict', json=payload)

    # Check for response status and parse JSON
    if response.status_code == 200:
        result = response.json()
        # Display results
        st.write('Prediction:', 'Will Take Vaccine' if result['prediction'] == 1 else 'Will Not Take Vaccine')
        st.write('Prediction Probability:', result['probability'])
    else:
        st.write('Error:', response.status_code, response.text)
