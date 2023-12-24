import sqlite3
import json

import plotly
from flask import Flask, render_template, request, redirect, url_for, session
from services import bmi_calculator, create_user, login, write_to_db, data_visualization

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        userid = request.form.get('userid')
        password = request.form.get('password')
        conn = sqlite3.connect('database/master.db')  # Update this with your database path
        if login.login_user(userid, password, conn):
            session['userid'] = userid  # Store the userid in session
            return redirect(url_for('bmi'))  # Redirect to the BMI page
        else:
            return "Invalid login credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        conn = sqlite3.connect('./database/master.db')  # Update this with your database path
        userid = create_user.create_user(name, age, email, password, conn)
        return f"Registration successful. Your user ID is {userid}"
    return render_template('register.html')
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')
        units = {'weight': 'kg', 'height': 'cm'}  # Update this based on your form
        bmi = bmi_calculator.calculate_bmi(weight, height, units)

        # Save BMI to database
        conn = sqlite3.connect('./database/master.db')  # Update this with your database path
        userid = session.get('userid')  # Get the userid from session
        write_to_db.write_bmi_to_db(userid, bmi, conn)

    return render_template('bmi.html')

@app.route('/data_visualization')
def data_visualization():
    # Generate the Plotly figure
    fig = data_visualization.plot_bmi_data()

    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the template with the figure
    return render_template('data_visualization.html', fig_json=fig_json)

if __name__ == "__main__":
    app.run(debug=True)