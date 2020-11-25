from config import get_env, init_port
from app.utilities.flask_module import initialize_flask_app
from app.utilities.slack_service import SlackService

# Jacob Pauls
# Nov 21, 2020
# uhda_main.py

# Initialize a Flask app
flask_app = initialize_flask_app()

# Start the Slack Service
SlackService().start_event_service(flask_app)

# Run the Flask app
if __name__ == '__main__':
    flask_app.run(port=3000)