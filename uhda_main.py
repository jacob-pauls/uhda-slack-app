from config import get_env, init_port
from app import initialize_flask_app
from app.slack_helper import SlackHelper
from app.slack_service import SlackService

# Jacob Pauls
# Nov 21, 2020
# uhda_main.py

# Initialize a Flask app
flask_app = initialize_flask_app()

# Instantiate SlackHelper
slack_helper = SlackHelper()

# Initialize Slack Events Adapter
slack_events_adapter = slack_helper.initialize_slack_events_adapter(flask_app)

# Initialize Slack Web Client
slack_web_client = slack_helper.initialize_slack_web_client()

# Start the Slack Service
SlackService(slack_events_adapter, slack_web_client).start_service()

# Run the Flask app
if __name__ == '__main__':
    flask_app.run(port=3000)