from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #imge = models.ImageField(upload_to="blog/",blank=True,null=True) #media/blog/파일이름
    image = models.ImageField(upload_to="blog/",blank=True,null=True)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
# Create your models here.
