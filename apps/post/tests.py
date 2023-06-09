from graphene_django.utils import GraphQLTestCase

from apps.core.schema import schema


# Create your tests here.
class PostModelTestCase(GraphQLTestCase):
    GRAPHENE_SCHEMA = schema
    # GRAPHQL_URL = "/graphql/"

    def test_all_post_woth_comments_and_users(self):
        response = self.query(
            '''
                query posts{
                  posts{
                    id
                    title
                    content
                    comments{
                      id
                      content
                      isActive
                      user{
                        id
                        username
                      }
                    }
                  }
                }
            '''
        )
        print(response)
        self.assertResponseNoErrors(response)
        # self.assertResponseHasErrors(response)
