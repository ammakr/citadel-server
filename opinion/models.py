from django.db import models
from django.conf import settings
from tags.models import Tags


class Opinion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.user.username}"

    class Meta:
        ordering = ["title"]
