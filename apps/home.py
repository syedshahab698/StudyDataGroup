import dash
import dash_html_components as html
import dash_core_components as dcc




layout =html.Div([

	html.Div(className = "justify-content-center",children = [
	html.Div(className = "w-100 d-flex jumbotron justify-content-center",
	    children=[html.H1(className = "w-50  p-5 text-center",children = 'Portfolio Site Of Study Data Group!',style = {"font-size":'100px'}),
	        ]
	    ),
	html.P(className = "w-100  p-2 text-center",children = 'We are Data Science enthusiasts and this has website has some interesting projects we did.',style = {"font-size":'25px'})
	   ]) ,

	html.Div(children = [

	html.Section(id="slideshow", children=[
	    html.Div(id="slideshow-container", children=[
	        html.Div(className = "d-flex justify-content-center border border-light p-5",id="image"),
	        dcc.Interval(id='interval', interval=3000)
	    ])
	]),

	])

	])
