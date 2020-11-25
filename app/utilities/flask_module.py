from flask import Flask, request, make_response
from app.utilities.slack_service import SlackService

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

    @app.route("/sendMessageToSlackUser", methods=["POST"])
    def triggerMessage():
        # Retrieve the POST data
        user_id = request.args.get("id")

        # Format the message displayed to the user
        message = 'This message was sent from the Flask endpoint'
        
        # Send the message
        slack = SlackService()
        slack.send_slack_message(user_id, message)
        return '<h1>UHDA Sent A Message in Slack to: ' + user_id + "</h1>"

    return app