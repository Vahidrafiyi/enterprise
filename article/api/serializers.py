from rest_framework import serializers

from article.models import Article, ArticleGroup


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleGroup
        fields = '__all__'
