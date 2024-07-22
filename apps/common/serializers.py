from rest_framework import serializers
from .models import *

class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["title", "description", "release_date", "duration", "rating", "category", "poster"]


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]



class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['movie', 'description']

class ContentSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Content
        fields = ['title', 'description', 'release_date', 'duration', 'rating', 'category', 'poster', 'episodes']