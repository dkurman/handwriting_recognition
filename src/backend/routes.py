from backend import app, dropzone, request, photos
from flask import render_template
import os
from flask import Flask, redirect, render_template, request, session, url_for

@app.route('/')
@app.route('/index')
def index():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    
    return render_template('res.html', file_urls=file_urls)



@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return redirect(url_for('index'))