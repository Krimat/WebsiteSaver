from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='name_constraint'),
        ]

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    added = models.DateField(auto_now=True)
    url = models.CharField(max_length=512)
    tags = models.ManyToManyField(Tag, related_name='sites')


    