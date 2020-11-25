from config import get_env
from slack_sdk.web import WebClient
from slackeventsapi import SlackEventAdapter

# Jacob Pauls
# Nov 23, 2020
# slack_helper.py

class SlackHelper:

    def __init__(self):
        self.slack_bot_token = get_env('SLACK_BOT_TOKEN')
        self.slack_signing_secret = get_env('SLACK_SIGNING_SECRET')

    def initialize_slack_events_adapter(self, flask_app):
        return SlackEventAdapter(self.slack_signing_secret, "/slack/events", flask_app)

    def initialize_slack_web_client(self):
        return WebClient(token=self.slack_bot_token)