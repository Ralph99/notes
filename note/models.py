from django.db import models

# Create your models here.

class Note(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body


# 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
