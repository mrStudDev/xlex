from django.db import models


class Home_Site(models.Model):
    xlex_home = models.CharField(max_length=100)

    def __str__(self):
        return self.xlex_home