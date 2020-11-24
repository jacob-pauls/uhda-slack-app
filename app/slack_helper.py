from slack_bolt import App
from config import get_env

# Jacob Pauls
# Nov 23, 2020
# slack_helper.py

class SlackHelper:

    def __init__(self):
        self.slack_bot_token = get_env('SLACK_BOT_TOKEN')
        self.slack_signing_secret = get_env('SLACK_SIGNING_SECRET')