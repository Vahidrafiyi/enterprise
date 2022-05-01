from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from enterprise.permissions import IsSuperUser
from services.api.serializers import ServiceSerializer, ProjectSerializer
from services.models import Service, Project


# -----------------------------------------------------------USER---------------------------------------------------------------#
class ServiceAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        query = Service.objects.all()
        serializer = ServiceSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class ProjectAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        query = Project.objects.all()
        serializer = ProjectSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


# -----------------------------------------------------------ADMIN---------------------------------------------------------------#

class AdminServiceAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Service.objects.all()
        serializer = ServiceSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Service.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminProjectAPI(APIView):
    permission_classes = (IsSuperUser, IsAdminUser)

    def get(self, request):
        query = Project.objects.all()
        serializer = ProjectSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Project.objects.get(pk=pk)
        query.delete()
        return Response(status=204)
