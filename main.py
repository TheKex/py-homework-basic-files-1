from pprint import pprint

def parse_recipe_file(path):
    recipes = dict()  #recipt
    with open(path, "rt", encoding="utf-8") as recipes_file:
        for line in recipes_file:
            recipe_name = line.strip()
            ingredients_count = int(recipes_file.readline())
            ingredients = []
            for _ in range(ingredients_count):
                ingredients_line = recipes_file.readline()
                name, quantity, measure = [elem.strip() for elem in ingredients_line.split(' | ')]
                ingredient = {
                    'name': name,
                    'quantity': int(quantity),
                    'measure': measure
                }
                ingredients.append(ingredient)
            recipes_file.readline()
            recipes[recipe_name] = ingredients
    return recipes


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['name'] in ingredients:
                ingredients[ingredient['name']]['quantity'] += person_count * ingredient['quantity']
            else:
                ingredients[ingredient['name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return ingredients


if __name__ == '__main__':
    cook_book = parse_recipe_file("src/recipes.txt")
    pprint(cook_book)
    shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
    pprint(shop_list)


