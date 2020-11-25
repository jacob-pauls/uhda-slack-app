from app.slack_helper import SlackHelper
from slack_sdk.web import WebClient
from slackeventsapi import SlackEventAdapter

# Jacob Pauls
# Nov 21, 2020
# slack_service.py

class SlackService:

    def __init__(self, slack_events_adapter, slack_web_client):
        self.slack_event = slack_events_adapter
        self.slack_web = slack_web_client

    def start_service(self):
        slack_event = self.slack_event
        slack_web = self.slack_web

        @slack_event.on("message")
        def message_alert(payload):
            event = payload.get("event", {})

            channel_id = event.get("channel")
            user_id = event.get("user")
            text = event.get("text")

            print("The slack event adapter triggered a message! For the user: " + user_id + ", on the channel: " + channel_id + ", with the text: " + text)