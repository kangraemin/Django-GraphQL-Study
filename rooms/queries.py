import graphene
from .models import Room
from .types import RoomListResponse

def resolve_rooms(root, info, page=1):
    # middleware로 부터 주어진 user를 받아 올 수 있다. 
    print(info.context.user)
    # print(page)
    if page < 1:
        page = 1
    page_size = 5
    skipping = page_size * (page-1)
    taking = page_size * page
    rooms = Room.objects.all()[skipping:taking]
    total = Room.objects.count()
    return RoomListResponse(arr=rooms, total=total)


def resolve_room(root, info, id):
    # try:
    #     return Room.objects.get(id=id)
    # except Room.DoesNotExist:
    #     return None
    # Show DRF error  
    return Room.objects.get(id=id)