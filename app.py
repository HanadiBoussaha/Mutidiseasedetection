import os
import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from login import login
from signup import signup
from connect import create_patient, get_patients, update_patient, delete_patient

# Initialize the session state key 'logged_in' if it does not exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Getting the working directory of the app.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# User authentication handling
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Login/signup page options
    option = st.sidebar.selectbox('Login/Signup', ('Login', 'Signup'))

    if option == 'Login':
        login()  # Call the login function from login.py
    else:
        signup()  # Call the signup function from signup.py
else:
    # Navigation menu for disease prediction and patient management
    with st.sidebar:
        selected = option_menu(
            'Patient Management and Health Diagnosis System',
            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Patient'],
            menu_icon='hospital-fill',
            icons=['activity', 'heart', 'person', 'person-lines-fill'],  # Change icons as desired
            default_index=0
        )

    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')

        # Prediction
        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

        st.success(diab_diagnosis)

    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # Prediction
        heart_diagnosis = ''
        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

        st.success(heart_diagnosis)

    # Parkinson's Prediction Page
    if selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        # Prediction
        parkinsons_diagnosis = ''
        if st.button("Parkinson's Test Result"):
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])

            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)

  # Section pour ajouter un nouveau patient
st.header("Add New Patient")
with st.form(key='create_patient_form'):
    name = st.text_input('Name')
    age = st.text_input('Age')
    gender = st.text_input('Gender')
    disease = st.text_input('Disease')
    submit_button = st.form_submit_button('Add Patient')

    if submit_button:
        create_patient(name, age, gender, disease)
        st.success(f"Patient '{name}' added successfully!")

# Section pour afficher et gérer les patients
st.header("Patients List")
patients = get_patients()

if patients:
    # Préparer les données pour l'affichage
    patient_data = []
    for patient in patients:
        patient_data.append({
            "id": patient[0],
            "name": patient[1],
            "age": patient[2],
            "gender": patient[3],
            "disease": patient[4]
        })

    # Convertir en DataFrame pour l'affichage
    df = pd.DataFrame(patient_data)

    for index, row in df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            st.text(row["name"])
        with col2:
            st.text(row["age"])
        with col3:
            st.text(row["gender"])
        with col4:
            st.text(row["disease"])
        
        with col5:
            # Affichage du bouton "Update"
            update_button = st.button(f"Update {row['id']}", key=f"update_{row['id']}")
            
            if update_button:
                # Formulaire de mise à jour
                with st.form(key=f"update_form_{row['id']}"):
                    new_name = st.text_input("New Name", value=row["name"], key=f"name{row['id']}")
                    new_age = st.text_input("New Age", value=row["age"], key=f"age{row['id']}")
                    new_gender = st.text_input("New Gender", value=row["gender"], key=f"gender{row['id']}")
                    new_disease = st.text_input("New Disease", value=row["disease"], key=f"disease{row['id']}")
                    
                    save_button = st.form_submit_button("Save Changes")
                    
                    if save_button:
                        updated_data = {
                            "name": new_name,
                            "age": new_age,
                            "gender": new_gender,
                            "disease": new_disease
                        }
                        # Appeler la fonction pour mettre à jour le patient
                        update_patient(row["id"], updated_data)
                        st.experimental_rerun()  # Réinitialiser l'affichage après mise à jour
        
        with col6:
            delete_button = st.button(f"Delete {row['id']}", key=f"delete_{row['id']}")
            
            if delete_button:
                delete_patient(row["id"])
                st.experimental_rerun()  # Réinitialiser l'affichage après suppression
else:
    st.write("No patients found.")