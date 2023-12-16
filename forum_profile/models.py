from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    photo = models.ImageField(upload_to='profile/photo/%Y/%m/%d')
    username = models.CharField(max_length=16)
    description = models.TextField()
    signature = models.TextField()
    profile_color = models.CharField(validators=[MinLengthValidator(8)], max_length=8)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username
