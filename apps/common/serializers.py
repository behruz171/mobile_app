from rest_framework import serializers
from .models import *

# class CreateContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Content
#         fields = ["title", "description", "release_date", "duration", "rating", "category", "poster"]


# class CreateCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["name"]



# class EpisodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Episode
#         fields = ['movie', 'description']

# class ContentSerializer(serializers.ModelSerializer):
#     episodes = EpisodeSerializer(many=True, read_only=True)
#     category = serializers.CharField(source="category.name")

#     class Meta:
#         model = Content
#         fields = ['title', 'description', 'release_date', 'duration', 'rating', 'category', 'poster', 'episodes']


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "name"]


# class QuestionsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Questions
#         fields = ["id", "question", "answer"]



class QismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qism
        fields = ['qism_number', 'movie']

class EpisodeSerializer(serializers.ModelSerializer):
    qismlar = QismSerializer(many=True, read_only=True)

    class Meta:
        model = Episode
        fields = ['episode_number', 'title', 'description', 'release_date', 'qismlar']

class ContentSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ['title', 'description', 'poster', 'release_date', 'categories', 'duration', 'content_type', 'episodes']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ContentHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'description', 'poster', 'release_date', 'categories', 'duration', 'content_type',]

class HomePageSerializer(serializers.ModelSerializer):
    content = ContentHomeSerializer(many=True, read_only=True,source='content_set')
    class Meta:
        model = Category
        fields = ['name', 'description', 'content']