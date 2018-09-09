from django.db import models

class sign_all(models.Model):
    sign_category = models.CharField(max_length=250)
    sign_id = models.CharField(max_length=4)
    sign_name = models.CharField(max_length=250)
    sign_url = models.CharField(max_length=250)

    def __str__(self):
            return self.sign_name
