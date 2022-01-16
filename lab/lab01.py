"""
DSC 20 Lab 01
Name: William Trang
PID: A16679845
"""

# Question 1
def channel_title(first, second, limit):
    """
    >>> channel_title('favorite', 'recipes', 70)
    'Favorite 15 Recipes.'
    >>> channel_title('favorite', 'recipes', 17)
    'Favorite 15 Rec.'
    >>> channel_title('yum', 'recipes', 10)
    'yumyumyum'
    >>> channel_title('yummy', 'rice', 10)
    'Super Chef'
    >>> channel_title('good', 'food', 15)
    'Good 8 Food.'
    >>> channel_title('', '', 3)
    ''
    >>> channel_title(' ', '', 2)
    'Super Chef'
    """
    number = str(len(first) + len(second)) #len of first string + second string and number to put between them in some cases, stored as string

    if (int(number) + len(number) + len('  .')) <= limit:
        return first.capitalize() + ' ' + number + ' ' + second.capitalize() + '.'
    elif (len(second) > 3) and (len(number) + len(first) + len('  .') + 3) <= limit:
        return first.capitalize() + ' ' + number + ' ' + second[0:3].capitalize() + '.'
    elif (len(first) <= 3) and ((len(first) * 3) <= limit):
        return first*3
    return 'Super Chef'


# Question 2
def recipe_type(lst):
    """
    >>> recipe_type([])
    'No preference'
    >>> recipe_type(['vegetarian', 'meatarian','vegetarian', 'meatarian', 'meatarian'])
    'meatarian'
    >>> recipe_type(['vegetarian', 'meatarian','vegetarian'])
    'vegetarian'
    """
    meat = 0 # number of meatarians in list
    veg = 0  # number of vegetarians in list

    for i in range(len(lst)): # counts number of meatarians and vegetarians in list
        if lst[i] == 'meatarian':
            meat += 1
        else:
            veg += 1

    if meat > veg: # return based on results of loop above
        return 'meatarian'
    elif veg > meat:
        return 'vegetarian'
    return 'No preference'


# Question 3
def recipe_name(input, index):
    """
    >>> recipe_name("maytuwmbmdyu ismafldaxd", 2)
    'yummy salad'
    >>> recipe_name("marina", 6)
    'NoName'
    >>> recipe_name("marina", -4)
    'NoName'
    >>> recipe_name("fried_r i c e ", 6)
    'rice'
    >>> recipe_name("", 0)
    'NoName'
    >>> recipe_name("jdka c a k e", 4)
    '    '
    """
    if (index < 0) or (index > (len(input) - 1)): # check if index is negative or out of bounds
        return 'NoName'
    
    name = ''
    for i in range(index, len(input), 2): # if not, create a name from every other letter starting from index
        name += input[i]
    return name


# Question 4
def total_calories(portions, calories):
    """
    >>> total_calories(3, 300)
    'For 3 portions your meal has 900 calories.'
    >>> total_calories(2, 100.75)
    'For 2 portions your meal has 201.5 calories.'
    >>> total_calories(7, 250.35)
    'For 7 portions your meal has 1752.45 calories.'
    >>> total_calories(0, 100)
    'For 0 portions your meal has 0 calories.'
    >>> total_calories(100, 0)
    'For 100 portions your meal has 0 calories.'
    """

    return 'For ' + str(portions) + ' portions your meal has ' + str(portions * calories) + ' calories.'


# Question 5
def calories_per_portion(input):
    """
    >>> calories_per_portion("For 7 portions your meal has 1752 calories.")
    '250.29'
    >>> calories_per_portion("For 4 portions your meal has 1000 calories.")
    '250.0'
    >>> calories_per_portion("For 1 portions your meal has 1 calories.")
    '1.0'
    >>> calories_per_portion("For 10 portions your meal has 0 calories.")
    '0.0'
    """
    lst = input.split(' ') # list containing the individual words in string
    nums = []   # store numbers of string in list

    for i in range(len(lst)):
        if lst[i].isnumeric():
            nums.append(lst[i])

    return str(round((float(nums[1]) / float(nums[0])), 2)) # divide the number of calories by number of portions


# Question 6
def calories_per_item(hundr, weight, number_cookies, output_type):
    """
    >>> calories_per_item(430, 0.3, 20, 0)
    'One item has 64.5 kcal.'
    >>> calories_per_item(430, 0.3, 20, 1)
    'One item has 64.5 Calories.'
    >>> calories_per_item(1, 1000, 10, 1)
    'One item has 1000.0 Calories.'
    >>> calories_per_item(1, 1000, 10, 0)
    'One item has 1000.0 kcal.'
    >>> calories_per_item(0, 1000, 10, 0)
    'One item has 0.0 kcal.'
    """
    kcal_per_item = hundr * 10 # convert kcal per 100g to kcal per kg
    unit = 'kcal'

    if output_type == 1: # change output unit based on input
        unit = 'Calories'
    
    return 'One item has ' + str((kcal_per_item * weight) / number_cookies) + ' ' + unit + '.'