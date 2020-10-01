from .models import User


def resolve_user(root, info, id):
        # password 같은건 숨기는게 좋다. 따라서 UserType 수정하라 
        return User.objects.get(id=id)


# 파일을 분리 했으니 resolve 안붙여도 동작 한다. 
def me(root, info):
        user = info.context.user
        if user.is_authenticated:
                return user
        else:
                raise Exception("You need to be logged in")