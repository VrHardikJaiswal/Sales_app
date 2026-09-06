import streamlit as st
import joblib
import pandas as pd

# Load the trained KNN model
loaded_knn_model = joblib.load('knn_regression_model.sav')

st.title('Sales Prediction using KNN Regression')
st.write('Enter the advertising spending to predict sales.')

# Input fields for advertising spending
tv = st.slider('TV Advertising Spend (in thousands)', 0.0, 300.0, 100.0)
radio = st.slider('Radio Advertising Spend (in thousands)', 0.0, 50.0, 20.0)
newspaper = st.slider('Newspaper Advertising Spend (in thousands)', 0.0, 120.0, 30.0)

# Create DataFrame for prediction
input_data = pd.DataFrame([{
    'TV': tv,
    'Radio': radio,
    'Newspaper': newspaper
}])

# Make prediction
if st.button('Predict Sales'):
    prediction = loaded_knn_model.predict(input_data)[0]
    st.success(f'Predicted Sales: {prediction:.2f} (in millions)')
