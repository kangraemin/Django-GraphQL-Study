import graphene
from graphene_django import DjangoObjectType
from .models import Room

class RoomType(DjangoObjectType):
    
    # Dynamic fields
    # https://docs.graphene-python.org/en/latest/types/objecttypes/#resolver-parameters
    is_fav = graphene.Boolean()

    class Meta:
        model = Room

    # 공식문서에 따르면, 필드와 resolver를 같이 추가 해줘야한다. 
    def resolve_is_fav(parent, info):
        # parent -> 7375 Carolyn Crossing (room)
        # info -> <graphql.execution.base.ResolveInfo object at 0x10c701c40>
        # print(parent, info) 
        user = info.context.user
        if user.is_authenticated:
            return parent in user.favs.all()
        return False

class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()