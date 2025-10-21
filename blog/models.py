from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content= models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'