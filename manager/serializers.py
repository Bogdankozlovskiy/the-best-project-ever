from django.contrib.auth.models import User
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


class UserSerialize(ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", "comment_set"]


class BookSerialize(ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    authors = UserSerialize(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', "text", "date", "authors"]

    def save(self, author):
        book = super().save()
        book.authors.add(author)
        book.save()

