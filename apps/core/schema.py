import graphene
from apps.post.schema import (
    Query as PostQuery,
    Mutation as PostMutation
)
from apps.user.schema import (
    Query as UserQuery,
)


class Query(
    PostQuery,
    UserQuery,
):
    pass


class Mutation(
    PostMutation,
):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
