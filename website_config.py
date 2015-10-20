import json

SECRET_KEY = 'tMsCUhLizue4cIfAe8s6vkbOWGBB9wUF99N5J0Whbtlf8a6iKIC3R30Rdbo4y6B'
DEBUG = False
CLIENT_SECRETS = 'client_secrets.json'
CLIENT_ID = json.loads(open(CLIENT_SECRETS, 'r').read())['web']['client_id']

IMGUR_CLIENT_ID = '873ad6bb61b29ec'
