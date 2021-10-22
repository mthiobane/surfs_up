# To import the Flask dependency, add the following to your code:
from flask import Flask
# Create a New Flask App Instance
app = Flask(__name__)
# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
# Create Flask Routes/about
@app.route('/test')
def about():
    return 'This is a tutorial Flask app on serving routes'