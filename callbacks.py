from app import app,flask_app
from dash.dependencies import Output, Input, State
import dash_html_components as html

from io import StringIO
import sys
from apps import home, machinelearning, deeplearning, computervision, nlp, python

import os
import numpy as np
from numpy import argmax
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# import base64
# import keras
# from keras.applications import vgg16
# from keras.preprocessing.image import img_to_array,load_img
# import tensorflow as tf

@app.callback(Output("page-content","children"),
              Input("url","pathname"))
def display_page(pathname):
    if pathname=="/apps/home":    
        return home.layout
    elif pathname=="/apps/machinelearning":
        
        return machinelearning.layout
    elif pathname=="/apps/deeplearning":
        
        return deeplearning.layout
    elif pathname=="/apps/computervision":
        
        return computervision.layout
    elif pathname=="/apps/nlp":
        
        return nlp.layout
    elif pathname=="/apps/py":
        
        return python.layout
    else:
        return home.layout

   
	


@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/datascience.jpeg")
    elif n % 3 == 2:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/deeplearning.jpeg")
    elif n % 3 == 0:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/machinelearning.jpeg")
    else:
        img = "None"
    return img

@app.callback(Output('image-nlp', 'children'),
              [Input('interval-nlp', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/nlp-application.jpg")
    elif n % 3 == 2:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/sentiment_analysis.jpg")
    elif n % 3 == 0:
        img = html.Img(className="w-90",style = {'height':'500px'},src="/static/text_summary.png")
    else:
        img = "None"
    return img


@app.callback(Output("python-output","value"),Input("python-input","value"))
def compile_python(the_code):
    loc = {}
    sys.stdout = StringIO()
    exec(the_code, globals(), loc)
    out = sys.stdout.getvalue()
    return " Variables : "+str(loc)+"\n Output :\n"+str(out)


def process(doc):
    stemmer= PorterStemmer()
    stop = stopwords.words('english')
    X = word_tokenize(doc)
    stemmed = [stemmer.stem(word) for word in X]
    clean = [word for word in stemmed if not word in stop]
    joined = ' '.join(clean)
    return joined
def Summarize(Text):
    tfidf=TfidfVectorizer(preprocessor=process)

    dataset=Text.replace("\n",'').split('.')

    mat=tfidf.fit_transform(dataset)
    matrix=mat.todense()

    svd_model = TruncatedSVD(n_components=7, 
                              random_state=42) 

    SVD=svd_model.fit_transform(matrix)
    X=svd_model.components_

    singular_matrix = np.diag(svd_model.singular_values_)
    Docs_relation=SVD.dot(singular_matrix)
    short_list=sorted(list(set([0]+[argmax(Docs_relation[:,i])for i in range(Docs_relation.shape[1])])))
    return [dataset[i] for i in short_list]

@app.callback(Output("text-summary-output","children"),Input("text-summary-input","value"))
def summarize_text(Text):
    short_list = Summarize(Text)
    return "\n".join(short_list)   

# def get_image_preds(contents):
#     image = decode_and_resize(contents)
#     #image = base64.b64decode(contents)#load_img(,target_size=(224,224))
#     imagearray = img_to_array(image)

#     imagearray = imagearray.reshape(1,imagearray.shape[0],imagearray.shape[1],imagearray.shape[2])
#     imagearray = vgg16.preprocess_input(imagearray)

#     model=vgg16.VGG16()
#     pred = model.predict(imagearray)
#     name = vgg16.decode_predictions(pred)[0][0][1]

#     return name

@app.callback( [Output("image-output" ,"children" ),Output("display-image","src")] ,
    [Input('image-input', 'contents'),
    State('image-input', 'filename'),  ] )
def get_image_class(uploaded_file_contents,uploaded_filenames):
    #class_name=get_image_preds(contents)
    return ["Is this a {}!".format(uploaded_filenames),uploaded_file_contents]