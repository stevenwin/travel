from django.db import models

class UserInput(models.Model):
    astro_sun = models.CharField(max_length=30)
    astro_moon = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.astro_sun}, {self.astro_moon}, {self.country}'