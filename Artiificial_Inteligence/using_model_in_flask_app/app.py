import warnings
from flask import Flask, request, jsonify
import pickle
import joblib

# Ignore warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    
    age = request.args.get('age')
    gender = request.args.get('gender')

    # Load Pickle model
    model = pickle.load(open('music-recommender.pkl', 'rb'))
    pickle_predection = model.predict([[age, gender]])
    print("Pickle model's output : ", pickle_predection)

    # Load joblib model
    model = joblib.load("music-recommender.joblib")
    joblib_predictions = model.predict([[age, gender]])
    print("Joblib model's output : ", joblib_predictions)


    return jsonify({ 'Pickle_prediction' : pickle_predection.tolist(),
                    'Joblib_prediction' : joblib_predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)