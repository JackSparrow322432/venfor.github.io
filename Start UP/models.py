from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username