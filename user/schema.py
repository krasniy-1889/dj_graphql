import graphene
from django.contrib.auth.models import User

from .types import UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
