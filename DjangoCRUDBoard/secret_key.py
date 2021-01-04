import os

SECRET_KEY = os.environ['Django_secret_key'] if 'Django_secret_key' in os.environ else os.environ['Django_secret_key'.upper()]