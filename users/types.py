import graphene
from .models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    rooms = graphene.List("rooms.schema.RoomType")

    class Meta:
        model = User
        exlude = ("password", "is_superUser", "last_login")