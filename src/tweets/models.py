from django.db import models
from django.conf import settings
from .validators import validate_content
from django.core.exceptions import ValidationError

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    # def clean_content(self):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("cannot be abc")
    #     return super(Tweet, self).clean()
