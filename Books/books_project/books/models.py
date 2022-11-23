
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Books(models.Model):
    
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    cover=models.ImageField(upload_to='covers/',blank=True)

    class Meta: # new
        permissions = [
        ("special_status", "Can read all books"),
            ]

    def __str__(self):
        return self.title

class Review(models.Model):
    book= models.ForeignKey(Books, on_delete=models.CASCADE,related_name='reviews')
    review=models.CharField(max_length=255)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.review