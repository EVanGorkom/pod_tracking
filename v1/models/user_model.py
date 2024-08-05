from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, required=True)
    email = models.CharField(max_length=255, required=True)
    password = models.CharField(max_length=255, required=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username