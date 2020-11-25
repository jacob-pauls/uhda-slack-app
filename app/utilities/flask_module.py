from flask import Flask, request, make_response

# Jacob Pauls
# Nov 24, 2020
# flask_module.py

def initialize_flask_app():

    # Load Default Configuration
    app = Flask(__name__)

    # Index Mapping
    @app.route("/", methods=["GET"])
    def home():
        return 'UHDA SlackApp is running!'

    return app