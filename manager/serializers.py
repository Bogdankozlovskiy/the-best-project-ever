from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from manager.models import Comment, LikeCommentUser, Book


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeCommentUserSerialize(ModelSerializer):
    class Meta:
        model = LikeCommentUser
        fields = "__all__"


class BookSerialize(ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = ['title', "text", "date"]

