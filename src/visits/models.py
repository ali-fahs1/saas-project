from django.db import models

class PageVisit(models.Model):
    path=models.TextField(blank=True,null=True)
    timestam=models.DateField(auto_now_add=True)