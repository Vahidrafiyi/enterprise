from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import ProfileSerializer
from accounts.models import Profile
from enterprise.permissions import IsSuperUser


# ---------------------------------------USER--------------------------------------------------------------------------------- #


class CurrentUserProfileAPI(APIView):
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def patch(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)


# ---------------------------------------ADMIN--------------------------------------------------------------------------------- #
class AdminProfileAPI(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        query = Profile.objects.all()
        serializer = ProfileSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Profile.objects.get(pk=pk)
        query.delete()
        return Response(status=204)
