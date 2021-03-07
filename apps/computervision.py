import dash_html_components as html
import dash_core_components as dcc

layout =html.Div([

		html.Div(className = "container text-uppercase ",children = [
                    html.Div(className = "row justify-content-md-center",children = [

                        html.Div(className = "col col-lg-4",children = [
                        		html.H1(children = "Computer Vision",style = {"font-size":'70px'}),

                            ]),
                       # html.Div(className = "col col-lg-2",children = []),
                       # html.Div(className = "col col-lg-4",children = [
                       #     html.Img(className="w-90",style = {'height':'500px','width':"800px"},src="/static/nlp.jpg")
                       #     ]),
                      
                        ])

                    ]),
		html.H2(className = "p-5", children = "Image Classification!",style = {"font-size":'40px'}),
		html.Div(className = "row justify-content-md-center",children = [
			html.Div(className = "col p-5",children = [
				dcc.Upload(className = "custom-file-input",
			        id='image-input',
			        children=html.Div([
			            'Drag and Drop or ',
			            html.A('Select Files')
			        ]),
			        style={
            'width': '70%',
            'height': '150px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }

				),]),
			html.Div(className="col p-5", children = [
					html.Img(id="display-image"),
					html.H6(id = "image-output",style= { 'font-size':"40px" })

				] )


			])
		])