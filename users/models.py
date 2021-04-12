from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photos',default='default.jpg')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        im=Image.open(self.image.path)
        if im.height>300 or im.width>300:
            size=(300,300)
            im.thumbnail(size)
            im.save(self.image.path)
