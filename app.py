from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Model load karo
model = joblib.load('ids_random_forest_model.pkl')

# Column names list (ab label aur difficulty nahi hain)
cols = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent",
        "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
        "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count",
        "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
        "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
        "dst_host_srv_rerror_rate"]

# Dataset ka structure load karo preprocessing ke liye
try:
    dummy_data = pd.read_csv("KDDTrain+.txt", names=cols + ['label', 'difficulty'])
except FileNotFoundError:
    dummy_data = pd.read_csv("KDDTrain+.TXT", names=cols + ['label', 'difficulty'])
    
dummy_data_for_processing = dummy_data.drop(['label', 'difficulty'], axis=1)

categorical_cols = dummy_data_for_processing.select_dtypes(include=['object']).columns
dummy_data_encoded = pd.get_dummies(dummy_data_for_processing, columns=categorical_cols, drop_first=True)
numerical_cols = dummy_data_encoded.select_dtypes(include=['int64', 'float64']).columns
    
scaler = StandardScaler()
scaler.fit(dummy_data_encoded[numerical_cols])

app = Flask(__name__)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['features']
        
        # Aane wale data ka DataFrame banao
        input_data = pd.DataFrame([data], columns=cols)
        
        # Categorical columns ko encode karo
        input_encoded = pd.get_dummies(input_data, columns=categorical_cols, drop_first=True)
        
        # Input columns ko trainig columns ke hisab se align karo
        final_input = input_encoded.reindex(columns=dummy_data_encoded.columns, fill_value=0)
        
        # Numerical values ko scale karo
        final_input[numerical_cols] = scaler.transform(final_input[numerical_cols])
        
        # Prediction lo
        prediction = model.predict(final_input)[0]
        proba = model.predict_proba(final_input)[0][1]
        
        # Prediction ko user-friendly format me convert karo
        if prediction == 0:
            result = "Normal Traffic"
        else:
            result = "Attack Detected"
            
        return jsonify({
            'prediction': result,
            'risk_score': round(float(proba) * 100, 2)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)