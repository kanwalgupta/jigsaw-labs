from src.client import requests_by_recipe
from src.adapter import meal_names, meal_ids, meal, sample_meals, sample_meal, meal_ingredients, ingredients_and_measurements


def test_meal_names():
    names = meal_names(sample_meals)
    assert names == ['Brown Stew Chicken', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Handi', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Thai Green Curry']

def test_meal_ids():
    ids = meal_ids(sample_meals)
    assert ids == ['52940', '52846', '52796', '52934', '52956', '52795', '52813', '52945', '52774', '53039', '52814']

def test_meal_ingredients():
    ingredients = meal_ingredients(sample_meal)
    assert ingredients == ['soy sauce', 'water', 'brown sugar', 'ground ginger', 'minced garlic', 'cornstarch', 'chicken breasts', 'stir-fry vegetables', 'brown rice']

def test_ingredients_and_measurements():
    in_and_meas = ingredients_and_measurements(sample_meal)
    assert in_and_meas == {'soy sauce': '3/4 cup', 'water': '1/2 cup', 'brown sugar': '1/4 cup', 'ground ginger': '1/2 teaspoon', 'minced garlic': '1/2 teaspoon', 'cornstarch': '4 Tablespoons', 'chicken breasts': '2', 'stir-fry vegetables': '1 (12 oz.)', 'brown rice': '3 cups'}