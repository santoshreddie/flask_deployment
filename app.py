from flask import Flask, render_template, request
import pickle

from numpy import product

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def hello():
    print("Request for index page received")
    return render_template('index2.html')

@app.route('/predict', methods = ['POST'])
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

    return render_template('result.html', n = prediction)


if __name__ == '__main__':
    app.run()