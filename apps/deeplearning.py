import dash_html_components as html
import dash_core_components as dcc

layout =html.Div([
		html.Div(className = "container text-uppercase ",children = [
                    html.Div(className = "row justify-content-md-center",children = [

                        html.Div(className = "col col-lg-4",children = [

                        		html.H1(children = "Deep Learning",style = {"font-size":'70px'}),

                            ]),
                       # html.Div(className = "col col-lg-2",children = []),
                       # html.Div(className = "col col-lg-4",children = [
                       #     html.Img(className="w-90",style = {'height':'500px','width':"800px"},src="/static/nlp.jpg")
                       #     ]),
                      
                        ])

                    ])
		])