# First, install the correct packages
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_recipe(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information (adjusted for the actual HTML structure)
        title = soup.find('h1')  # Assuming the title is in an h1 tag
        ingredients = soup.find_all('li', class_='recipe-ingredients__item')
        instructions = soup.find_all('li', class_='recipe-instructions__item')

        # Create a dictionary with the scraped information
        recipe_data = {
            'title': title.text.strip() if title else "Title not found",
            'ingredients': [item.text.strip() for item in ingredients] if ingredients else ["Ingredients not found"],
            'instructions': [step.text.strip() for step in instructions] if instructions else ["Instructions not found"]
        }

        return recipe_data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# URL of the recipe page
url = "https://www.google.com/search?q=milk+bikis+ingredients+complete+list"

# Scrape the recipe
recipe = scrape_recipe(url)

# Print the scraped data
if recipe:
    print(f"Recipe: {recipe['title']}")
    print("\nIngredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print("\nInstructions:")
    for i, step in enumerate(recipe['instructions'], 1):
        print(f"{i}. {step}")
else:
    print("Failed to scrape the recipe.")