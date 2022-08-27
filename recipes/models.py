from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

class Recipe(models.Model):
    dish_name = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ingredients = models.TextField(default=" ")
    instruction = models.TextField(default=" ")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)