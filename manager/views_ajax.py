from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from manager.models import LikeCommentUser, Comment, Book
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from manager.permissions import IsAuthor
from manager.serializers import CommentSerializer, LikeCommentUserSerialize, BookSerialize
from django.contrib.auth.models import auth
from rest_framework.authtoken.models import Token


class CreateBook(ListCreateAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerialize
    queryset = Book.objects.all()
    search_fields = ['title', 'text']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    # ordering_fields = ["rate"]


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


class CreateToken(APIView):
    def post(self, request):
        login = request.data.get('login')
        pwd = request.data.get("pwd")
        user = auth.authenticate(request, username=login, password=pwd)
        if user is not None:
            token, flag = Token.objects.get_or_create(user=user)
            return Response({"token": token.__str__()}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)



