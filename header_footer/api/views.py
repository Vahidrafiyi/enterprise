from rest_framework.response import Response
from rest_framework.views import APIView

from header_footer.api.serializers import HeaderSerializer, FooterSerializer
from header_footer.models import Header, Footer


class HeaderAPI(APIView):
    def get(self, request):
        query = Header.objects.all()
        serializer = HeaderSerializer(query)
        return Response(serializer.data, status=200)


class FooterAPI(APIView):
    def get(self, request):
        query = Footer.objects.all()
        serializer = FooterSerializer(query)
        return Response(serializer.data, status=200)
