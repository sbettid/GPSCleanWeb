from flask import Flask, render_template, request

__name__ = 'GPSClean'

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('main.html')

@app.route("/correct_trace")
def correct_trace(methods=['POST']):
    return "Got " + request.form.get('file')