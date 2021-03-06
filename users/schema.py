import graphene
from .types import UserType
from .models import User
from .queries import resolve_user, me
from .mutations import CreateAccountMutation, LoginMutation, ToggleFavsMutation, EditProfileMutation

# class Query(object):
    
#     user = graphene.Field(UserType, id=graphene.Int(required=True))

#     def resolve_user(self, info, id):
#         # password 같은건 숨기는게 좋다. 따라서 UserType 수정하라 
#         return User.objects.get(id=id)

class Query(object):

    user = graphene.Field(UserType, id=graphene.Int(required=True), resolver=resolve_user)
    me = graphene.Field(UserType, resolver=me)


class Mutation(object):

    create_account = CreateAccountMutation.Field()
    login = LoginMutation.Field()
    toggle_favs = ToggleFavsMutation.Field()
    edit_profile = EditProfileMutation.Field()