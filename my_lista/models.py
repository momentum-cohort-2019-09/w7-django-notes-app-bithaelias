from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    # description = models.TextField(
    #     help_text="Any instructions people need to use this checklist.",
    #     blank=True,
    #     null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
