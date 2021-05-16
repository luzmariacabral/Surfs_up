# Import dependencies
from flask import Flask

# Create instace
app = Flask(__name__)

# Create route, define (starting point) aka root
@app.route('/')
def hello_world():
    return 'Hello world'
    