from flask import Flask, request
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)

from backend import routes