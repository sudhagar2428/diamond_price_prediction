import joblib
from flask import Flask, request, jsonify
import pandas as pd

# Load the model
model = joblib.load('diamond_price_model.pkl')

app = Flask(__name__)


cut_mapping = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_mapping = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
clarity_mapping = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

@app.route('/predict', methods=['POST'])
def predict_price():
    data = request.json  

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        
        feature_columns = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
        
        filled_data = {col: data.get(col, 0) for col in feature_columns}

        
        filled_data['cut'] = cut_mapping.get(filled_data['cut'], 0)
        filled_data['color'] = color_mapping.get(filled_data['color'], 0)
        filled_data['clarity'] = clarity_mapping.get(filled_data['clarity'], 0)

        
        input_df = pd.DataFrame([filled_data])

        
        prediction = model.predict(input_df)
        predicted_price = prediction[0]

        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
