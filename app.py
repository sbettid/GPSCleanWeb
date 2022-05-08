from flask import Flask, render_template, request, redirect, url_for
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

    if traceFileObject is None: 
        return render_template('main.html')
    
     
    # generate random UUID
    userUUID = str(uuid.uuid4())
    # get file name
    filename = traceFileObject.filename
    # sanitize it
    safeFileName = secure_filename(filename)

    # temporary output path
    temporaryTracePath = os.path.join(app.config['uploadFolder'], userUUID + "_" + safeFileName)

    # save trace file to temporary folder, using uuid + filename
    traceFileObject.save(temporaryTracePath)

    # correct the trace using GPSClean package
    sys.argv = ["gpsclean", temporaryTracePath]
    gpsclean.main()

    # get corrected trace as string
    correctedFilePath = os.path.splitext(temporaryTracePath)[0] + "_cleaned.gpx"
    correctedFile = open(correctedFilePath, "r")

    correctedTrace = correctedFile.read()

    correctedFile.close()

    # clean files, we do not want left-overs
    os.remove(correctedFilePath)
    os.remove(temporaryTracePath) 
    print(correctedTrace)
    return render_template('correct_trace.html', corrected_trace=correctedTrace)
    