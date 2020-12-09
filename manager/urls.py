from django.urls import path
from manager.views import hello, MyPage, AddLike, AddLike2Comment, AddRate2Book, BookDetail


urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path("add_like/<int:id>/", AddLike.as_view(), name="add-like"),
    path("add_like_to_comment/<int:id>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
    path("add_rate_to_book/<int:id>/<str:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("book_view_detail/<int:id>/", BookDetail.as_view(), name="book-detail"),
    path("", MyPage.as_view(), name="the-main-page"),
]
