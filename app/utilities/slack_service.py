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

    def send_message(self, channel, username, description, title, priority, category, method):
        block_types = SlackBlockTypes()
        
        if method == "CREATE_TICKET":
            blocks = block_types.create_ticket_block(username, description, title, priority, category)
            message = username + " Created a Ticket :spiral_note_pad:"
        else:
            blocks = block_types.default_ticket_block()
            message = " :four: :zero: :four: "   

        return self.slack_web.chat_postMessage(
            channel=channel,
            text=message,
            blocks=blocks
        )   