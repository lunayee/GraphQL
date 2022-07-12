from dataclasses import field
import imp
from tokenize import String
import graphene
from graphene_django import DjangoObjectType
from .models import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        field = ("id","title","excerpt")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

shchema = graphene.Schema(query=Query)