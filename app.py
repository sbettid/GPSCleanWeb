from flask import Flask, render_template

__name__ = 'GPSClean'

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('main.html')