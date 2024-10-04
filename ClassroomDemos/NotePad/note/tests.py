from django.test import TestCase

# Create your tests here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()