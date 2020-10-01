import graphene
from django.conf import settings
import jwt
from django.contrib.auth import authenticate
from .models import User

class CreateAccountMutation(graphene.Mutation):

    # Mutation 클래스의 인자를 받음
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    
    # Mutation 클래스의 Response 값
    ok = graphene.Boolean()
    error = graphene.Boolean()

    def mutate(self, info, email, password, first_name=None, last_name=None):
        try:
            User.objects.get(email=email)
            return CreateAccountMutation(ok=False, error="User already exist")
        except User.DoesNotExist:
            try:
                User.objects.create_user(email, email, password)
                return CreateAccountMutation(ok=True)
            except Exception:
                return CreateAccountMutation(ok=False, error="Can't create user")

    # def mutate(self, info, *args, **kwargs):
    #     email = kwargs.get~~~
    #     pass


# "email": "ryoung@yahoo.com",
# "username": "espinozakurt",
# "password": "Community air room agent quite. Require key age crime hand back speech."

class LoginMutation(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    pk = graphene.Int()
    error = graphene.String()

    def mutate(self, info, email, password):
        user = authenticate(username=email, password=password)
        if user:
            token = jwt.encode({'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256')
            # token은 문자열이 아니라, byte값이다 따라서 decode 해줘서 문자열로 만들어주는게 좋음
            return LoginMutation(token=token.decode('utf-8'), pk=user.pk)
        else:
            return LoginMutation(error="Wrong username/password")