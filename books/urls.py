from django.urls import path
from graphene_django.views import GraphQLView
import graphql
from books.schema import shchema

urlpatterns = [
    path("graphql",GraphQLView.as_view(graphiql=True,schema=shchema)),
]
