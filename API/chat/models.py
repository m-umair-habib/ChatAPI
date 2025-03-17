from django.db import models

# Create your models here.
class Chat(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.user}: {self.message[:20]}"
        return self.message
