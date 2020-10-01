import graphene
from rooms.models import Room

from graphene_django import DjangoObjectType


class RoomType(DjangoObjectType):
    class Meta:
        model = Room

# class RoomType(graphene.ObjectType):
#     name = graphene.String()
#     address = graphene.String()
#     price = graphene.Int()
#     beds = graphene.Int()

class Query(graphene.ObjectType):
    hello = graphene.String()
    # Field => Use for complex type (not String, boolean ... etc)
    # rooms = graphene.Field(type=RoomType)
    rooms = graphene.List(RoomType)

    def resolve_hello(self, info):
        # Information object all of resolver 
        # print(info)
        # print(info.context)
        # print(info.context.user)
        return "Hello"

    def resolve_rooms(self, info):
        return Room.objects.all()

class Mutation():
    pass


schema = graphene.Schema(query=Query)