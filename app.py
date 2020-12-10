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

flask_app = flask.Flask(__name__)
bootstrapcss = ['https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css']
app = dash.Dash(__name__,external_stylesheets = bootstrapcss,server=flask_app)
app.title = "STUDYDATA-GROUP"

app.layout = html.Div(children = [

        html.Nav(
                className = 'navbar navbar-expand-lg navbar-light bg-light',
                  
                children=[
                html.Div(className = "container text-uppercase ",children = [
                    html.Div(className = "row justify-content-center d-flex",children = [

                        html.Div(id="Home",className = "col",children = [
                            html.A('StudyData Group', className = "navbar-brand font-weight-bold",href='https://github.com/syedshahab698'),
                            ]),
                        html.Div(className = "col-md-auto",children = [
                            html.Ul(className = "navbar-nav mr-auto mt-2 mt-lg-0",children = [
                                html.Li(className = "nav-item",children = [html.A(children = 'Machine Learning', className = "nav-link",href='#Home')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Deep Learning', className = "nav-link",href='#Home')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Computer vision', className = "nav-link",href='#Home')]),
                                html.Li(className = "nav-item",children = [html.A(children = 'Natural Language Processing', className = "nav-link",href='#Home')]),
              
                                ])
                            ]),
                        html.Div(className = "col float-right",children = [
                            html.Button(className = "btn btn-secondary float-right",children = [
                                html.A([
                                    "Contact US"])])
                            ])
                        ])

                    ])
                

               
            ]),
    html.Div(className = "justify-content-center",children = [
    html.Div(className = "w-100 d-flex jumbotron justify-content-center",
        children=[html.H1(className = "w-50  p-5 text-center",children = 'Portfolio Page of Study Data group!',style = {"font-size":'100px'}),
            ]
        ),
    html.P(className = "w-100  p-2 text-center",children = 'We are Data Science enthusiast and this has website has some interesting projects we did.',style = {"font-size":'25px'})
       ]) ,

    html.Div(children = [

    html.Section(id="slideshow", children=[
        html.Div(id="slideshow-container", children=[
            html.Div(id="image"),
            dcc.Interval(id='interval', interval=3000)
        ])
    ]),

   # html.Footer(className = "page-footer font-small blue pt-4",children = [

  #      html.Div(className = "container-fluid text-center text-md-left",children = [

   #         html.Div(className = "row",children=[
#
    #            html.Div(className = "col-md-6 mt-md-0 mt-3",children=[
   #                 html.H5(className = "text-uppercase",children = "STUDYDATAGROUP"),
     #               html.P("Exploring Cool New Possibilities in the Field of DataScience")
     #               ]),
     #           html.Div(className = "col-md-6 mb-md-0 mb-3",children = [
    #                html.H5(className = "text-uppercase",children="GITHUB LINKS"),
   #                 html.Ul(className="list-group list-group-flush",children=[
   #                     html.Li(
  #                          html.A(className="list-group-item",children="Sai Krishna",href="https://github.com/syedshahab698"),
  #                          ),
   #                     html.Li(
    #                        html.A(className="list-group-item",children="Nikhil Kumar",href="https://github.com/syedshahab698"),
  #                          ),
  #                      html.Li(
   #                         html.A(className="list-group-item",children="Mani Kumar",href="https://github.com/syedshahab698"),
   #                         ),
   #                     html.Li(
    #                        html.A(className="list-group-item",children="Syed Shahab",href="https://github.com/syedshahab698"),
   ##                         )

   #                     ])

   #                 ])
#
    #            ])
#
      #      ])

       # ]),
    html.Div(className = "footer-copyright text-center py-3",children = [
        "© 2020 Copyright:",
        html.A(children = "STUDYDATAGROUP",href="#Home")
           
        ])

])

    ],style = {'font-family': "Times New Roman"})

@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(className="w-100",style = {'height':'500px'},src="http://placeimg.com/625/200/any")
    elif n % 3 == 2:
        img = html.Img(className="w-100",style = {'height':'500px'},src="http://placeimg.com/625/200/animals")
    elif n % 3 == 0:
        img = html.Img(className="w-100",style = {'height':'500px'},src="http://placeimg.com/625/200/arch")
    else:
        img = "None"
    return img

    
    
    
    


if __name__ == "__main__":
    flask_app.run()




