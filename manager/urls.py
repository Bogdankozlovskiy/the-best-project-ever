from django.urls import path
from manager.oath_views import brazzers_view, brazzers_callback
from manager.views import MyPage, AddLike2Comment, AddRate2Book, BookDetail, AddBook
from manager.views import LoginView, logout_user, book_delete, UpdateBook, RegisterView
from manager.views_ajax import AddLikeComment, DeleteComment, CreateBook, CreateToken

urlpatterns = [
    path("add_like_to_comment/<int:id>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
path("add_like_to_comment/<int:id>/<int:location>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
    path("add_rate_to_book/<str:slug>/<int:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(), name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("add_book/", AddBook.as_view(), name="add-book"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", logout_user, name="logout"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("update_book/<str:slug>/", UpdateBook.as_view(), name='update-book'),
    path("brazzers/", brazzers_view, name="brazzers"),
    path("brazzers/github/", brazzers_callback, name="brazzers_callback"),
    path("add_like2comment_ajax/<int:pk>", AddLikeComment.as_view()),
    path("delete_comment_ajax/<int:pk>", DeleteComment.as_view()),
    path("create_book_ajax/", CreateBook.as_view()),
    path("create_token/", CreateToken.as_view(), name="create-token"),
    path("", MyPage.as_view(), name="the-main-page"),
]
