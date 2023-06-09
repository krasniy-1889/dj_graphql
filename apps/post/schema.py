import graphene
from .types import PostType, CommentType
from .models import Post, Comment
from graphene import Int


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=Int(required=True))
    comments = graphene.List(
        CommentType,
        limit=Int(),
        offset=Int()
    )

    # Posts Resolver
    def resolve_posts(self, info, **kwargs):
        return Post.objects.prefetch_related('comments__user')

    def resolve_post(self, info, id: int):
        # return Post.objects.filter(pk=id).prefetch_related("comments__user")
        return Post.objects.get(pk=id)

    # Comments Resolvers
    def resolve_comments(self, info, limit: int = 10, offset: int = 0, **kwargs):
        return Comment.objects.all()[offset:limit]


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
