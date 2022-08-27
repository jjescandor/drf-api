from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('dish_name', 'author', 'ingredients', 'instruction', 'created_at', 'updated_at')
        model = Recipe

