from config import get_env

# Jacob Pauls
# Nov 23, 2020
# config/env.py

# Default configuration class
class EnvConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SLACK_SIGNING_SECRET = get_env('SLACK_SIGNING_SECRET')