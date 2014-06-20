# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from micawber import bootstrap_basic

# Create app
app = Flask(__name__)

# MongoDB Config
app.config['MONGODB_DB'] = 'notes'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

# Create database connection object
db = MongoEngine(app)

oembed = bootstrap_basic()

if __name__ == '__main__':
    app.run()
