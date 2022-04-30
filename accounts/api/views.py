from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import ProfileSerializer
from accounts.models import Profile


class CurrentUserProfileAPI(APIView):
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query)
        return Response(serializer.data, status=200)

    def patch(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)
