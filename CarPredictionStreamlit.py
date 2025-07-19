import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load and preprocess the dataset
def load_data():
    file_path = "car-data.csv"  # Update this path if needed
    data = pd.read_csv(file_path)
    data_cleaned = data.drop("Car_Name", axis=1)
    data_encoded = pd.get_dummies(
        data_cleaned, columns=["Fuel_Type", "Seller_Type", "Transmission"], drop_first=True
    )
    return data_encoded

data = load_data()

# Split the data
X = data.drop("Selling_Price", axis=1)
y = data["Selling_Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Streamlit UI
st.title("Car Selling Price Prediction")
st.write(f"Model Mean Squared Error: {mse:.2f}")

# User inputs
year = st.number_input("Year of Manufacture (1990-2025)", min_value=1990, max_value=2025, step=1)
present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.radio("Seller Type", ["Dealer", "Individual"])
transmission = st.radio("Transmission", ["Manual", "Automatic"])

# Predict function
def predict_price():
    input_data = {
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Owner": [owner],
        "Fuel_Type_Diesel": [1 if fuel_type == "Diesel" else 0],
        "Fuel_Type_Petrol": [1 if fuel_type == "Petrol" else 0],
        "Seller_Type_Individual": [1 if seller_type == "Individual" else 0],
        "Transmission_Manual": [1 if transmission == "Manual" else 0],
    }
    input_df = pd.DataFrame(input_data)
    missing_cols = set(X.columns) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0
    input_df = input_df[X.columns]
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Selling Price: Rs.{prediction:,.2f} Lakhs")

# Predict button
if st.button("Predict Selling Price"):
    predict_price()