from flask import *

app = Flask(__name__)
@app.route('/')
def test():
    return "WORKS"