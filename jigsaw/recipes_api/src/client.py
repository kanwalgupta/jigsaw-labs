import requests

root_url = 'https://www.themealdb.com/api/json/v1/1/'

def recipe_url(meal:str) -> str:
    return f"{root_url}search.php?s={meal}"
#print(recipe_url('Arrabiata'))

def main_ingredient_url(ingredient:str) -> str:
    return f"{root_url}filter.php?i={ingredient}"
#print(main_ingredient_url("chicken_breast"))

def requests_by_recipe(meal:str) -> str:
    response = requests.get(recipe_url(meal))
    return response.json()
    #return response
#print(requests_by_recipe('Arrabiata'))

def request_by_main_ingredient(ingredient:str) -> str:
    response = requests.get(main_ingredient_url(ingredient))
    return response.json()
#print(request_by_main_ingredient("chicken_breast"))

def id_url(id:str) -> str:
    return f"{root_url}lookup.php?i={id}"
#print(id_url('52772'))