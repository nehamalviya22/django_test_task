from django.db import models

class Information(models.Model):
    Choices = (
        ('Ad', 'Advertise'),
        ('IMP', 'Impression'),
    )
    
    username = models.CharField(max_length=100)
    sdk_version = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    media = models.CharField(max_length=65, choices=Choices)

    def __str__(self):
        return self.username

