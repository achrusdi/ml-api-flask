# ==== IMPORT LIBRARY ====
import pandas as pd
import numpy as np
import pickle as pkl
from flask import Flask, redirect, url_for, render_template, request, Response

# ==== LOAD MODEL ====
model = pkl.load(open('finalized_model_logreg.sav', 'rb'))

# ==== CREATE FLASK APP ====
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['gender']
        Married = request.form['married']
        Dependents = request.form['dependents']
        Education = request.form['edu']
        Self_Employed = request.form['self_employed']
        ApplicantIncome = request.form['app_income']
        CoapplicantIncome = request.form['coapp_income']
        LoanAmount = request.form['loan_amount']
        Loan_Amount_Term = request.form['loan_amount_term']
        Credit_History = request.form['credit']
        Property_Area = request.form['property']
        dt = pd.DataFrame({'Gender': [Gender],
                           'Married': [Married],
                           'Dependents': [Dependents],
                           'Education': [Education],
                           'Self_Employed': [Self_Employed],
                           'ApplicantIncome': [ApplicantIncome],
                           'CoapplicantIncome': [CoapplicantIncome],
                           'LoanAmount': [LoanAmount],
                           'Loan_Amount_Term': [Loan_Amount_Term],
                           'Credit_History': [Credit_History],
                           'Property_Area': [Property_Area]})
        prediction = model.predict(dt.values)
        no = 'User ini TIDAK LAYAK mendapat Pinjaman'
        yes = 'User ini LAYAK mendapat Pinjaman'
        if prediction == 'N':
            return render_template('home.html', out_no=no)
        elif prediction == 'Y':
            return render_template('home.html', out_yes=yes)

    # return render_template('home.html')


@app.route('/intro')
def intro():
    return render_template('intro.html')


if __name__ == '__main__':
    app.run(debug=True)
