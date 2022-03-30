from flask import current_app, g
from pymongo import MongoClient

def connect():
    if 'mongodb' not in g:
        g.mongodb = MongoClient(
            current_app.config['MONGODB_URL'],
            username=current_app.config['MONGODB_USER'],
            password=current_app.config['MONGODB_SECRET']
        )

    return g.mongodb

def disconnect(e=None):
    print('disconnecting...')
    mongodb = g.pop('mongodb', None)

    print('mongodb:', mongodb)
    if mongodb is not None:
        mongodb.close()

def add_app_hooks(app):
    app.teardown_appcontext(disconnect)
