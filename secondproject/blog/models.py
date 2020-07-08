from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #imge = models.ImageField(upload_to="blog/",blank=True,null=True) #media/blog/파일이름
    image = models.ImageField(upload_to="blog/",blank=True,null=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likers")
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name= 'comments')
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True, blank = True, related_name = "comments")
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auther}님이 {self.blog}에 단 댓글"
# Create your models here.
