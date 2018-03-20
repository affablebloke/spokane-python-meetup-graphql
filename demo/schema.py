import arrow
import graphene
# http://docs.graphene-python.org/en/latest/types/scalars/
from graphene.types.datetime import DateTime



class Player(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


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
        player_loader = info.context.get('player_loader')
        return player_loader.load_many(['abc'])
