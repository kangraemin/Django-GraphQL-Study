# https://docs.graphene-python.org/en/latest/execution/middleware/
import jwt
from django.conf import settings
from users.models import User

# 직접 안만들고, django-graphql-jwt 라는 라이브러리가 이미 만들어 져 있다.
# 하지만 직접 만들어본다. 
class JWTMiddleware(object):
    def resolve(self, next, root, info, **args):
        request = info.context
        # print(request.META)
        # print(request.META.get("HTTP_AUTHORIZATION"))
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
                # print(decoded)
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)
                # print(user)
                # user를 info객체에 담으면 된다 info는 every query에 다 전달되니까 
                info.context.user = user
                # middleware에서는, 에러가 있던 없던 next를 반드시 리턴 해주어야 한다. 그렇지 않으면 null만 리턴시킴
            except Exception:
                pass
        return next(root, info, **args)