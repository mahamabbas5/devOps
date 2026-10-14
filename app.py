
import os
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your registration number as an environment variable.
REGISTRATION_NUMBER = os.environ.get(
    "STUDENT_ROLL_NUMBER", "FA23-BDS-019"
)

# Generate deterministic coefficients.
random.seed(REGISTRATION_NUMBER)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])

        prediction = a1*x1 + a2*x2 + a3*x3 + b

        return jsonify({
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction, 2)
        })

    except (KeyError, ValueError):
        return jsonify({
            "error": "Provide numeric x1, x2, and x3 parameters."
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
