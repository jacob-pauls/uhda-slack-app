import os
from flask import Flask, request, make_response, render_template

# Jacob Pauls
# Nov 21, 2020
# flask_module.py

# Module Context
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return 'Hello World'
    
if __name__ == '__main__':
    app.run()