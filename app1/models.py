from django.db import models
from django.utils.text import slugify

class Movies(models.Model):
    name=models.CharField(max_length=10,unique=True)
    slug = models.SlugField(max_length=10, unique=True,null=True)
    desc=models.TextField(max_length=200,blank=True)
    image=models.ImageField(upload_to='project1/image',null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
