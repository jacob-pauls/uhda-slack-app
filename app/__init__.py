from flask_api import FlaskAPI

# Jacob Pauls
# Nov 23, 2020
# app/__init__.py

def create_flask_app():

    # Load Default Configuration
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_pyfile('../config/env.py')

    # Index Mapping
    @app.route("/", methods=["GET"])
    def home():
        return 'Hello World'

    return app