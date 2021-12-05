import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from model import News as NewsModel

class News(MongoengineObjectType):
    class Meta:
        model = NewsModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    Allnews = graphene.List(News)

    def resolve_Allnews(self, info):
        return list(NewsModel.objects.all())

schema = graphene.Schema(query=Query )