import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        # Information object all of resolver 
        # print(info)
        # print(info.context)
        # print(info.context.user)
        return "Hello"

class Mutation():
    pass


schema = graphene.Schema(query=Query)