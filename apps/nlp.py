import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([

		
		 html.Div(className = "container text-uppercase",children = [
                    html.Div(className = "row justify-content-md-center",children = [

                        html.Div(className = "col col-lg-6 p-5",children = [
                        		html.H1(children = "Natural Language Processing",style = {"font-size":'70px'}),

                            ]),
                       #  html.Div(className = "col col-lg-1",children = []),
                        html.Div(className = "col col-lg-6",children = [

							html.Section(id="slideshow", children=[
							    html.Div(id="slideshow-container", children=[
							        html.Div(className = "d-flex justify-content-center border border-light p-5",id="image-nlp"),
							        dcc.Interval(id='interval-nlp', interval=3000)
							    ])
							]),

							])
                        ])

                    ]),

		 

		 html.Div(className = "row justify-content-md-center bg-light",children = [

		 	dcc.Markdown(className = "p-5",children ='''
# Text Summarization!
Text Analytics project using Text Preprocessing, TFIDF Vectorizer, Singular Value Decomposition!
''')  ,
	#html.H1(className = "p-5",children = "Text Summarization!"),
	#html.P(className = "p-5",children = "Text Analytics Project -"),

	html.Div(className = "col col-lg-6 p-5 ",children = [
    		dcc.Textarea(
    			className = "p-5",
        id='text-summary-input',
        placeholder = "Paste a Document to Summarize!",
        style={'width': '100%', 'height': 400},
    ),
			]),
        html.Div(className = "col col-lg-6 p-5",children = [
        	html.H5("Summary of Document!"),
        	html.P(
        		className = "p-5",
        id='text-summary-output',
        children='',
        style={'width': '100%', 'height': 300},
    ),
			]),
        html.P(className="text-center .bg-secondary", children=["Project by : ",
        	html.A(className="text-dark",children="Nikhil Kumar Thakur",href="https://www.linkedin.com/in/nikhil-kumar-thakur-11872891/")
        	],style = {'font-size':"20px"})
	]),

		 html.Div(className ="Jumbotron text-center p-5 bg-light",children="",style = {"font-size":'70px'}),

		])