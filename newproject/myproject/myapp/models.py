from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Creater(models.Model):
    created_by = models.CharField(max_length=15)
    def __str__(self):
        return self.created_by


class Client(models.Model):
    created_by  = models.ForeignKey(Creater, on_delete=models.CASCADE)
    client_name  = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=now,blank=True)
class Project(models.Model):
    client  = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name   = models.CharField(max_length=15)

class User(models.Model):
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_name   = models.CharField(max_length=15)



