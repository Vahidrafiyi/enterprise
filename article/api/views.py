from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from article.api.serializers import ArticleSerializer, ArticleGroupSerializer
from article.models import Article, ArticleGroup
from enterprise.permissions import IsSuperUser


# ---------------------------------------USER--------------------------------------------------------------------------------- #
class ArticleAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        if len(pk) == 0:
            query = Article.objects.all()
        else:
            query = Article.objects.filter(pk=pk)
        print(query)
        serializer = ArticleSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesGroupAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        if len(pk) == 0:
            query = ArticleGroup.objects.all()
        else:
            query = ArticleGroup.objects.filter(pk=pk)
        serializer = ArticleGroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


# ---------------------------------------ADMIN--------------------------------------------------------------------------------- #
class AdminArticleAPI(APIView):
    permission_classes = (IsAdminUser, IsSuperUser)

    def get(self, request):
        query = Article.objects.filter(author=request.user.id)
        serializer = ArticleSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['author'] = request.user.id
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Article.objects.get(pk=pk, author=request.user.id)
        serializer = ArticleSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Article.objects.get(pk=pk, author=request.user.id)
        query.delete()
        return Response(status=204)


class AdminGroupAPI(APIView):
    permission_classes = (IsAdminUser, IsSuperUser)

    def get(self, request):
        query = ArticleGroup.objects.all()
        serializer = ArticleGroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleGroupSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = ArticleGroup.objects.get(pk=pk)
        serializer = ArticleGroupSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = ArticleGroup.objects.get(pk=pk)
        query.delete()
        return Response(status=204)
