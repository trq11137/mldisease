import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading saves model
Diabetes_disease_model = pickle.load(open('Diabetes_disease_model.pkl', 'rb'))

heart_model = pickle.load(open('heart_disease_model.pkl', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_disease_model.sav', 'rb'))

Breast_model = pickle.load(open('Breast_model.pkl', 'rb'))

#Pregnency_model = pickle.load(open('parkinsons_disease_model.sav', 'rb'))

# side bar for navigations

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',

                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'

                            ],

                           icons=['activity', 'heart', 'person', 'diamond'],

                           default_index=0)

    # Diabetes prediction page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes prediction using machine learnig')

    # getting the input data from user
    # colum for input fields

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

    # code for prediction

    diab_diagnosis = ''

    # creating button for predictions

    if st.button('Diabetes Test Results'):
        diab_prediction = Diabetes_disease_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):
            diab_diagnosis = ' The person is Diabetic!'
        else:
            diab_diagnosis = 'The person is not Diabetic!'

    st.success(diab_diagnosis)

    # heart disease predicton page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease prediction using machine learnig')
    # getting the input data from user
    # colum for input fields
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
        chol = st.text_input('Serum Cholestoral in mg/dl(chol)')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar(fbs)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(restecg)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved(thalach)')

    with col3:
        exang = st.text_input('Exercise Induced Angina(exang)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(oldpeak)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(ca)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Prediction using machine learnig')

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        NHR = st.text_input('NHR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread2 = st.text_input('spread2')

    with col2:
        D2 = st.text_input('D2')

    with col3:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, NHR, RPDE, DFA, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

    # Breast cancer prediction page
if (selected == 'Breast Cancer Prediction'):

    # page title
    st.title('Breast cancer prediction using machine learnig')

    # getting the input data from user
    # colum for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('mean_radius')

    with col2:
        mean_texture = st.text_input('mean_texture')

    with col3:
        mean_perimeter = st.text_input('mean_perimeter value')

    with col1:
        mean_area = st.text_input('mean_area')

    with col2:
        mean_smoothness = st.text_input('mean_smoothness')

    # code for prediction

    Breast_diagnosis = ''

    # creating button for predictions

    if st.button('Breast cancer Test Results'):
        Breast_prediction = Breast_model.predict(
            [[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
        if (Breast_prediction[0] == 0):
            Breast_diagnosis = ' The person do not have breast cancer'
        else:
            Breast_diagnosis = 'The person has breast cancer'

    st.success(Breast_diagnosis)


