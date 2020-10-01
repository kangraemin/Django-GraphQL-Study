import graphene
from .models import Room
from .types import RoomListResponse, RoomType

class Query(object):

    # rooms = graphene.List(RoomType, page=graphene.Int())
    rooms = graphene.Field(RoomListResponse, page=graphene.Int())
    # required = True -> 꼭 받아야 함 
    room = graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        # print(page)
        if page < 1:
            page = 1
        page_size = 5
        skipping = page_size * (page-1)
        taking = page_size * page
        rooms = Room.objects.all()[skipping:taking]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)


    def resolve_room(self, info, id):
        # try:
        #     return Room.objects.get(id=id)
        # except Room.DoesNotExist:
        #     return None
        # Show DRF error  
        return Room.objects.get(id=id)