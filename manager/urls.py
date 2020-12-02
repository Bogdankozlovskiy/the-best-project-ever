from django.urls import path
from manager.views import hello, MyPage


urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path("", MyPage.as_view(), name="the-main-page"),
]
