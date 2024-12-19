Diamond Price Prediction Using Machine Learning

Project Overview:
This project aims to predict diamond prices based on their key attributes using supervised machine learning models. Various models were implemented, including Linear Regression, Decision Tree, KNN, and XGBoost, with XGBoost achieving the highest accuracy of 97.30%. The trained model was deployed via a Flask API for real-time predictions, which was tested and validated using Postman.

Features:
Flask API: Real-time predictions using a /predict endpoint that accepts JSON inputs.
Postman Testing: Validates the API for seamless integration and functionality.
EDA:Descriptive Statistics, Visualization, Correlation Analysis
Machine Learning Models: Includes Linear Regression, Decision Tree, KNN, and XGBoost for robust analysis.

Technologies Used:
Programming Language: Python
Machine Learning: Scikit-learn, Linear Regression, Decision Tree, KNN, and XGBoost
Visualization: Matplotlib, Seaborn
API Framework: Flask
API Testing: Postman

Installation
Follow these steps to set up and test the Diamond Price Prediction project:

Step 1: Unzip the Folder
Unzip the downloaded project folder containing all the necessary files.

Step 2: Download Required Tools
Ensure the following tools are installed on your system:

Python
Visual Studio Code (VSC)
Postman
Step 3: Upload Project in Visual Studio Code
Upload the entire unzipped project folder into Visual Studio Code.

Step 4: Open Terminal in VSC
In Visual Studio Code, open the terminal and navigate to the project folder.

Step 5: Install Dependencies and Run Python File
Run the following commands in the terminal to install necessary libraries and execute the Flask API:
pip install flask joblib pandas
python -c "import sklearn; print(sklearn.__version__)"
python app_service.py

Step 6: Copy the Local Host URL
After running the app_service.py file, a local host URL will be generated (e.g., http://127.0.0.1:8080). Copy this URL.

Step 7: Test the API Using Postman
Open Postman and set the request type to POST.
Enter the endpoint URL: <Local Host URL>/predict (e.g., http://127.0.0.1:8080/predict).
In the body section, select raw and JSON format.
Provide input data in JSON format:
{
    "carat": 0.5,
    "cut": "Premium",
    "color": "E",
    "clarity": "SI1",
    "depth": 61.5,
    "table": 55,
    "x": 5.1,
    "y": 8,
    "z": 3.1
}
Click Send.
View the predicted result in the response section.


Future Enhancements
User-Friendly Website: Design a front-end UI for user interaction.
Database Integration: Store data and user interactions for enhanced analysis.
Data Visualization: Add visual insights like price trends and feature importance.
Synthetic Datasets: Use synthetic data to improve model robustness and address biases.



