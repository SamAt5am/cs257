'''
    app.py
    Sam Hiken James Brink

    API for the Crossword Crunch the website
    9 Novemeber 2022
'''
import flask
import argparse
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/') 
def home():
    return flask.render_template('index.html')

@app.route('/dates') 
def dates():
    return flask.render_template('dates.html')

@app.route('/about') 
def about():
    return flask.render_template('about.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A crossword application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
