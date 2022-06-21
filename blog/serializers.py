from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields =["name"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = CommentModel
        fields = ["user", "contents"]

class ArticleSerializer(serializers.ModelSerializer):
    category =serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comments_set")
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]
    
    class Meta:
        model = ArticleModel
        fields = ["category", "title", "contents", "comments"]

