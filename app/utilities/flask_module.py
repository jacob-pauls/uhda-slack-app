import urllib
from flask import Flask, request, make_response
from app.utilities.slack_service import SlackService

# Jacob Pauls
# Nov 24, 2020
# flask_module.py

# Load Default Configuration
app = Flask(__name__)

# Index Mapping
@app.route("/", methods=["GET"])
def home():
    return 'UHDA SlackApp is running!'

# TODO: Placeholder method, consider removing
@app.route("/buildTicketNotification", methods=["POST"])
def buildTicketNotification():
    # Retrieve the POST data
    ticket_data = {
        "channel": decode_url_param(request.args.get("channel")),
        "username": decode_url_param(request.args.get("username")),
        "description": decode_url_param(request.args.get("description")),
        "title": decode_url_param(request.args.get("title")),
        "priority": decode_url_param(request.args.get("priority")),
        "category": decode_url_param(request.args.get("category")),
        "method": decode_url_param(request.args.get("method"))
    }

    # Send the message
    slack = SlackService()
    slack.send_message(ticket_data)
    return "<h1>UHDA Sent A Message in Slack to: " + ticket_data["channel"] + "</h1>"

def decode_url_param(param):
    decoded_param = urllib.parse.unquote(param)
    return decoded_param