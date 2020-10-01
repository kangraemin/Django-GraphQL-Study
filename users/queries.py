from .models import User


def resolve_user(self, info, id):
        # password 같은건 숨기는게 좋다. 따라서 UserType 수정하라 
        return User.objects.get(id=id)

    