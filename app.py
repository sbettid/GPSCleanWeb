from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from gpsclean.main import main as gpsclean_main
import tempfile
import os
import sys

__name__ = 'GPSClean'
TEST_TRACES_PATH = "./test_traces"

app = Flask(__name__)

# main page
@app.route("/")
def render_main():
    
    return render_template('main.html')

@app.route("/correct_example_trace", methods=['GET'])
def correct_example_trace():
    with open(f"{TEST_TRACES_PATH}/test_trace_cleaned.gpx", "r") as data:
        corrected_trace = data.read()

    with open(f"{TEST_TRACES_PATH}/test_trace.gpx", "r") as data:
        original_trace = data.read()

    corrected_trace = corrected_trace.replace('\n', ' ')
    original_trace = original_trace.replace('\n', ' ')
    
    return render_template('correct_trace.html', corrected_trace=corrected_trace, original_trace=original_trace, original_trace_name="test_trace", test_trace=True)
    

# correct trace page
@app.route("/correct_trace", methods=['POST'])
def correct_trace():
    
    # get trace file, if any
    trace_file = request.files.get('trace')

    if trace_file is None: 
        return render_template('main.html')
    
    # create temporary directory
    temp_dir = tempfile.TemporaryDirectory()
     
    # get file name
    filename = trace_file.filename

    if filename == "":
        filename = "trace"

    # sanitize it
    safe_filename = secure_filename(filename)

    # temporary output path
    original_trace_filepath = os.path.join(temp_dir.name, safe_filename)

    # save trace file to temporary folder, using uuid + filename
    trace_file.save(original_trace_filepath)

    # correct the trace using GPSClean package
    gpsclean_main([original_trace_filepath])

    # get corrected trace as string
    corrected_trace_path = os.path.splitext(original_trace_filepath)[0] + "_cleaned.gpx"
    
    with open(corrected_trace_path, "r") as data:

        corrected_trace = data.read()

    with open(original_trace_filepath, "r") as data:

        original_trace = data.read()

    # clean files, we do not want left-overs
    temp_dir.cleanup()

    corrected_trace = corrected_trace.replace('\n', ' ')
    original_trace = original_trace.replace('\n', ' ')
    
    original_trace_name = os.path.splitext(original_trace_filepath)[0].rsplit("/", 1)[-1]

    return render_template('correct_trace.html', corrected_trace=corrected_trace, original_trace=original_trace, original_trace_name=original_trace_name, test_trace=False)

@app.route("/privacy", methods=['GET'])
def privacy():
    return render_template('privacy.html')