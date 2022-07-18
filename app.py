from flask import Flask, render_template, request #importing the necessary libraries 
import pickle

from numpy import product

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])# this code block is to show the user html page to enter the details to be predicted and the clicking the submit button
def hello():
    print("Request for index page received")
    return render_template('index2.html')

@app.route('/predict', methods = ['POST']) #This code block is when the user clicked the submit button details from html page will be received using "request.form" and predictio
                                           #will be done based on the array
def prediction():
    if request.method == 'POST':
        product = request.form['product']
        fro = request.form['fro']
        to = request.form['to']
        quantity = request.form['quantity']
        permt = request.form['permt']
        commo = request.form['commo']

        data = [[product, fro, to, float(quantity), permt, commo]]
        model = pickle.load(open('revenue.pkl', 'rb'))

        prediction = model.predict(data)[0]

    return render_template('result.html', n = prediction)# result will be posted on the prediction page


if __name__ == '__main__': #main execution code
    app.run()