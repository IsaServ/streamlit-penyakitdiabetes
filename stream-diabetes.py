import pickle
import streamlit as st
import os
st.write("Files di folder:", os.listdir())

# membaca model
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
except Exception as e:
    st.error(f"Gagal load model: {e}")

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Pregnancies')

with col2 :
    Glucose = st.text_input ('input nilai Glucose')

with col1 :
    BloodPressure = st.text_input ('input nilai Blood Pressure')

with col2 :
    SkinThickness = st.text_input ('input nilai Skin Thickness')

with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        diab_prediction = diabetes_model.predict([[
            float(Pregnancies),
            float(Glucose),
            float(BloodPressure),
            float(SkinThickness),
            float(Insulin),
            float(BMI),
            float(DiabetesPedigreeFunction),
            float(Age)
        ]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'

        st.success(diab_diagnosis)

    except:
        st.error("Masukkan semua input dengan angka yang valid")
