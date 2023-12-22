import logging
from flask import Flask, render_template, request, redirect, url_for
from joblib import load

# Set up logging
logging.basicConfig(filename='logs/app.txt', level=logging.INFO)

app = Flask(__name__)

# Load model
model = load("models/iris_model.joblib")
global prediction

@app.route("/")
def home():
    logging.info("Home page accessed")
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            sepal_length = float(request.form["sepal_length"])
            sepal_width = float(request.form["sepal_width"])
            petal_length = float(request.form["petal_length"])
            petal_width = float(request.form["petal_width"])
            features = [sepal_length, sepal_width, petal_length, petal_width]
            prediction = model.predict([[features]])
            if prediction[0] == 0:
                prediction = "Setosa"
            elif prediction[0] == 1:
                prediction = "Versicolor"
            else:
                prediction = "Virginica"
            return output(prediction)

        except Exception as e:
            logging.error(f"Error occurred during prediction: {e}")
            return render_template("error.html", error=e)

    elif request.method == "GET":
        logging.info("Prediction page accessed")
        return render_template("predict.html")


@app.route("/output")
def output(prediction):
    logging.info(f"Output page accessed, prediction: {prediction}")
    return render_template('output.html', prediction=prediction)



if __name__ == "__main__":
    app.run()