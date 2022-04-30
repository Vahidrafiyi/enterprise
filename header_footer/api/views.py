from rest_framework.response import Response
from rest_framework.views import APIView

from header_footer.api.serializers import HeaderSerializer, FooterSerializer, SocialMediaSerializer
from header_footer.models import Header, Footer


class HeaderAPI(APIView):
    def get(self, request):
        query = Header.objects.all()
        serializer = HeaderSerializer(query, many=True)
        return Response(serializer.data, status=200)


class FooterAPI(APIView):
    def get(self, request):
        query = Footer.objects.all()
        serializer = FooterSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class SocialMediaAPI(APIView):
    def post(self, request):
        serializer = SocialMediaSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=202)
