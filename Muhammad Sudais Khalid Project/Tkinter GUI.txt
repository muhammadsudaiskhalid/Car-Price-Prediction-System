import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import messagebox

# Load and preprocess the dataset
def load_data():
    # Load dataset (replace with the provided dataset)
    file_path = "car-data.csv"  # Update this path if needed
    data = pd.read_csv(file_path)

    # Drop irrelevant columns
    data_cleaned = data.drop("Car_Name", axis=1)

    # Encode categorical variables
    data_encoded = pd.get_dummies(
        data_cleaned, columns=["Fuel_Type", "Seller_Type", "Transmission"], drop_first=True
    )
    return data_encoded

data = load_data()

# Split the data into features and target variable
X = data.drop("Selling_Price", axis=1)
y = data["Selling_Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error: {mse:.2f}")

# Function to predict selling price
def predict_price():
    try:
        # Get user inputs
        year = int(year_entry.get())
        present_price = float(present_price_entry.get())
        kms_driven = int(kms_driven_entry.get())
        owner = int(owner_entry.get())
        fuel_type = fuel_type_var.get()
        seller_type = seller_type_var.get()
        transmission = transmission_var.get()

        # Prepare the input for prediction
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

        # Ensure input data has the same columns as the model
        missing_cols = set(X.columns) - set(input_df.columns)
        for col in missing_cols:
            input_df[col] = 0  # Add missing columns with default value 0

        # Reorder the input_df columns to match the model's training set
        input_df = input_df[X.columns]

        # Predict and show result
        prediction = model.predict(input_df)
        messagebox.showinfo("Prediction Result", f"Estimated Selling Price: Rs.{prediction[0]:,.2f} Lakhs")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Car Selling Price Prediction")

# Create input fields
tk.Label(root, text="Year of Manufacture (1990 to 2025):").grid(row=0, column=0, padx=10, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Present Price (in Lakhs):").grid(row=1, column=0, padx=10, pady=5)
present_price_entry = tk.Entry(root)
present_price_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Kilometers Driven:").grid(row=2, column=0, padx=10, pady=5)
kms_driven_entry = tk.Entry(root)
kms_driven_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Previous Owners (0, 1, 2, 3):").grid(row=3, column=0, padx=10, pady=5)
owner_entry = tk.Entry(root)
owner_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Fuel Type:").grid(row=4, column=0, padx=10, pady=5)
fuel_type_var = tk.StringVar(value="Petrol")
tk.Radiobutton(root, text="Petrol", variable=fuel_type_var, value="Petrol").grid(row=4, column=1, sticky="w")
tk.Radiobutton(root, text="Diesel", variable=fuel_type_var, value="Diesel").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="CNG", variable=fuel_type_var, value="CNG").grid(row=6, column=1, sticky="w")

tk.Label(root, text="Seller Type:").grid(row=7, column=0, padx=10, pady=5)
seller_type_var = tk.StringVar(value="Dealer")
tk.Radiobutton(root, text="Dealer", variable=seller_type_var, value="Dealer").grid(row=7, column=1, sticky="w")
tk.Radiobutton(root, text="Individual", variable=seller_type_var, value="Individual").grid(row=7, column=1, sticky="e")

tk.Label(root, text="Transmission:").grid(row=8, column=0, padx=10, pady=5)
transmission_var = tk.StringVar(value="Manual")
tk.Radiobutton(root, text="Manual", variable=transmission_var, value="Manual").grid(row=8, column=1, sticky="w")
tk.Radiobutton(root, text="Automatic", variable=transmission_var, value="Automatic").grid(row=8, column=1, sticky="e")

# Predict button
predict_button = tk.Button(root, text="Predict Selling Price", command=predict_price)
predict_button.grid(row=9, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()