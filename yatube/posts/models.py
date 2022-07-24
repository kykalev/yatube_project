from datetime import date
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title: str = models.CharField(max_length=200)
    slug: str = models.TextField()
    description: str = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text: str = models.TextField()
    pub_date: date = models.DateTimeField(auto_now_add=True)
    author: str = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group: str = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
