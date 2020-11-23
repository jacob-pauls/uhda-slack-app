from os import environ

# Jacob Pauls
# Nov 23, 2020
# config/__init__.py

def get_env(key):
    return environ.get(key)