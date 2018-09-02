from django.db import models


class Test_t(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)


class Sign(models.Model):
    sign_category = models.CharField(max_length=250)
    sign_id = models.CharField(max_length=4)
    sign_name = models.CharField(max_length=250)
    sign_url = models.CharField(max_length=250)
