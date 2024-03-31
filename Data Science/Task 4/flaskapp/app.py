from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from flask import Flask, render_template, request
import nltk
import pandas as pd
import numpy as np
nltk.download("punkt")
nltk.download("stopwords")
import pickle

import string
app = Flask(__name__,template_folder='templates')
ps = PorterStemmer()
def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  del text # free up memory space
  text = []
  for i in y:
    if i not in stopwords.words("english") and i not in string.punctuation:
      text.append(i)
  y.clear()
  for i in text:
    y.append(ps.stem(i))
  out = " ".join(y)
  del y # Free memory space
  del text # Free memory space
  return out



model = pickle.load(open('models/final_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer_final.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = vectorizer.transform(data).toarray()
        my_prediction = model.predict(vect)
        return render_template('output.html', prediction=my_prediction)
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html',prediction = prediction)

if __name__ == '__main__':
    app.run(debug=True)