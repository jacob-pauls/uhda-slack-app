from os import path, environ
from dotenv import load_dotenv

# Jacob Pauls
# Nov 23, 2020
# config/__init__.py

# Configure environment for local development
env_path = path.join(path.dirname(__file__), path.pardir, '.env')
load_dotenv(env_path, override=True)

def get_env(key):
    return environ.get(key)

def init_port(port_number):
    return environ.get("PORT", port_number)