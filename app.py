# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:40:43 2020

@author: syeds
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import flask
from apps import home, machinelearning, deeplearning, computervision, nlp
#from webui import WebUI


flask_app = flask.Flask(__name__)
bootstrapcss = ['https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
               ]
app = dash.Dash(__name__,external_stylesheets = bootstrapcss,server=flask_app, suppress_callback_exceptions=True)
app.title = "StudyData-Group"
#ui = WebUI(flask_app, debug=True)

app.layout = html.Div(children = [
        dcc.Location(id='url', refresh=False),
        html.Nav(
                className = 'navbar navbar-expand-lg navbar-light bg-light',
                  
                children=[
                html.Div(className = "container text-uppercase",children = [
                    html.Div(className = "row justify-content-center ",children = [

                        html.Div(id="Home",className = "col m-1 h4",children = [
                            html.A(children='StudyData Group',href='/apps/home', className = "navbar-brand font-weight-bold"),
                            ]),
                        html.Div(className = "col-md-auto",children = [
                            html.Ul(className = "navbar-nav mr-auto mt-2 mt-lg-0",children = [
                                html.Li(className = "nav-item",children = [html.A(children = 'Machine Learning', className = "nav-link",href='/apps/machinelearning')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Deep Learning', className = "nav-link",href='/apps/deeplearning')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Computer vision', className = "nav-link",href='/apps/computervision')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Natural Language Processing', className = "nav-link",href='/apps/nlp')]),
              
                                ])
                            ]),
                        html.Div(className = "col float-right",children = [
                            html.Button(className = "btn btn-secondary float-right",children = [
                                html.A(className = "text-white",children=["Contact US"],href='#Home',)])
                            ])
                        ])

                    ])
                

               
            ]),
			
			html.Div(id="page-content"),
    
    html.Div(className = "footer-copyright text-center text-white py-3 bg-secondary",children = [
        "© 2020 Copyright: ",
        html.A(className = "text-white",children = " STUDYDATAGROUP",href="#Home")
           
        ])



    ],style = {'font-family': "Times New Roman"})

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

    
    
    
    


if __name__ == "__main__":
    flask_app.run()
    #ui.run()



