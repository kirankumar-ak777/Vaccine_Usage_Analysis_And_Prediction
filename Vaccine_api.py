from flask import Flask, request, jsonify
import joblib
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        if request.method == 'POST':
            data = request.get_json()
        else:
            data = request.args

        # Validate if data is received properly
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        feature_keys = [
            'h1n1_worry', 'h1n1_awareness', 'bought_face_mask',
            'avoid_large_gatherings', 'dr_recc_h1n1_vacc', 'dr_recc_seasonal_vacc',
            'cont_child_undr_6_mnths', 'is_health_worker', 'has_health_insur',
            'is_h1n1_vacc_effective', 'is_h1n1_risky', 'is_seas_risky',
            'age_bracket', 'sex', 'marital_status'
        ]

        # Convert query parameters to a numpy array
        features = np.array([int(data.get(key, 0)) for key in feature_keys])
        print("Features received for prediction:", features)

        # Make prediction
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0].tolist()
        print("Prediction:", prediction, "Probability:", probability)

        return jsonify({'prediction': int(prediction), 'probability': list(probability)})


    except ValueError as e:
        return jsonify({'error': 'Invalid input. Please ensure all inputs are numeric.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
