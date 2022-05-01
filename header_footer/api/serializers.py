from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from header_footer.models import Menu, Logo, Footer, SocialMedia


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','name','parent')

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'
        depth = 1


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
