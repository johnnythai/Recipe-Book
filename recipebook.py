"""
Recipe Book

- create, search, display, edit recipes
- all recipes stored in database using sqlite3
- implement tkinter for a gui
- integrate into website
"""

import sqlite3 as my_db
import pprint

class Recipe:
    def __init__(self, name, servings, time, ingredients, equipment, procedure):
        self.name = name
        self.servings = servings
        self.time = time
        self.ingredients = ingredients
        self.equipment = equipment
        self.procedure = procedure

    def show_recipe(self):
        #able to print and display recipe as a list
        print(
        '-------------------------',
        '\n\nRecipe: ', self.name,
        '\n-------------------------',
        '\n\nServings:\n\n',
        self.servings,
        '\n\nTime (in minutes):\n\n',
        self.time,
        '\n\nIngredients:\n\n',
        self.ingredients,
        '\n\nEquipment:\n\n',
        self.equipment,
        '\n\nProcedure:\n\n',
        self.procedure,
        '\n---------------------------'
        )
        print("my_word {word} and another {key_word}".format(word="nice", key_word="test"))

    def __str__(self):
        return self.name

def close_program():
    import sys
    sys.exit(0)

def connect_db():
    """
    setup connection to db
    """
    conn = my_db.connect('recipebook.db')

    c = conn.cursor()

    """
    check if table exists, if it does not, create recipe table
    """
    c.execute('''
        SELECT count(name) FROM sqlite_master WHERE type='table' AND name='recipes'
        ''')

    if c.fetchone()[0] == 1:
        print('table exists')

    else:
        print('table does not exist')

        c.execute('''
            CREATE TABLE recipes
            (name text, servings int, time int, ingredients text, procedure text, equipment text)
            ''')

        print('table now created')

    main_screen()

def show_recipe(recipe):
    recipe_name = recipe.name
    c.execute('SELECT * FROM recipes WHERE name={recipe_name}').format(recipe_name=recipe_name)
    print(c.fetchone())

def insert_db(recipe):
    """
    variables obtained from create(), insert variables into db
    """ 
    # inserts = ['name', 'servings', 'time', 'ingredients', 'equipment', 'procedure']
    # values = [recipe.name, recipe.servings, recipe.time, recipe.equipment, recipe.procedure]
    dict_values = {
        'name': recipe.name, 
        'servings': recipe.servings,
        'time': recipe.time,
        'ingredients': recipe.ingredients,
        'equipment': recipe.equipment,
        'procedure': recipe.procedure
        }

    for key, value in dict_values.items():
        # dict_val = value
        # dict_key = key
        # c.execute('INSERT INTO (?) recipes VALUES(?)', (key, value))
        # # print(i,' inserted into value', dict_values[i])
        print("INSERT INTO RECIPES {key} VALUES {value}".format(key=key, value=value))
        c.execute("INSERT INTO RECIPES {key} VALUES {value}".format(key=key, value=value))

def edit():
    """
    called from search and create functions
    """
    pass

def create():
    """
    """
    name = input('\nName your recipe:\n')
    servings = input('\nHow many servings does this make?\n')
    time = input('\nAlloted time (in minutes):\n')

    ingredients = []
    print('\nWhat ingredients (in grams) are required? (type \'done\' to end)')
    while True:
        ingredients_input = input()
        if ingredients_input == 'done':
            break
        ingredients.append(str(ingredients_input))

    equipment = []
    print('\nWhat equipment is required? (type \'done\' to end)')
    while True:
        equipment_input = input()
        if equipment_input == 'done':
            break
        equipment.append(str(equipment_input))

    procedure = []
    print('\nWhat is the procedure? (type \'done\' to end)')
    while True:
        procedure_input = input()
        if procedure_input == 'done':
            break
        procedure.append(str(procedure_input))

    new_recipe = Recipe(name, servings, time, ingredients, procedure, equipment)
    insert_db(new_recipe)

def search():
    """
    use c.fetchone() to find recipe name in db that matches with user input
    """
    user_search = input('\nEnter recipe name:\n')

    c.execute('SELECT * FROM recipes WHERE name=?', (user_search,))
    print(c.fetchone())

def main_screen():
    print(
    '-----------------------\n',
    '     Recipe Book',
    '\n-----------------------\n'
    )

    x = input('search or create recipe? (\'exit\' to end program)\n')
    
    if x == 'search':
        search()
    
    elif x == 'create':
        create()
    
    elif x == 'exit':
        close_program()
    
    else:
        print('Not a valid entry.\n')
        main_screen()

if __name__ == '__main__':
    connect_db()