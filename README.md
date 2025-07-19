# Car Selling Price Prediction Using Machine Learning

A comprehensive machine learning project that predicts used car selling prices based on various features using Linear Regression, with both web-based and desktop GUI implementations.

## 📋 Project Overview

This project develops a predictive model that estimates the selling price of used cars based on features such as manufacturing year, kilometers driven, fuel type, seller type, and transmission type. The model is accessible through two different user interfaces: a web-based Streamlit application and a desktop Tkinter application.

## 🎯 Objectives

- Develop an accurate machine learning model for predicting car selling prices
- Provide user-friendly interfaces for easy interaction with the prediction model
- Implement dual GUI solutions (web-based and desktop) for maximum accessibility
- Demonstrate practical application of machine learning in automotive price estimation

## 🛠️ Technologies Used

**Programming Language:** Python

**Libraries & Frameworks:**
- **Machine Learning:** scikit-learn (model training and evaluation)
- **Data Handling:** pandas (dataset manipulation and preprocessing)
- **User Interfaces:** 
  - Streamlit (web-based interface)
  - Tkinter (desktop application)

## 📊 Dataset Description

The model is trained on a comprehensive car dataset (`car-data.csv`) containing the following features:

| Feature | Description | Type |
|---------|-------------|------|
| Car_Name | Name of the car | Text (excluded from model) |
| Year | Year of manufacture | Numerical |
| Present_Price | Current market price | Numerical |
| Kms_Driven | Distance traveled by the car | Numerical |
| Fuel_Type | Type of fuel (Petrol, Diesel, CNG) | Categorical |
| Seller_Type | Type of seller (Dealer/Individual) | Categorical |
| Transmission | Transmission type (Manual/Automatic) | Categorical |
| Owner | Number of previous owners | Numerical |
| Selling_Price | Target variable - actual selling price | Numerical |

## 🔄 Data Preprocessing

- **Feature Engineering:** Removed non-numerical Car_Name column
- **Categorical Encoding:** Applied one-hot encoding to categorical variables (Fuel_Type, Seller_Type, Transmission)
- **Data Splitting:** 80% training data, 20% testing data for robust model evaluation

## 🤖 Model Implementation

- **Algorithm:** Linear Regression using scikit-learn
- **Evaluation Metric:** Mean Squared Error (MSE) for accuracy assessment
- **Training Approach:** Supervised learning on historical car sales data

## 🖥️ User Interface Implementation

### Streamlit Web Application
- Clean, intuitive web interface
- Interactive input fields for car specifications
- Real-time prediction with model performance metrics
- Accessible via web browser

### Tkinter Desktop Application
- Native desktop GUI application
- Dropdown menus and input fields for parameter selection
- One-click prediction generation
- Standalone executable application

## 📈 Results & Performance

- Achieved reasonable accuracy in car price predictions
- Model performance evaluated using Mean Squared Error metrics
- Successfully deployed in both web and desktop environments
- User-friendly interfaces enable easy price estimation for end users

## 🚀 Future Enhancements

- **Advanced Algorithms:** Implement Random Forest, XGBoost, or Neural Networks
- **Extended Features:** Include location, brand reputation, and car condition
- **Database Integration:** Store user inputs and predictions for analysis
- **Mobile Application:** Develop mobile-friendly interface
- **Real-time Data:** Integrate with live market data APIs

## 📦 Installation & Setup

```bash
# Clone the repository
git clone [repository-url]

# Install required dependencies
pip install -r requirements.txt

# Run Streamlit web application
streamlit run streamlit_app.py

# Run Tkinter desktop application
python tkinter_app.py
```

## 🔧 Usage

### Web Interface (Streamlit)
1. Launch the Streamlit application
2. Enter car details in the provided fields
3. Click "Predict Price" button
4. View the predicted selling price and model metrics

### Desktop Interface (Tkinter)
1. Run the Tkinter application
2. Fill in car specifications using dropdowns and input fields
3. Click the prediction button
4. View results displayed on the interface

## 📊 Model Performance

The Linear Regression model demonstrates effective performance in predicting used car prices, with detailed evaluation metrics available in both GUI implementations.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

## 📧 Contact Information

**Developer:** Muhammad Sudais Khalid  
**Email:** muhammadsudaiskhalid.artificialintelligence@stmu.edu.pk  
**LinkedIn:** [https://www.linkedin.com/in/sudais-khalid/](https://www.linkedin.com/in/sudais-khalid/)  
**Discord:** [https://discord.com/invite/cfjfrec9](https://discord.com/invite/cfjfrec9)

**Academic Details:**
- Registration No: BSAI-23F-0050
- Program: BS Artificial Intelligence
- Semester: 03

## 📄 License

This project is available under the MIT License. See LICENSE file for details.

## 🔗 References

For more projects and implementations, visit: [Speech Emotion Analysis for Workplace Wellness](https://github.com/muhammadsudaiskhalid/Speech-Emotion-Analysis-for-Workplace-Wellness)

---

*This project demonstrates the practical application of machine learning in automotive price prediction, providing accessible tools for both technical and non-technical users.*
