import graphene
from .types import PostType
from .models import Post, Comment
from graphene import Int


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=Int(required=True))

    def resolve_posts(self, info, **kwargs):
        return Post.objects.prefetch_related('comments__user')

    def resolve_post(self, info, id: int):
        # return Post.objects.filter(pk=id).prefetch_related("comments__user")
        return Post.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
