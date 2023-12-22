# Iris Classifier Flask Application

This project is a Flask web application that uses a Machine Learning model to classify the Iris dataset. The application is structured according to best programming practices, ensuring easy management and scalability.

## Project Structure

The project is structured as follows:

- `myflaskapp`: The root directory of the application.
- `app`: This directory contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `templates`: Contains all HTML templates.
  - `static`: Contains all static files like CSS, JavaScript, images etc.
  - `models`: Contains the machine learning model files.
  - `views.py`: Contains the routes of the application.
  - `models.py`: Contains the code for loading and using the machine learning models.
- `tests`: Contains all the test cases for the application.
- `config.py`: Contains configuration variables for the Flask app.
- `main.py`: The file that is run to start the Flask server and the application.

## Functionality

The application provides a user interface where users can input the parameters of an Iris flower. These parameters are then processed by a Machine Learning model to classify the Iris flower into one of the three species: Setosa, Versicolor, or Virginica.

## Technologies Used

- **Python**: The main programming language used for developing the application and the Machine Learning model.
- **Flask**: A lightweight web application framework used for serving the application.
- **SQL**: Used for any database interactions if required.
- **Machine Learning**: Used for creating the model that classifies the Iris flowers.

## Running the Application

To run the application, navigate to the root directory (`myflaskapp`) and execute the `run.py` script. This will start the Flask server and the application.

## Testing

Tests for the application are located in the `tests` directory. These tests can be run to verify the functionality of the application and the Machine Learning model.

## Future Improvements

While the application currently serves its purpose well, future improvements could include adding more Machine Learning models to classify other types of data, improving the user interface, and adding more comprehensive tests.