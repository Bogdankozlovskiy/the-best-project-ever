from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(
        max_length=50,
        verbose_name="название",
        help_text="ну это типо погоняло книги"
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    authors = models.ManyToManyField(User, related_name="books")

    def __str__(self):
        return f"{self.title}-{self.id}"


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

