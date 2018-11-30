from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    def blog_count(self):
        return self.blog_set.count()
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<Blog:%s>"% self.title
    class Meta:
        ordering = ['-created_time']
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog,on_delete=models.CASCADE)'''