# Import dependencies
from flask import Flask

# Note: Variables with underscores before an after them are called "magic methods" in Python.

# Create first Flask app instance
app = Flask(__name__)

# __name__ denotes the name of the current function.  Use __name__ to determine if the code is being run from the command line or if it has been imported into another piece of code.

# Create a Flask route.  First, define a starting point, which is known as the "root".  To do this, use @app.route('/')
# the forward slash inside of app.route() denoates that the data will root to our routes.  The forward slash is commonly known as the highest level of hierarchy in any computer system.
@app.route('/')
def hello_world():
    return 'Hello world!'