from os import environ as ENV

MONGODB_URL = ENV.get('MONGODB_URL')
MONGODB_USER = ENV.get('MONGODB_ATLAS_USER')
MONGODB_SECRET = ENV.get('MONGODB_ATLAS_SECRET')
