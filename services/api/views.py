from rest_framework.response import Response
from rest_framework.views import APIView

from services.api.serializers import ServiceSerializer, ProjectSerializer
from services.models import Service, Project


class ServiceAPI(APIView):
    def get(self, request):
        query = Service.objects.all()
        serializer = ServiceSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class ProjectAPI(APIView):
    def get(self, request):
        query = Project.objects.all()
        serializer = ProjectSerializer(query, many=True, context={'request':request})
        return Response(serializer.data, status=200)
