# Bank Customer Churn Prediction

This project aims to predict customer churn for a bank using a Gaussian Naive Bayes model. The project includes data preprocessing, model training, and a Streamlit app for making predictions based on user input.

### Project Structure

app.py: Streamlit app for customer churn prediction.
gaussian_nb_model.pkl: Trained Gaussian Naive Bayes model.
scaler.pkl: Scaler used for data normalization.
Bank_Customer_Churn_Prediction.ipynb: Jupyter notebook for data preprocessing and model training.
venv/: Virtual environment directory.
.gitignore: Git ignore file to exclude unnecessary files from the repository.
README.md: Project documentation.

### Setup Instructions

Clone the Repository
Create a Virtual Environment
Install Dependencies
Run the Streamlit App

### Usage
Run the Streamlit app using this command: streamlit run app.py
Enter the customer details in the sidebar form.
View the prediction result to see if the customer is likely to churn.

### Data Preprocessing and Model Training
The Bank_Customer_Churn_Prediction.ipynb notebook contains the following steps:

Data loading and preprocessing.
Feature scaling using MinMaxScaler.
Model training using Gaussian Naive Bayes.
Saving the trained model and scaler to disk.

### Author
### Barakat Akinsiku



