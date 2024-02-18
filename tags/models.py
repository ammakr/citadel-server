from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_tag_name(value):
    if ' ' in value:
        raise ValidationError(
            message="Tagname cannot contain space",
            params={'value':value}
        )
        

class Tags(models.Model):
    tag_name = models.CharField(max_length=50,validators=[validate_tag_name])

    def __str__(self) -> str:
        return self.tag_name