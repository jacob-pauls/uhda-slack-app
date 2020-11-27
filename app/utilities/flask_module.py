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
@app.route("/sendMessageToSlackUser", methods=["POST"])
def sendMessageToSlackUser():
    # Retrieve the POST data
    channel = request.args.get("user_id")
    username = request.args.get("username")
    description = request.args.get("description")
    title = request.args.get("title")
    priority = request.args.get("priority")
    category = request.args.get("category")

        
    # Send the message
    slack = SlackService()
    slack.send_create_ticket_message(channel, username, description, title, priority, category)
    return "<h1>UHDA Sent A Message in Slack to: " + channel + "</h1>"

@app.route("/sendMessageToEmployeeChannel", methods=["POST"])
def sendMessageToEmployeeChannel():
    return "<h1>UHDA Sent A Message in Slack to </h1>"