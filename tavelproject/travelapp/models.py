from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class details(models.Model):
    det=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    click=models.CharField(max_length=50)
    def __str__(self):
        return self.det



