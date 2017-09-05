import random


question = """
Are you looking for 
a) breakfast 
b) lunch 
c) dinner
d) snack
e) everything

type in a, b, c, d, or e

"""

answer = ""

while answer not in ['a', 'b', 'c', 'd', 'e']:
    answer = raw_input(question)


city = "Capitola"

fullList = [
    "Sushi Garden",
    "Betty's Burgers",
    "Asian Express",
    "Mayflower"
]

breakfastList = [
    "Avenue Cafe"
]

lunchList = [
    "Chipotle",
    "Betty's Burgers"
]

dinnerList = [
    "Sushi Garden",
    "Dharma"
]

snackList = [
    "Yogurt Land"
]

if answer == 'a':
    restaurants = breakfastList
elif answer == 'b':
    restaurants = lunchList
elif answer == 'c':
    restaurants = dinnerList
elif answer == 'd':
    restaurants = snackList
else:
    restaurants = fullList

numRestaurants = len(restaurants)

numRestaurantsString = str(numRestaurants)
print("\n\n")
print("There are " + numRestaurantsString + " restaurants in the " + city +
      " list.")

randomPositionInList = random.randrange(0, numRestaurants)

randomRestaurant = restaurants[randomPositionInList]

print("How about " + randomRestaurant + "?")
print("\n\n")
