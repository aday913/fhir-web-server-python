# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from fhir.resources.patient import Patient

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your Vue frontend

@app.route('/api/patient')
def get_patient():
    # Construct a basic FHIR Patient resource using fhir.resources
    patient = Patient.model_construct(
        id="example",
        active=True,
        name=[{"family": "Doe", "given": ["John"]}]
    )
    return jsonify(patient.dict())

if __name__ == "__main__":
    app.run(debug=True)

