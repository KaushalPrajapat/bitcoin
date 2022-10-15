from distutils.log import debug
from flask import Flask, render_template,request
import pickle
import numpy as np


model = pickle.load(open('Mymodel.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/BitcoinPrediction', methods=['POST','GET'])
def prediction():
    gender = 0
    if request.method == 'POST':
        low=float(request.form['lowest'])
        open = float(request.form['open'])
        high=float(request.form['highest'])
        data = np.array([open,high,low])
        prediction=model.predict([data])
        

    return render_template('BitcoinPrediction.html',dta = (data,prediction))
    # return Data
@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug = True, port=8000)