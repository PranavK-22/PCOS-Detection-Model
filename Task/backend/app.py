from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import traceback

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

model = joblib.load("Task/backend/models/pcos_model.pkl")
label_encoders = joblib.load("Task/backend/models/encoders.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("\n=== Raw input data ===")
        print(data)

        input_df = pd.DataFrame([data])
        print("\n=== DataFrame before encoding ===")
        print(input_df)

        # Renaming columns to match model's expected feature names
        input_df.rename(columns={
            'pain': 'Pain',
            'weightGain': 'Weight Gain',
            'cycleDelay': 'Cycle Delay',
            'acne': 'Acne',
            'polycysticOvaries': 'Polycystic Ovaries',
            'excessiveHairGrowth': 'Excessive Hair Growth',
            'scalpHairLoss': 'Scalp Hair Loss',
            'infertility': 'Infertility',
            'darkSkinPatches': 'Dark Skin Patches'
        }, inplace=True)

        print("\n=== DataFrame after renaming ===")
        print(input_df)

        # Applying label encoders on renamed columns
        for column in label_encoders:
            if column in input_df.columns:
                try:
                    input_df[column] = label_encoders[column].transform(input_df[column])
                except Exception as e:
                    print(f"\nLabel encoding failed for {column}: {str(e)}")
                    return jsonify({'error': f'Encoding failed for {column}: {str(e)}'}), 500

        print("\n=== DataFrame after encoding ===")
        print(input_df)

        
        expected_cols = [
            'Pain', 'Weight Gain', 'Cycle Delay', 'Acne',
            'Polycystic Ovaries', 'Excessive Hair Growth',
            'Scalp Hair Loss', 'Infertility', 'Dark Skin Patches'
        ]
        input_df = input_df[expected_cols]

        prediction = model.predict(input_df)[0]
        result = "Likely PCOS" if prediction == 1 else "Unlikely PCOS"

        return jsonify({'result': result})

    except Exception as e:
        print("\n=== Error traceback ===")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)