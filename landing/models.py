from django.db import models
from django.contrib.auth.models import User

class Mails(models.Model):
    mail = models.fields.EmailField(max_length=100)