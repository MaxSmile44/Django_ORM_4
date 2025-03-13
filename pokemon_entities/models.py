from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon', null=True, blank=True)

    def __str__(self):
        return self.title