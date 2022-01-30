"""
DSC 20 Lab 04
Name: William Trang
PID: A16679845
"""

# Q1
def smiley(message):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, any, map, and/or filter.

    Make a function that converts specific characters to smiley faces.
    
    >>> smiley("DSC20:(")
    'DSC20:)(:'
    >>> smiley(":e)k3o(")
    ':)e:)k3o(:'
    >>> smiley(":(((((")
    ':)(:(:(:(:(:'
    """
    return ''.join(list(map(lambda mess: ':)' if mess == ':' else '(:' if mess == '(' else ':)' if mess == ')' else mess, message)))

#Q2
def math_message(message):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, map, and/or filter.

    Make a function that converts the specified characters to numbers and removes
    non-alphanumeric characters.

    >>> math_message("Math!!")
    'M4th'
    >>> math_message("DSC20 is Great! :))")
    'D5C20i5Gr34t'
    >>> math_message("!@!@!@")
    ''
    """
    return ''.join(list(map(lambda repl_str: repl_str.replace('e', '3').replace('E', '3').replace('a', '4').replace('A', '4').replace('o', '0').replace('O','0').replace('s', '5').replace('S', '5'), filter(lambda string: string.isalnum(), message))))

#Q3
def chocolate_cakes(recipes):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, map, and/or filter.

    Take a dictionary of dishes and ingredients
    and return cakes that contain chocolate in them.

    >>> chocolate_cakes({'rum cake': ["chocolate", "cheese"], 'fried rice': ["egg", "rice"]})
    ['rum cake']
    >>> chocolate_cakes({'cheesecake': ["sugar", "cheese"], 'fried rice': ["egg", "rice"]})
    []
    >>> chocolate_cakes({})
    []
    """
    cake_check = lambda cake: False if 'cake' not in cake else True
    choco_check = lambda choco: True if 'chocolate' in choco else False
    return list(filter(lambda x: list(map(choco_check, recipes.values())) and list(map(cake_check, recipes)), recipes))

#Q4
def contains_ingredients(ing, check_ing):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, map, and/or filter.

    Take a 2D list of ingredients you have and a list of pancake ingredients.
    Return a 2D list where each list only contains ingredients present in the list
    of pancake ingredients.

    >>> contains_ingredients([["peanut butter","sugar"], ["maple syrup", \
    "brown sugar", "salt"], ["flour", "eggs", "tomatoes"]], ["sugar", \
    "maple syrup", "eggs", "flour"])
    [['sugar'], ['maple syrup'], ['flour', 'eggs']]

    >>> contains_ingredients([["honey", "cinnamon"], ["water", "cucumber"], \
    ["flour", "eggs", "eggplants"], ["vanilla"]], ["vanilla", "honey", \
    "cinnamon", "eggs",])
    [['honey', 'cinnamon'], [], ['eggs'], ['vanilla']]
    """
    return list(map(lambda ings: list(filter(lambda inside_ings: True if inside_ings in check_ing else False, ings)), ing))

#Q5
def christmas_gifts(gifts, maximum_price):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, map, and/or filter.

    Given a list of tuples (Gift, Price), return the list of presents you bought.
    You should buy any present the price of which is below or equal to the maximum price.

    >>> gifts = [('Laptop', 100), ('PS5', 150), ('car', 500), \
    ('Plane ticket', 150)]
    >>> christmas_gifts(gifts, 200)
    ['Laptop', 'PS5', 'Plane ticket']

    >>> gifts = [('Phone', 10), ('PS5', 150), ('car', 500), \
    ('Laptop', 50), ('Clothes', 21)]
    >>> christmas_gifts(gifts, 10)
    ['Phone']
    """
    return list(map(lambda gift_name: gift_name[0],list(filter(lambda gift: True if gift[1] <= maximum_price else False, gifts))))

#Q6
def notifications(notifications_list, max_chars):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this question.
    Instead, use lambda functions, map, and/or filter.

    Given a list of notifications and the number of max characters, determine the
    number of notifications that you received the alert for.

    >>> notif = ['John, Call us', 'Please review our Subscription Policy', \
    'Congrats, you are enrolled in DSC20', 'Pay you rent tomorrow']
    >>> notifications(notif, 35)
    3
    >>> notifications(notif, 1)
    0
    >>> notifications(notif, 100)
    4
    """
    return list(map(lambda notifs: True if len(notifs) <= max_chars else False, notifications_list)).count(True)
