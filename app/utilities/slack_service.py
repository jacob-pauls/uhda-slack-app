from config import get_env
from slack_sdk.web import WebClient
from slackeventsapi import SlackEventAdapter
from app.utilities.slack_blocks import SlackBlockTypes

# Jacob Pauls
# Nov 21, 2020
# slack_service.py

class SlackService:

    def __init__(self):
        self.slack_bot_token = get_env('SLACK_BOT_TOKEN')
        self.slack_signing_secret = get_env('SLACK_SIGNING_SECRET')
        self.slack_web = WebClient(token=self.slack_bot_token)

    def start_event_service(self, flask_app):
        slack_event = SlackEventAdapter(self.slack_signing_secret, "/slack/events", flask_app)

        # TODO: Clean up this event, either make use of it or add the 'team_join' event
        @slack_event.on("message")
        def message_alert(payload):
            event = payload.get("event", {})

            # Retrieve message data from API
            channel_id = event.get("channel")
            user_id = event.get("user")
            text = event.get("text")

            print("The slack event adapter triggered a message!")
            print("channel: " + channel_id)
            print("user: " + user_id)
            print("text: " + text)        

    def send_message(self, ticket_data):
        block_types = SlackBlockTypes()
        
        method = ticket_data["method"]

        if method == "CREATE_TICKET":
            blocks = block_types.create_ticket_block(ticket_data)
            message = ticket_data["username"] + " Created a Ticket :spiral_note_pad:"           
        elif method == "ASSIGN_TICKET":
            blocks = block_types.assigned_ticket_block(ticket_data)
            message = ":heavy_check_mark: \t" + ticket_data["username"] + " has been assigned to your ticket!"
        elif method == "PICKUP_TICKET":
            blocks = block_types.pickup_ticket_block(ticket_data)
            message = "Ticket picked up by " + ticket_data["username"]
        else:
            blocks = block_types.default_ticket_block()
            message = " :four: :zero: :four: "   

        return self.slack_web.chat_postMessage(
            channel=ticket_data["channel"],
            text=message,
            blocks=blocks
        )   