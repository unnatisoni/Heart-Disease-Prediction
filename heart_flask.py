# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:03:15 2020

@author: ANCHAL SONI
"""

import numpy as np
from flask import Flask, render_template, request,jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open("F:\machine learning\heart Disease Prediction\heart_mod.sav", "rb"))

@app.route("/")

def home():
    return render_template('index_form.html')


def valuepredictor(to_predict_list):
    to_predict  = np.array(to_predict_list).reshape(1,-1)
    loaded_model= pickle.load(open("F:\machine learning\heart Disease Prediction\heart_mod.sav","rb"))
    result=loaded_model.predict(to_predict)
    return result[0]

@app.route('/results',methods = ['POST'])
def results():
    if request.method == 'POST':
        to_predict_list=request.form.to_dict()
        to_predict_list= list(to_predict_list.values())
        to_predict_list = list(map(int,to_predict_list))
        result= valuepredictor(to_predict_list)
        if int(result) == 1:
            prediction= "You have the heart disease, Contact to you doctor!!"
        else:
            prediction="You are fine "
        return render_template("index_form.html", prediction=prediction)
         
app.run()