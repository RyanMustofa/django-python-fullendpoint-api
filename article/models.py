from django.db import models

def upload_path(instance, filename):
    return '/'.join(['images',str(instance.title), filename])

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
