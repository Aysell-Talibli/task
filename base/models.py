from django.db import models

class InstagramModel(models.Model):
    username=models.CharField(max_length=100)
    following=models.IntegerField()
    follower=models.IntegerField()

    def __str__(self):
        return self.username