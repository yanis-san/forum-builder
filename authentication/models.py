from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from pythonbb.models import Forum



class User(AbstractUser):
    profile_picture = models.ImageField(verbose_name='Photo de profil')


class UserForum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Group, on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.user} - {self.forum} - {self.groupe}"

    class Meta:
        unique_together = ('user', 'forum')

    
