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

    def post_notification(self, ticket_data):
        block_types = SlackBlockTypes()
        
        method = ticket_data["method"]

        # Cycle through possible notification methods
        # Send JSON payload respective to the notification method
        if method == "CREATE_TICKET":
            blocks = block_types.create_ticket_block(ticket_data)
            message = ticket_data["username"] + " Created a Ticket :spiral_note_pad:"           
        elif method == "PICKUP_TICKET":
            blocks = block_types.pickup_ticket_block(ticket_data)
            message = ":heavy_check_mark: Ticket picked up by " + ticket_data["username"]
        elif method == "ASSIGN_TICKET":
            blocks = block_types.assigned_ticket_block(ticket_data)
            message = ":heavy_check_mark: " + ticket_data["username"] + " has been assigned to your ticket!"
        elif method == "STATUS_UPDATE":
            blocks = block_types.field_update_block(ticket_data, "status")
            message = ":heavy_check_mark: Ticket status updated in the UHDA!" 
        elif method == "PRIORITY_UPDATE":
            blocks = block_types.field_update_block(ticket_data, "priority")
            message = ":heavy_check_mark: Ticket priority updated in the UHDA!"
        else:
            blocks = block_types.error_ticket_block()
            message = " :four: :zero: :four: "   

        return self.slack_web.chat_postMessage(
            channel=ticket_data["channel"],
            text=message,
            blocks=blocks
        )   