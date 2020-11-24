from os import environ

# Jacob Pauls
# Nov 23, 2020
# config/__init__.py

def get_env(key):
    return environ.get(key)

def init_port(port_number):
    return environ.get("PORT", port_number)