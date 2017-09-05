import random

city = "Capitola"

restaurants = [
    "Sushi Garden",
    "Betty's Burgers",
    "Asian Express",
    "Mayflower"
    ]

numRestaurants = len(restaurants)

numRestaurantsString = str(numRestaurants)
print("\n\n")
print("There are " + numRestaurantsString + " restaurants in the " + city +
      " list.")

randomPositionInList = random.randrange(0, numRestaurants)

randomRestaurant = restaurants[randomPositionInList]

print("How about " + randomRestaurant + "?")
print("\n\n")
