from rest_framework import serializers
from article.models import Article

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id","title","body","image"]
        def save(self,*args,**kwargs):
            if self.instance.image:
                self.instance.image.delete()
            return super().save(*args,**kwargs)
