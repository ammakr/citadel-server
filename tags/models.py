from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="parent_category",
    )

    def __str__(self):
        return self.name
