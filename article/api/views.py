from rest_framework.response import Response
from rest_framework.views import APIView

from article.api.serializers import ArticleSerializer, ArticleGroupSerializer
from article.models import Article, ArticleGroup


class ArticleAPI(APIView):
    def get(self, request, pk):
        if len(pk) == 0:
            query = Article.objects.all()
        else:
            query = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(query)
        return Response(serializer.data, status=200)


class ArticlesGroupAPI(APIView):
    def get(self, request, pk):
        if len(pk) == 0:
            query = ArticleGroup.objects.all()
        else:
            query = ArticleGroup.objects.get(pk=pk)
        serializer = ArticleGroupSerializer(query)
        return Response(serializer.data, status=200)
