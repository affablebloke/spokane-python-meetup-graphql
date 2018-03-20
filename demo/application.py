import logging
import os

import graphene
from flask import request, Flask
from flask_graphql import GraphQLView
from graphql.execution.executors.gevent import GeventExecutor
from schema import Query
from loaders import PlayerLoader

FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
APPLICATION_PORT = os.environ.get('FLASK_PORT', 8080)

# Create the Flask app
application = Flask(__name__)

# Load config values specified above
application.config.from_object(__name__)
# Only enable Flask debugging if an env var is set to true
application.debug = FLASK_DEBUG in ['true', 'True', '1']

schema = graphene.Schema(query=Query)
# https://github.com/graphql-python/flask-graphql
application.add_url_rule(
    '/',
    view_func=GraphQLView.as_view(
        'graphql', schema=schema, graphiql=True, context={'player_loader': PlayerLoader()}, executor=GeventExecutor()))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=APPLICATION_PORT)
