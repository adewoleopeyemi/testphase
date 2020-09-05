# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 04:07:24 2020

@author: adewole opeyemi
"""
import os
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

from . import train

app=Flask(__name__)
Swagger(app)


port = int(os.environment.get('PORT', 5000))

@app.route('/')
def welcome():
    return 'Welcome All'
'''
@app.route('/predict',methods=['Get'])
def predict_note_authentication():
    
    '''''''Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
            
    '''''''
    
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The predicted value is '+str(prediction)
'''

@app.route('/predict_file', methods=['POST'])
def predict_image_file():
    '''Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
        
    responses:
        200:
            description: The output values
    '''
    model = load_model("nudedetectionalgorithm.h5")

    img=Image.open(request.files.get('file'))
    img=Img.resize((124, 124))
    img = np.array(img)
    img = img/255.
    prediction = model.predict(img)
    if prediction < 0.5:
        return 'The uploaded image contains nude contents and is not allowed'
    else:
        return "The uploaded image doesn't contain any form of nudity you look good to go"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
