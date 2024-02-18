from django.db import models
from opinion.models import Opinion

# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    opinion = models.ForeignKey(Opinion,on_delete=models.CASCADE)