import datetime

from django.db.models import Sum
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from enterprise.permissions import IsSuperUser
from header_footer.api.serializers import MenuSerializer, LogoSerializer, FooterSerializer, SocialMediaSerializer
from header_footer.models import Logo, Footer, SocialMedia, Menu
# ---------------------------------------USER--------------------------------------------------------------------------------- #
from header_footer.proccessor import save_visitor_info


class LogoAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Logo.objects.get()
        serializer = LogoSerializer(query, many=True)
        return Response(serializer.data, status=200)


class MenuAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Menu.objects.filter(parent__isnull=True)
        serializer = MenuSerializer(query, many=True)
        return Response(serializer.data, status=200)


class FooterAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Footer.objects.all()
        serializer = FooterSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class OnlineUsers(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        traffic = save_visitor_info(request)

        return Response({'traffic':traffic}, status=200)


class SiteVisitAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        date = datetime.date.today()
        today = Visit.objects.filter(date__day=date.day)[0].number
        week = Visit.objects.filter(date__week=date.isocalendar()[1])
        month = Visit.objects.filter(date__month=date.month)[0].number
        year = Visit.objects.filter(date__year=date.year).aggregate(sum=Sum('number'))
        data = {'today': today, 'week': week, 'month': month, 'year': year}
        return Response(data, status=200)


# ---------------------------------------ADMIN--------------------------------------------------------------------------------- #
class AdminMenuAPI(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        query = Menu.objects.all()
        serializer = MenuSerializer(query, many=True)
        visit()
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Menu.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminLogoAPI(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        query = Logo.objects.get()
        serializer = LogoSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        query = Logo.objects.count()
        if query >= 1:
            return Response({'error': 'can not add another logo because there is one!'})
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        query = Logo.objects.get()
        serializer = LogoSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        query = Logo.objects.get()
        query.delete()
        return Response(status=204)


class AdminFooterAPI(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        query = Footer.objects.all()
        serializer = FooterSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        query = Footer.objects.count()
        if query >= 1:
            return Response({'error': 'you can not add footer because there is another one, just can edit it'})
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        query = Footer.objects.get()
        serializer = FooterSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        query = Footer.objects.get()
        query.delete()
        return Response(status=204)


class AdminSocialMediaAPI(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        query = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = SocialMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = SocialMedia.objects.get(pk=pk)
        serializer = SocialMediaSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = SocialMedia.objects.get(pk=pk)
        query.delete()
        return Response(status=204)
