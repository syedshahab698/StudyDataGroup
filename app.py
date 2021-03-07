# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:40:43 2020

@author: syeds
"""

import dash
import flask


flask_app = flask.Flask(__name__)
bootstrapcss = ['https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
               ]
app = dash.Dash(__name__,external_stylesheets = bootstrapcss,server=flask_app, suppress_callback_exceptions=True)
app.title = "StudyData-Group"
#ui = WebUI(flask_app, debug=True)


    #ui.run()



