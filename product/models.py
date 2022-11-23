from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100, default='Post Name')
    text = models.TextField()
    img = models.ImageField(upload_to='static/posts/', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


# id
# name
# text
# img
# date


# CharField, TextField, IntegerField, DateField, DateTimeField,
# EmailField, ImageField, FileField, ForeignKey, ManyToManeField
# auto_now
