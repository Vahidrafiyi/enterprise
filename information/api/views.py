from rest_framework.response import Response
from rest_framework.views import APIView

from information.api.serializers import SliderSerializer, ProductSerializer, CommentSerializer, PartnerSerializer, \
    NewsSerializer
from information.models import News, Slider, Partner, Product, Comment


class NewsAPI(APIView):
    def get(self, request):
        query = News.objects.all()
        serializer = NewsSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class SlidersAPI(APIView):
    def get(self, request):
        query = Slider.objects.all()
        serializer = SliderSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class PartnerAPI(APIView):
    def get(self, request):
        query = Partner.objects.all()
        serializer = PartnerSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class ProductAPI(APIView):
    def get(self, request):
        query = Product.objects.all()
        serializer = ProductSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class CommentAPI(APIView):
    def get(self, request):
        query = Comment.objects.all()
        serializer = CommentSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)
