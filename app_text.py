import streamlit as st
import pandas as pd
#import joblib
import pickle

# Load the model
#model = joblib.load('model.pkl')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the layout
st.title("Machine Learning App")
st.write("Enter the data to get the prediction:")
# input_data = pd.DataFrame({
#     'column_1': [st.  input("Enter column 1 value")]})
#     # 'column_2': [st.number_input("Enter column 2 value")],
#     # 'column_3': [st.number_input("Enter column 3 value")],
# })
input_string = st.text_input("Enter a string")
st.write("입력한 문자열은 ", input_string)

# Preprocess the input data
#processed_data = preprocess(input_data)

# Make the prediction
prediction = model.predict([input_string])

# Show the prediction
st.write("The prediction is:", prediction)
