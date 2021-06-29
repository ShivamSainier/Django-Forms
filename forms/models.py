from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=300)
    no=models.IntegerField()
    covver_image=models.ImageField(upload_to='images',default="image.jpg")
    file=models.FileField(upload_to="files",default="file.jpg")
    

    def __str__(self):
        return self.name+' - '+self.author
