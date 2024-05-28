import streamlit as st
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load('gaussian_nb_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit App
st.title('Bank Customer Churn Prediction')

# Input form
st.sidebar.title('Input Customer Data')
credit_score = st.sidebar.number_input('Credit Score', min_value=0)
age = st.sidebar.number_input('Age', min_value=0)
tenure = st.sidebar.number_input('Tenure', min_value=0)
balance = st.sidebar.number_input('Balance', min_value=0)
num_of_products = st.sidebar.number_input('Number of Products', min_value=1)
has_cr_card = st.sidebar.checkbox('Has Credit Card', value=True)
is_active_member = st.sidebar.checkbox('Is Active Member', value=True)
estimated_salary = st.sidebar.number_input('Estimated Salary', min_value=0)
geography = st.sidebar.selectbox('Geography', ['France', 'Spain', 'Germany'])
loyalty = st.sidebar.number_input('Loyalty', min_value=0.0, max_value=1.0, step=0.01)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [int(has_cr_card)],
    'IsActiveMember': [int(is_active_member)],
    'EstimatedSalary': [estimated_salary],
    'Geography_France': [1 if geography == 'France' else 0],
    'Geography_Germany': [1 if geography == 'Germany' else 0],
    'Geography_Spain': [1 if geography == 'Spain' else 0],
    'Loyalty': [loyalty]
})

# Ensuring order of columns is the same as in training
columns_order = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
                 'Geography_France', 'Geography_Germany', 'Geography_Spain', 'Loyalty']
input_data = input_data[columns_order]

# Scale the input data using the loaded scaler
input_data_scaled = scaler.transform(input_data)

# Make predictions
prediction = model.predict(input_data_scaled)

# Show prediction
st.subheader('Prediction')
if prediction[0] == 1:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is unlikely to churn.')
