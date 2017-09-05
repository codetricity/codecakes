## Create Separate Lists for Each Meal Type

Build 5 lists

- breakfastList
- lunchList
- dinnerList
- snackList
- fullList

## Set Up Question Using Triple Quotes

    question = """
    Are you looking for 
    a) breakfast 
    b) lunch 
    c) dinner
    d) snack
    e) everything

    type in a, b, c, d, or e

    """

## Use `raw_input` or `input` to ask question

Assign response to the variable `answer`

## Use `if` and `elif` statements to assign the restaurants list

    if answer == 'a':
        restaurants = breakfastList
    elif answer == 'b':
        restaurants = lunchList

## Use `while` loop to check for correct answer

    answer = ""

    while answer not in ['a', 'b', 'c', 'd', 'e']:
        answer = raw_input(question)