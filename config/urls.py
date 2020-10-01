from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# https://docs.graphene-python.org/projects/django/en/latest/installation/
from graphene_django.views import GraphQLView
from config.schema import schema

# https://docs.graphene-python.org/projects/django/en/latest/installation/#csrf-exempt
# 다른 도메인에서 post 요청을 막는 django의 보호정책을 사용하지 않겠다고 선언
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
