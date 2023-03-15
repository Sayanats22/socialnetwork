from pydoc import classname
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Posts(models.Model):
    image=models.ImageField(upload_to="images",null=True)
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    likes=models.ManyToManyField(User,related_name="likes")


    @property
    def fetch_comments(self):
        comments=self.comments_set.all()
        return comments

    def __str__(self):
        return self.post


class Comments(models.Model):
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create_date=models.DateField(auto_now_add=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    cmt_likes=models.ManyToManyField(User,related_name="upvotes")
    # up_vote=models.ManyToManyField()

    def __str__(self):
        return self.comment

        
