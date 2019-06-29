from backend import app, dropzone, request
from flask import render_template
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('static', f.filename))

    return 'upload template'