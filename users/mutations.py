import graphene
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