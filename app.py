from flask import Flask, render_template, request, redirect, url_for
import os
import sys
import uuid
import re
from werkzeug.utils import secure_filename
from gpsclean.main import main as gpsclean_main
import tempfile

__name__ = 'GPSClean'

app = Flask(__name__)

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
    
    # create temporary directory
    temp_dir = tempfile.TemporaryDirectory()
     
     
    # generate random UUID
    userUUID = str(uuid.uuid4())

    # generate random UUID
    userUUID = str(uuid.uuid4())
    # get file name
    filename = traceFileObject.filename

    if filename == "":
        filename = "trace"

    print(f"FIle {traceFileObject}")

    print(f"Original filename {filename}")

    # sanitize it
    safeFileName = secure_filename(filename)

    print(f"Sanitized filename {safeFileName}")

    # temporary output path
    temporaryTracePath = os.path.join(temp_dir.name, safeFileName)

    # save trace file to temporary folder, using uuid + filename
    traceFileObject.save(temporaryTracePath)

    print(f"File saved in {temporaryTracePath}")

    # correct the trace using GPSClean package
    gpsclean_main([temporaryTracePath])

    # get corrected trace as string
    correctedFilePath = os.path.splitext(temporaryTracePath)[0] + "_cleaned.gpx"
    
    with open(correctedFilePath, "r") as data:

        correctedTraceMultiLine = data.read()

    with open(temporaryTracePath, "r") as data:

        original_trace = data.read()

    # clean files, we do not want left-overs
    temp_dir.cleanup()
    correctedTrace = correctedTraceMultiLine.replace('\n', ' ')
    original_trace = original_trace.replace('\n', ' ')
    
    # print(correctedTrace)
    return render_template('correct_trace.html', corrected_trace=correctedTrace, original_trace=original_trace)
    