import pandas as pd
import os

cwd = r'F:\projects\iti projects\Project-CSVs'
os.chdir(cwd)

# 1. Load Foods and original data
foods_df = pd.read_csv('Foods.csv')
valid_foods = set(foods_df['Name'].tolist())

# Read the original recipes and ingredients (powershell > output is utf-16)
orig_recipes_df = pd.read_csv('original_recipes.csv', encoding='utf-16')
orig_ing_df = pd.read_csv('original_ingredients.csv', encoding='utf-16')

# Filter out any original recipe that somehow has invalid ingredients
valid_orig_ings = orig_ing_df[orig_ing_df['FoodName'].isin(valid_foods)]
valid_orig_recipe_names = valid_orig_ings.groupby('RecipeName').filter(lambda x: 3 <= len(x) <= 12)['RecipeName'].unique()

orig_recipes_df = orig_recipes_df[orig_recipes_df['Name'].isin(valid_orig_recipe_names)]
orig_ing_df = valid_orig_ings[valid_orig_ings['RecipeName'].isin(valid_orig_recipe_names)]

# 2. Define highly authentic Egyptian recipes with STRICT ingredients from Foods.csv
new_recipes_data = [
    {
        "Name": "Koshari",
        "Description": "Egypt's national dish made of rice, macaroni, and lentils, topped with tomato sauce.",
        "Instructions": "Boil rice, macaroni, lentils, and chickpeas. Make a tomato sauce with garlic and cumin. Serve layered.",
        "Servings": 4,
        "PreparationTimeMinutes": 45,
        "Ingredients": [
            ("Rice Grains (Short)", 200, "g"),
            ("Macaroni", 200, "g"),
            ("Unpeeled Lentils", 150, "g"),
            ("Chickpeas", 100, "g"),
            ("Tomatoes", 300, "g"),
            ("Mature Onion Bulb", 150, "g"),
            ("Garlic Bulb", 20, "g"),
            ("Vegetable Oil", 3, "tbsp"),
            ("Cumin", 1, "tsp")
        ]
    },
    {
        "Name": "Molokhia",
        "Description": "A traditional Egyptian green soup made from finely chopped Jew's Mallow.",
        "Instructions": "Simmer the finely chopped leaves in chicken stock. Fry garlic and coriander in ghee (taqliya) and stir into the soup.",
        "Servings": 4,
        "PreparationTimeMinutes": 30,
        "Ingredients": [
            ("Jew's Mallow", 400, "g"),
            ("Chicken Stock", 500, "ml"),
            ("Garlic Bulb", 30, "g"),
            ("Coriander Seeds", 2, "tsp"),
            ("Butter Oil (Ghee)", 2, "tbsp")
        ]
    },
    {
        "Name": "Mahshi Waraq Enab",
        "Description": "Stuffed grape leaves rolled with a fragrant rice and herb mixture.",
        "Instructions": "Mix rice, tomatoes, herbs, and onions. Roll inside grape leaves and simmer until tender.",
        "Servings": 6,
        "PreparationTimeMinutes": 60,
        "Ingredients": [
            ("Grape Leaves", 300, "g"),
            ("Rice Grains (Short)", 250, "g"),
            ("Tomatoes", 200, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Parsley", 50, "g"),
            ("Dill", 50, "g"),
            ("Coriander Leaves", 50, "g"),
            ("Vegetable Oil", 2, "tbsp")
        ]
    },
    {
        "Name": "Ful Medames",
        "Description": "Slow-cooked fava beans, a staple Egyptian breakfast.",
        "Instructions": "Simmer broad beans slowly. Mash lightly with oil, cumin, salt, and lemon.",
        "Servings": 4,
        "PreparationTimeMinutes": 120,
        "Ingredients": [
            ("Broad Beans", 300, "g"),
            ("Vegetable Oil", 2, "tbsp"),
            ("Cumin", 1, "tsp"),
            ("Lemons", 1, "piece"),
            ("Table/Cooking Salt", 1, "tsp")
        ]
    },
    {
        "Name": "Taameya",
        "Description": "Egyptian falafel made from crushed fava beans and fresh herbs.",
        "Instructions": "Blend beans with herbs, onions, and garlic. Shape into patties and deep fry.",
        "Servings": 4,
        "PreparationTimeMinutes": 45,
        "Ingredients": [
            ("Decorticated Broad Beans", 250, "g"),
            ("Parsley", 50, "g"),
            ("Coriander Leaves", 50, "g"),
            ("Garlic Bulb", 20, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Vegetable Oil", 500, "ml")
        ]
    },
    {
        "Name": "Macarona Bechamel",
        "Description": "Baked macaroni layered with spiced minced meat and creamy bechamel sauce.",
        "Instructions": "Boil macaroni. Cook beef with onions. Make bechamel with flour, milk, and ghee. Layer and bake until golden.",
        "Servings": 8,
        "PreparationTimeMinutes": 60,
        "Ingredients": [
            ("Macaroni", 400, "g"),
            ("Beef Meat", 300, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Wheat Flour (White)", 100, "g"),
            ("Full Cream Milk", 500, "ml"),
            ("Butter Oil (Ghee)", 3, "tbsp")
        ]
    },
    {
        "Name": "Om Ali",
        "Description": "Traditional Egyptian bread pudding with nuts and cream.",
        "Instructions": "Layer pastry with nuts and raisins. Pour hot sweetened milk over it and top with cream. Bake until golden.",
        "Servings": 6,
        "PreparationTimeMinutes": 30,
        "Ingredients": [
            ("Flaky Pastry", 200, "g"),
            ("Full Cream Milk", 600, "ml"),
            ("Sugar (Sucrose)", 100, "g"),
            ("Whipping Cream", 150, "g"),
            ("Almonds", 50, "g"),
            ("Raisins", 50, "g"),
            ("Butter Oil (Ghee)", 1, "tbsp")
        ]
    },
    {
        "Name": "Moussaka Masreya",
        "Description": "Fried eggplant layered with spiced beef and tomato sauce.",
        "Instructions": "Fry eggplant slices. Cook minced beef with onions and tomatoes. Layer and bake.",
        "Servings": 6,
        "PreparationTimeMinutes": 50,
        "Ingredients": [
            ("Round Eggplant", 500, "g"),
            ("Beef Meat", 250, "g"),
            ("Tomatoes", 300, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Garlic Bulb", 20, "g"),
            ("Vegetable Oil", 4, "tbsp")
        ]
    },
    {
        "Name": "Roz Bel Laban",
        "Description": "Creamy Egyptian rice pudding.",
        "Instructions": "Simmer rice in full cream milk and sugar until tender and thickened. Top with nuts or cream.",
        "Servings": 4,
        "PreparationTimeMinutes": 45,
        "Ingredients": [
            ("Rice Grains (Short)", 100, "g"),
            ("Full Cream Milk", 800, "ml"),
            ("Sugar (Sucrose)", 100, "g"),
            ("Whipping Cream", 50, "g")
        ]
    },
    {
        "Name": "Sayadeya",
        "Description": "Coastal Egyptian fish with caramelized onion rice.",
        "Instructions": "Fry fish. Caramelize onions deeply, add water and cumin, then cook the rice in this dark broth.",
        "Servings": 4,
        "PreparationTimeMinutes": 60,
        "Ingredients": [
            ("Tilapia", 500, "g"),
            ("Rice Grains (Short)", 300, "g"),
            ("Mature Onion Bulb", 200, "g"),
            ("Tomatoes", 100, "g"),
            ("Cumin", 2, "tsp"),
            ("Vegetable Oil", 4, "tbsp")
        ]
    },
    {
        "Name": "Kofta Mashweya",
        "Description": "Grilled spiced minced beef skewers.",
        "Instructions": "Mix minced beef with grated onion, parsley, salt, and pepper. Shape onto skewers and grill.",
        "Servings": 4,
        "PreparationTimeMinutes": 30,
        "Ingredients": [
            ("Beef Meat", 500, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Parsley", 50, "g"),
            ("Black Pepper", 1, "tsp"),
            ("Table/Cooking Salt", 1, "tsp")
        ]
    },
    {
        "Name": "Fatteh Masreya",
        "Description": "A celebratory dish of crispy bread, rice, beef, and a garlicky tomato-vinegar sauce.",
        "Instructions": "Layer toasted bread and cooked rice. Top with boiled beef chunks and a sauce made of garlic, tomato, and vinegar.",
        "Servings": 6,
        "PreparationTimeMinutes": 90,
        "Ingredients": [
            ("Beef Meat", 500, "g"),
            ("Rice Grains (Short)", 300, "g"),
            ("Baladi Bread", 2, "piece"),
            ("Tomatoes", 300, "g"),
            ("Garlic Bulb", 30, "g"),
            ("Butter Oil (Ghee)", 2, "tbsp"),
            ("Table/Cooking Salt", 2, "tsp")
        ]
    },
    {
        "Name": "Shorbet Adss",
        "Description": "Warm and comforting Egyptian yellow lentil soup.",
        "Instructions": "Boil lentils with onions, carrots, and tomatoes. Blend until smooth. Add cumin and serve hot.",
        "Servings": 4,
        "PreparationTimeMinutes": 35,
        "Ingredients": [
            ("Peeled Lentils (Yellow)", 250, "g"),
            ("Tomatoes", 100, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Carrots", 100, "g"),
            ("Garlic Bulb", 20, "g"),
            ("Cumin", 1, "tsp")
        ]
    },
    {
        "Name": "Shakshouka Masreya",
        "Description": "Eggs cooked in a chunky tomato, onion, and pepper sauce.",
        "Instructions": "Sauté onions and peppers, add tomatoes. Crack eggs into the sauce and cook until set.",
        "Servings": 2,
        "PreparationTimeMinutes": 20,
        "Ingredients": [
            ("Whole Chicken Egg", 4, "piece"),
            ("Tomatoes", 200, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Green Peppers", 100, "g"),
            ("Vegetable Oil", 2, "tbsp")
        ]
    },
    {
        "Name": "Kabab Halla",
        "Description": "Tender beef cubes slow-cooked with melting onions.",
        "Instructions": "Brown beef cubes in ghee. Add sliced onions and spices, cook slowly until tender.",
        "Servings": 4,
        "PreparationTimeMinutes": 90,
        "Ingredients": [
            ("Beef Meat", 500, "g"),
            ("Mature Onion Bulb", 500, "g"),
            ("Butter Oil (Ghee)", 2, "tbsp"),
            ("Black Pepper", 1, "tsp")
        ]
    },
    {
        "Name": "Tagen Bamia Bel Lahma",
        "Description": "Okra and beef stew baked in a clay pot.",
        "Instructions": "Brown beef, add onions, garlic, and tomatoes. Add okra and bake in a tagen (clay pot) until tender.",
        "Servings": 5,
        "PreparationTimeMinutes": 75,
        "Ingredients": [
            ("Okra", 400, "g"),
            ("Beef Meat", 300, "g"),
            ("Tomatoes", 300, "g"),
            ("Mature Onion Bulb", 100, "g"),
            ("Garlic Bulb", 20, "g"),
            ("Coriander Seeds", 1, "tsp")
        ]
    },
    {
        "Name": "Salatat Baladi",
        "Description": "Classic Egyptian mixed salad.",
        "Instructions": "Chop tomatoes, cucumbers, onions, and parsley. Dress with lemon juice and salt.",
        "Servings": 4,
        "PreparationTimeMinutes": 10,
        "Ingredients": [
            ("Tomatoes", 200, "g"),
            ("Cucumber", 200, "g"),
            ("Mature Onion Bulb", 50, "g"),
            ("Parsley", 20, "g"),
            ("Lemons", 1, "piece")
        ]
    },
    {
        "Name": "Baid Bel Basterma",
        "Description": "Eggs scrambled with Egyptian cured beef pastrami.",
        "Instructions": "Sauté basterma in ghee, then add eggs and scramble until just set.",
        "Servings": 2,
        "PreparationTimeMinutes": 10,
        "Ingredients": [
            ("Whole Chicken Egg", 3, "piece"),
            ("Beef Basterma", 100, "g"),
            ("Butter Oil (Ghee)", 1, "tbsp")
        ]
    },
    {
        "Name": "Hawawshi",
        "Description": "Crispy baladi bread stuffed with spiced minced meat.",
        "Instructions": "Mix minced beef with onions, peppers, and spices. Stuff into baladi bread and bake until crispy.",
        "Servings": 4,
        "PreparationTimeMinutes": 40,
        "Ingredients": [
            ("Baladi Bread", 4, "piece"),
            ("Beef Meat", 400, "g"),
            ("Mature Onion Bulb", 150, "g"),
            ("Green Peppers", 100, "g"),
            ("Black Pepper", 1, "tsp")
        ]
    },
    {
        "Name": "Kebda Iskandarani",
        "Description": "Alexandrian-style stir-fried liver with garlic and peppers.",
        "Instructions": "Quickly stir-fry liver with garlic, cumin, and peppers. Serve hot with lemon.",
        "Servings": 3,
        "PreparationTimeMinutes": 15,
        "Ingredients": [
            ("Beef Liver", 300, "g"),
            ("Garlic Bulb", 30, "g"),
            ("Green Peppers", 100, "g"),
            ("Cumin", 1, "tsp"),
            ("Vegetable Oil", 2, "tbsp")
        ]
    }
]

# 3. Validate new recipes strictly against valid_foods before adding
final_recipes = orig_recipes_df.to_dict('records')
final_ingredients = orig_ing_df.to_dict('records')

for nr in new_recipes_data:
    # Check if name already exists in orig to avoid duplicates
    if nr["Name"] in orig_recipes_df['Name'].values:
        continue
    
    # Validate ingredients
    valid = True
    for ing in nr["Ingredients"]:
        if ing[0] not in valid_foods:
            valid = False
            break
    
    if valid:
        final_recipes.append({
            "Name": nr["Name"],
            "Description": nr["Description"],
            "Instructions": nr["Instructions"],
            "Servings": nr["Servings"],
            "PreparationTimeMinutes": nr["PreparationTimeMinutes"]
        })
        for ing in nr["Ingredients"]:
            final_ingredients.append({
                "RecipeName": nr["Name"],
                "FoodName": ing[0],
                "Quantity": ing[1],
                "Unit": ing[2]
            })

# Rebuild DataFrames
recipes_df = pd.DataFrame(final_recipes)
recipe_ing_df = pd.DataFrame(final_ingredients)

# 4. Generate RecipeAliases.csv for ALL recipes in recipes_df
arabic_names = {
    "Koshari": "كشري", "Molokhia": "ملوخية", "Mahshi Waraq Enab": "محشي ورق عنب",
    "Ful Medames": "فول مدمس", "Taameya": "طعمية", "Macarona Bechamel": "مكرونة بشاميل",
    "Om Ali": "أم علي", "Moussaka Masreya": "مسقعة مصرية", "Roz Bel Laban": "أرز باللبن",
    "Sayadeya": "صيادية", "Kofta Mashweya": "كفتة مشوية", "Fatteh Masreya": "فتة مصرية",
    "Shorbet Adss": "شوربة عدس", "Shakshouka Masreya": "شكشوكة مصرية", "Kabab Halla": "كباب حلة",
    "Tagen Bamia Bel Lahma": "طاجن بامية باللحمة", "Salatat Baladi": "سلطة بلدي",
    "Baid Bel Basterma": "بيض بالبسطرمة", "Hawawshi": "حواوشي", "Kebda Iskandarani": "كبدة إسكندراني"
}

aliases_list = []
for name in recipes_df['Name']:
    # Add exact English
    aliases_list.append({"RecipeName": name, "Alias": name, "Language": "English"})
    
    # Variations
    v = name.replace(" ", "")
    if v != name:
        aliases_list.append({"RecipeName": name, "Alias": v, "Language": "English"})
    if "ou" in name:
        aliases_list.append({"RecipeName": name, "Alias": name.replace("ou", "oo"), "Language": "English"})
    
    # Mock/Real Arabic
    ar = arabic_names.get(name, "وصفة " + name)
    aliases_list.append({"RecipeName": name, "Alias": ar, "Language": "Arabic"})
    
    # specific variations
    if name == "Koshari":
        aliases_list.append({"RecipeName": name, "Alias": "Koshary", "Language": "English"})
        aliases_list.append({"RecipeName": name, "Alias": "Kosheri", "Language": "English"})
    if name == "Molokhia":
        aliases_list.append({"RecipeName": name, "Alias": "Molokheya", "Language": "English"})
        aliases_list.append({"RecipeName": name, "Alias": "Mulukhiyah", "Language": "English"})

recipe_aliases_df = pd.DataFrame(aliases_list)
recipe_aliases_df.drop_duplicates(subset=['RecipeName', 'Alias'], inplace=True)

# 5. Overwrite the files
recipes_df.to_csv('Recipes.csv', index=False)
recipe_ing_df.to_csv('RecipeIngredients.csv', index=False)
recipe_aliases_df.to_csv('RecipeAliases.csv', index=False)

# Validation check
assert set(recipe_ing_df['FoodName']).issubset(valid_foods), "ERROR: RecipeIngredients contains invalid FoodName"

print("Success!")
print(f"Total recipes: {len(recipes_df)}")
print(f"Total ingredients: {len(recipe_ing_df)}")
print(f"Total aliases: {len(recipe_aliases_df)}")
