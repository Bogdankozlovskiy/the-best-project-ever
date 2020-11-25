from django.urls import path
from manager.views import hello

# hello/34/
# hello/bogdan/
urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
]
