from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"