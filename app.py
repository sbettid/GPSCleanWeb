from flask import Flask, render_template, request
import os
import sys
import uuid
import re
from werkzeug.utils import secure_filename
from gpsclean import gpsclean

__name__ = 'GPSClean'
uploadTracesPath = "upload"

app = Flask(__name__)
app.config['uploadFolder'] = uploadTracesPath

# main page
@app.route("/")
def render_main():
    
    return render_template('main.html')

# correct trace page
@app.route("/correct_trace", methods=['POST'])
def correct_trace():
    
    # get trace file, if any
    traceFileObject = request.files.get('trace')
    
    # if trace file is None, go to main page
    if not traceFileObject: 
        return render_template('main.html')
    
    # generate random UUID
    userUUID = str(uuid.uuid4())
    # get file name
    filename = traceFileObject.filename
    # sanitize it
    safeFileName =secure_filename(filename)

    # temporary output path
    temporaryTracePath = os.path.join(app.config['uploadFolder'], userUUID + "_" + safeFileName)

    # save trace file to temporary folder, using uuid + filename
    traceFileObject.save(temporaryTracePath)

    # correct the trace using GPSClean package
    sys.argv = ["gpsclean", temporaryTracePath]
    gpsclean.main()

    return ""
    