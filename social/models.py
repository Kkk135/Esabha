from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import  MinValueValidator,RegexValidator
import datetime

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    user=models.OneToOneField(User,related_name="User_name", on_delete=CASCADE)
    age=models.IntegerField(default=18, validators=[MinValueValidator(18)])
    address=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=10, default="single", choices=(("single","single"),("married","married")))
    gender=models.CharField(max_length=10, default="Female", choices=(("Male","Male"),("Female","Female")))
    Mobile_no=models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10,null=True,blank=True)
    Desciption=models.TextField(null=True,blank=True)
    pic =models.ImageField(upload_to ="image\\",null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    Title=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    Desciption=models.TextField(null=True,blank=True)
    pic =models.ImageField(upload_to ="image\\",null=True)
    creat_date=models.DateTimeField(auto_now_add=True)
    upload_by=models.ForeignKey(to=Profile ,related_name='post',blank=True, null=True,on_delete=CASCADE)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    post=models.ForeignKey(to=Post,related_name="User_post_by",blank=True, null=True,on_delete=CASCADE)
    msg=models.TextField()
    comment_by=models.ForeignKey(to=Profile,related_name="User_commented_by",blank=True, null=True ,on_delete=CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=10, default="Female", choices=(("racist","racist"),("abbusing","abbusing")))

    def __str__(self):
        return self.msg

class Like(models.Model):
    post=models.ForeignKey(to=Profile,related_name="User_post" ,on_delete=CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    like_by=models.ForeignKey(to=Profile ,related_name="User_like_by",on_delete=CASCADE)


    def __str__(self):
        return self.like_by

class FollowUser(models.Model):
    profile=models.ForeignKey(to=Profile,related_name="Profile_by" ,on_delete=CASCADE)
    followe_by=models.ForeignKey(to=Profile ,related_name="User_follow_by",on_delete=CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.followe_by
