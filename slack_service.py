import os
from slack_bolt import App
from app.slack_helper import SlackHelper
from config import init_port, get_env

# Jacob Pauls
# Nov 21, 2020
# slack_service.py

slackhelper = SlackHelper()

# SlackApp Launcher
app = App (
    token=slackhelper.slack_bot_token,
    signing_secret=slackhelper.slack_signing_secret
)

@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")

if __name__ == "__main__":
    app.start(port=int(init_port(3000)))