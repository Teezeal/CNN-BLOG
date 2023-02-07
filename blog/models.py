from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=100)
    content= models.TextField()
    image= models.ImageField(default='news.jpg', upload_to='news_images')
    reporter= models.ForeignKey(User, on_delete=models.CASCADE)
    date_published= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug= models.SlugField(default='me')

    class Meta:
        verbose_name_plural = 'News'
    
    # get absolute url
    def get_absolute_url(self):
        return reverse('details', args=str(self.id))

    def __str__(self):
        return self.headline