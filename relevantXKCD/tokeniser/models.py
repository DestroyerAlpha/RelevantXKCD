from django.db import models

# Create your models here.
class Input(models.Model):
    input_text = models.TextField()
    tokenised_text = models.JSONField()