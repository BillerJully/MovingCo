from django.db import models

# Create your models here.


class Clientsfeedback(models.Model):
    feedback_title = models.CharField(max_length=60)
    feedback_author = models.CharField(max_length=90)
    feedback_text = models.TextField(blank=True)
    feedback_photo = models.ImageField(upload_to='feedbackphoto/%Y/%m/%d/')
    feedback_mark = models.CharField(max_length=20)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.feedback_author

