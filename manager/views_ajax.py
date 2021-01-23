from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from manager.models import LikeCommentUser, Comment, Book
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from manager.permissions import IsAuthor
from manager.serializers import CommentSerializer, LikeCommentUserSerialize, BookSerialize


class CreateBook(ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerialize
    queryset = Book.objects.all()


class AddLikeComment(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikeCommentUserSerialize
    queryset = LikeCommentUser.objects.all()

    def get_object(self):
        user = self.request.user
        comment_id = self.kwargs['pk']
        query_set = LikeCommentUser.objects.filter(user=user, comment_id=comment_id)
        if query_set.exists():
            return query_set.first()

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            LikeCommentUser.objects.create(user=request.user, comment_id=self.kwargs['pk'])
        else:
            obj.delete()
        return Response({"likes": LikeCommentUser.objects.filter(comment_id=self.kwargs['pk']).count()})


class DeleteComment(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
