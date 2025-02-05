from django.db import models
from django.contrib.auth.models import User
from Account import models as account_model

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(account_model.Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    @property
    def like_count(self):
        return self.likes.count()
    
class Like(models.Model):
    user = models.ForeignKey(account_model.Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


class Comment(models.Model):
    user = models.ForeignKey(account_model.Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


