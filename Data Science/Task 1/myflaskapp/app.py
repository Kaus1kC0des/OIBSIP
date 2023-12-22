from flask import Flask, render_template, request, url_for, redirect,session
from joblib import load



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        try:
            model = load("../../models/iris_model.joblib")
            sepal_length = float(request.form["sepal_length"])
            sepal_width = float(request.form["sepal_width"])
            petal_length = float(request.form["petal_length"])
            petal_width = float(request.form["petal_width"])
            prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
            return redirect(url_for('output'))
        except Exception as e:
            return render_template("error.html",error=e)
    elif request.method == "GET":
        try:
            return render_template("predict.html")
        except Exception as e:
            return render_template("error.html",error=e)

@app.route("/output", methods=["GET"])
def output():
    prediction = session.get('prediction', None)
    return render_template("output.html", prediction=prediction)



if __name__=="__main__":
    app.run()

