#from client import requests_by_recipe

#meal = 'Arrabiata'
meal = 'Chick-Fil-A Sandwich'
sample_meal = sample_meal = {'idMeal': '52772', 'strMeal': 'Teriyaki Chicken Casserole', 'strDrinkAlternate': None, 
'strCategory': 'Chicken', 'strArea': 'Japanese',
 'strInstructions': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wvpsxx1468256321.jpg', 'strTags': 'Meat,Casserole', 'strYoutube': 'https://www.youtube.com/watch?v=4aZr5hZXP_s',
  'strIngredient1': 'soy sauce', 'strIngredient2': 'water', 'strIngredient3': 'brown sugar', 'strIngredient4': 'ground ginger', 'strIngredient5': 'minced garlic', 'strIngredient6': 'cornstarch', 'strIngredient7': 'chicken breasts', 'strIngredient8': 'stir-fry vegetables', 'strIngredient9': 'brown rice', 'strIngredient10': '', 'strIngredient11': '', 'strIngredient12': '', 'strIngredient13': '', 'strIngredient14': '', 'strIngredient15': '', 'strIngredient16': None, 'strIngredient17': None, 'strIngredient18': None,
  'strIngredient19': None, 'strIngredient20': None, 'strMeasure1': '3/4 cup', 'strMeasure2': '1/2 cup', 'strMeasure3': '1/4 cup', 'strMeasure4': '1/2 teaspoon', 'strMeasure5': '1/2 teaspoon', 'strMeasure6': '4 Tablespoons', 'strMeasure7': '2', 'strMeasure8': '1 (12 oz.)', 'strMeasure9': '3 cups', 'strMeasure10': '', 'strMeasure11': '',
 'strMeasure12': '', 'strMeasure13': '', 'strMeasure14': '', 'strMeasure15': '', 'strMeasure16': None, 'strMeasure17': None, 'strMeasure18': None, 'strMeasure19': None, 'strMeasure20': None, 'strSource': None, 'strImageSource': None, 'strCreativeCommonsConfirmed': None, 'dateModified': None}
sample_meals = [{'strMeal': 'Brown Stew Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg', 'idMeal': '52940'}, {'strMeal': 'Chicken & mushroom Hotpot', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuuspp1511297945.jpg', 'idMeal': '52846'}, {'strMeal': 'Chicken Alfredo Primavera', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/syqypv1486981727.jpg', 'idMeal': '52796'}, {'strMeal': 'Chicken Basquaise', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wruvqv1511880994.jpg', 'idMeal': '52934'}, {'strMeal': 'Chicken Congee', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529446352.jpg', 'idMeal': '52956'}, {'strMeal': 'Chicken Handi', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wyxwsp1486979827.jpg', 'idMeal': '52795'}, {'strMeal': 'Kentucky Fried Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xqusqy1487348868.jpg', 'idMeal': '52813'}, {'strMeal': 'Kung Pao Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1525872624.jpg', 'idMeal': '52945'}, {'strMeal': 'Pad See Ew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuuspp1468263334.jpg', 'idMeal': '52774'}, {'strMeal': 'Piri-piri chicken and slaw', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/hglsbl1614346998.jpg', 'idMeal': '53039'}, {'strMeal': 'Thai Green Curry', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sstssx1487349585.jpg', 'idMeal': '52814'}]

strIngredients = ['strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 'strIngredient13', 'strIngredient14', 'strIngredient15', 'strIngredient16', 'strIngredient17', 'strIngredient18', 'strIngredient19', 'strIngredient20']
strMeasures = ['strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 'strMeasure15', 'strMeasure16', 'strMeasure17', 'strMeasure18', 'strMeasure19', 'strMeasure20']


def meal_recipe(meal:str) -> str:
    meal_data = requests_by_recipe(meal)
    #dict -> meals is first value -> we want first element in the list -> then we want dict['strInstructions']
    meal_list = meal_data["meals"]
    meal_dict = meal_list[0]
    recipe = meal_dict['strInstructions']
    return recipe  
#print(meal_recipe(meal))

def meal_names_and_ids(meals:list) -> list:
    names_and_ids = []
    for meal in meals:
        name_and_id = {}
        name_and_id['name'] = meal['strMeal']
        name_and_id['id'] = meal['idMeal']
        names_and_ids.append(name_and_id)
    return(names_and_ids)
#print(meal_names_and_ids(sample_meals))


def meal_names(meals:list) -> list:
    names_ids = meal_names_and_ids(sample_meals)
    names = []
    for names_id in names_ids:
        names.append(names_id['name'])
    return names
    #print(names)
def meal_ids(meals:list) -> list:
    names_ids = meal_names_and_ids(sample_meals)
    ids = []
    for names_id in names_ids:
        ids.append(names_id['id'])
    return ids
    #print(ids)

def meal_ingredients(meal:dict) -> list:
    ingredients = []
    for k,v in meal.items():
        if k in strIngredients and v is not None and v != "":
            ingredients.append(v)
    return ingredients
#print(meal_ingredients(sample_meal))

def ingredients_and_measurements(meal:dict) -> dict:
    #output is a dict where the key is the ingredient and the value is the associated measurement
    ingredients = meal_ingredients(meal)
    measurements = []
    for k,v in meal.items():
        if k in strMeasures and v is not None and v != "":
            measurements.append(v)
    matched = zip(ingredients, measurements)
    return dict(matched)
print(ingredients_and_measurements(sample_meal))

