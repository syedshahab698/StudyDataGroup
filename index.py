import dash_html_components as html
import dash_core_components as dcc


#from webui import WebUI
from app import app,flask_app
import callbacks

app.layout = html.Div(children = [
        dcc.Location(id='url', refresh=False),
        html.Nav(
                className = 'navbar navbar-expand-lg navbar-light bg-light',
                  
                children=[
                html.Div(className = "container text-uppercase text-secondary",children = [
                    html.A(children='StudyData Group',href='/apps/home', className = "navbar-brand"),
                    
                    html.Ul(className = "nav navbar-nav mr-auto mt-2 mt-lg-0",children = [
                        html.Li(className = "nav-item",children = [html.A(children = 'Machine Learning', className = "nav-link",href='/apps/machinelearning')]),
                        html.Li(className = "nav-item",children = [html.A(children = 'Deep Learning', className = "nav-link",href='/apps/deeplearning')]),
                        html.Li(className = "nav-item",children = [html.A(children = 'Computer vision', className = "nav-link",href='/apps/computervision')]),
                        html.Li(className = "nav-item",children = [html.A(children = 'Natural Language Processing', className = "nav-link",href='/apps/nlp')]),
                        html.Li(className = "nav-item",children = [html.A(children = 'Python Fundamentals', className = "nav-link",href='/apps/py')]),                      
                            ]),                      
                    html.Button(className = "btn btn-secondary float-right",children = [
                        html.A(className = "text-white",children=["Contact US"],href='#Home',)])

                    ])
                

               
            ]),
			
			html.Div(id="page-content"),
    
    html.Div(className = "footer-copyright text-center text-white py-3 bg-secondary",children = [
        "© 2020 Copyright: ",
        html.A(className = "text-white",children = " STUDYDATAGROUP",href="#Home")
           
        ])



    ],style = {'font-family': "Times New Roman"},className = "text-secondary")


    
    
    
    


if __name__ == "__main__":
    flask_app.run(debug=True,port = 8000)







