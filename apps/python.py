import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([

html.Div(className = "container text-uppercase",children = [
    html.Div(className = "row justify-content-md-center",children = [
		html.Div(className = "col col-lg-6 p-5",children = [
    		html.H1(children = "Python Fundamentals",style = {"font-size":'70px'}),
			]),
        html.Div(className = "col col-lg-6",children = [
			html.Section(id="slideshow", children=[
			    html.Div(id="slideshow-container", children=[
			        html.Div(className = "d-flex justify-content-center border border-light p-5",id="image-py"),
			        dcc.Interval(id='interval-py', interval=3000)
			    	])
				]),

			])
    	])

    ]),

html.Div(className = "row justify-content-md-center",children = [
	html.H1(className = "p-5",children = "Python Interpreter!"),
	html.Div(className = "col col-lg-6 p-5",children = [
    		dcc.Textarea(
    			className = "p-5",
        id='python-input',
        placeholder = "Enter Python Code.",
        style={'width': '100%', 'height': 300},
    ),
			]),
        html.Div(className = "col col-lg-6 p-5",children = [
        	dcc.Textarea(
        		className = "p-5",
        id='python-output',
        value='Output of Python Code.',
        style={'width': '100%', 'height': 300},
        disabled = True
    ),
			])
	]),

html.Div(className ="Jumbotron text-center p-5 bg-light",children="Python Concepts Coming SOON!",style = {"font-size":'70px'})

		])