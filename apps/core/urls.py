from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    # path('/graphql', GraphQLView.as_view(graphiql=True)),
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
