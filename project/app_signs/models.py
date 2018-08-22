from django.db import models


class Test_t(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
