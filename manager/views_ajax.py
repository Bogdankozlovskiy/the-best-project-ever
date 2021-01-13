from django.http import HttpResponse, JsonResponse
from rest_framework import status
from manager.models import LikeCommentUser, Comment


def add_like2comment(request):
    if request.user.is_authenticated:
        comment_id = request.GET.get('comment_id')
        LikeCommentUser.objects.create(user=request.user, comment_id=comment_id)
        comment = Comment.objects.get(id=comment_id)
        count_likes = comment.users_like.count()
        return JsonResponse({"likes": count_likes}, status=status.HTTP_201_CREATED)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


def delete_comment(request):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=request.GET.get("comment_id"))
        if request.user == comment.author:
            comment.delete()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)
