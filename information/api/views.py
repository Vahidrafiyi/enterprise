from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from enterprise.permissions import IsSuperUser
from information.api.serializers import SliderSerializer, ProductSerializer, CommentSerializer, PartnerSerializer, \
    NewsSerializer
from information.models import News, Slider, Partner, Product, Comment


# -----------------------------------------------------------USER---------------------------------------------------------------#
class NewsAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        if len(pk) == 0:
            query = News.objects.all()
        else:
            query = News.objects.filter(pk=pk)
        serializer = NewsSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class SliderAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Slider.objects.all()
        serializer = SliderSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class PartnerAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Partner.objects.all()
        serializer = PartnerSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class ProductAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Product.objects.all()
        serializer = ProductSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class CommentAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Comment.objects.all()
        serializer = CommentSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


# -----------------------------------------------------------ADMIN---------------------------------------------------------------#

class AdminNewsAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = News.objects.all()
        serializer = NewsSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = News.objects.get(pk=pk)
        serializer = NewsSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = News.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminSliderAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Slider.objects.all()
        serializer = SliderSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Slider.objects.get(pk=pk)
        serializer = SliderSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Slider.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminPartnerAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Partner.objects.all()
        serializer = PartnerSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Partner.objects.get(pk=pk)
        serializer = PartnerSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Partner.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminProductAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Product.objects.all()
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Product.objects.get(pk=pk)
        serializer = ProductSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Product.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminCommentAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Comment.objects.all()
        serializer = CommentSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Comment.objects.get(pk=pk)
        query.delete()
        return Response(status=204)
