from flask import Flask, render_template, request,url_for
from joblib import load
import numpy as np
import logging

app = Flask(__name__)
logging.basicConfig(filename="logs/app.txt",level=logging.DEBUG)
prediction = ""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            global prediction
            model = load('models/iris_model.joblib')
            data = request.form.to_dict()
            data = list(data.values())
            data = np.array(data,dtype=np.float64)
            data = data.reshape(1,-1)
            predicted = model.predict(data)
            if predicted == 0:
                prediction += "Iris Setosa"
                print(prediction)
                return render_template('output.html',prediction="Iris Setosa")
            elif predicted == 1:
                prediction += "Iris Versicolour"
                print(prediction)
                return render_template('output.html',prediction="Iris Versicolour")
            else:
                prediction += "Iris Virginica"
                print(prediction)
                return render_template('output.html',prediction="Iris Virginica")
        except Exception as e:
            logging.exception(e)
            return render_template('error.html',error=e)
    else:
        return render_template('predict.html')

@app.route("/output")
def output():
    return render_template("output.html", prediction=prediction)


if __name__ == '__main__':
    app.run()