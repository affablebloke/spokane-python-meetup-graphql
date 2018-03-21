import json

import arrow
import graphene
# http://docs.graphene-python.org/en/latest/types/scalars/
from graphene.types.datetime import DateTime
from elasticsearch import Elasticsearch
es = Elasticsearch(['es'])

class Player(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

    @staticmethod
    def from_redis_obj(key, obj):
        obj = json.loads(obj.decode('utf-8'))
        return Player(id=key, name=obj.get('name'))


class Team(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Game(graphene.ObjectType):
    id = graphene.ID()
    start_time = DateTime()


class Query(graphene.ObjectType):
    search_players = graphene.List(
        Player, query=graphene.String(required=True))

    def resolve_search_players(self, info, query):
        # TODO: implement method
        res = es.search(index="players", body={
            "query": {
                "query_string" : {
                    "default_field" : "name",
                    "query" : "*{0}*".format(query)
                }
            }
        })
        player_loader = info.context.get('player_loader')
        keys = [obj.get('_id') for  obj in res.get('hits').get('hits')]
        print(keys)
        return player_loader.load_many(keys)
