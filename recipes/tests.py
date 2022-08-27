from dis import Instruction
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Recipe

class RecipeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_recipe = Recipe.objects.create(dish_name='Toast', author=testuser1, ingredients='bread', instruction='toast')
        test_recipe.save()

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        actual_dish_name = str(recipe.dish_name)
        self.assertEqual(actual_dish_name,'Toast')

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        actual_ingredients = str(recipe.ingredients)
        self.assertEqual(actual_ingredients, 'bread')

    def test_recipe_instruction(self):
        recipe = Recipe.objects.get(id=1)
        actual_instruction = str(recipe.instruction)
        self.assertEqual(actual_instruction,'toast')
