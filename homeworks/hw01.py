"""
DSC 20 Homework 01
Name: William Trang (failure to write name or pid will be penalized)
PID: A16679845
"""

# Question 1
def unlucky_number(numbers):
    """
    # Takes in a list of numbers and adds the elements up.
    # Returns True if '4' is in the calculated sum and False if not.

    >>> unlucky_number([1,2,3,4])
    False
    >>> unlucky_number([1,2,3,4,4])
    True

    # Add at least 3 doctests below here #
    >>> unlucky_number([3,3,3,3,3,3,3,3])
    True
    >>> unlucky_number([])
    False
    >>> unlucky_number([-4])
    True
    >>> unlucky_number([-4, 3])
    False
    """
    list_sum = 0
    bad_number = '4'
    for i in range(0, len(numbers)):
        list_sum += numbers[i]
    return bad_number in str(list_sum)

# Question 2
def pick_name(names):
    """
    # Takes in a list of strings and returns the one with the least
    # number of words.

    >>> pick_name(["Hi, welcome to DSC20!", "Goodbye to DSC10!", \
"Get Ready To Work Hard!"])
    'Goodbye to DSC10!'
    >>> pick_name(["Start Early!", "Start Often!", "LET'S GO!"])
    'Start Early!'
    >>> pick_name(["Weiyue likes the Fire Spot"])
    'Weiyue likes the Fire Spot'

    # Add at least 3 doctests below here #
    >>> pick_name(["This is even worse.", "This is sad."])
    'This is sad.'
    >>> pick_name([])
    ''
    >>> pick_name(['', "Japanese ramen"])
    ''
    """
    if len(names) == 0:
        return ""

    names_split = []
    minimum = 1000000000
    min_index = 0

    for i in range(0, len(names)):
        names_split.append(names[i].split())
        if len(names_split[i]) < minimum:
            minimum = len(names_split[i])
            min_index = i

    return names[min_index]

# Question 3
def replace_text(text, target_word, desired_word):
    """
    # Takes in 3 arguments of text we are replacing in, a word to
    # replace, and the word to replace it with. Replaces first
    # instance of word only, and returns original text in all caps
    # if the word to replace is not within the given text.

    >>> replace_text("Dumplings is a very famous dish for the new year", \
"Dumplings", "🥟")
    '🥟 is a very famous dish for the new year'
    >>> replace_text("dumplings dumplings dumplings", "dumplings", "🥟")
    '🥟 dumplings dumplings'
    >>> replace_text("We all love DSC20", "Lie", "Truth")
    'WE ALL LOVE DSC20'
    >>> replace_text("Happy! new! Year!", "!", "🧧")
    'Happy🧧 new! Year!'

    # Add at least 3 doctests below here #
    >>> replace_text('', 'DSC20', 'DSC30')
    ''
    >>> replace_text('Dumpling soup', '', 'lets go')
    'lets goDumpling soup'
    >>> replace_text('abra', 'a', 'switch')
    'switchbra'
    """
    if target_word not in text:
        return text.upper()
    return text.replace(target_word, desired_word, 1)

# Question 4
def approved_recipe(recipe, day, threshold):
    """
    # Takes in three arguments. First is a list containing
    # ingredients and their weights, second is the day of the week,
    # and the third is the threshold that the combined weights must
    # be above. Day of the week affects the multiplier of the
    # ingredients weight. For a recipe to be approved, it must contain
    # the right ingredients and a weight above the threshold.

    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], 'FRIDAY', 30)
    'Fuiyoh'
    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], 'friday', 31)
    'Haiyah'
    >>> approved_recipe([['soy sauce', 10], ['rice', 20], ['egg', 30]], \
'FRIDAY', 30)
    'Haiyah'

    # Add at least 3 doctests below here #
    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], 'SuNdAY', 60)
    'Fuiyoh'
    >>> approved_recipe([['msg', 6], ['rice', 20], ['egg', 30]], 'Sunday', 60)
    'Haiyah'
    >>> approved_recipe([['a', 1], ['b', 2], ['c', 3]], 'Saturday', 0)
    'Haiyah'
    """
    weekends = ['saturday', 'sunday']
    weights = 0
    weight_multiplier = 0.5
    ingredients = []

    if day.lower() in weekends:
        weight_multiplier = 1

    for i in range(0, len(recipe)):
        weights += (recipe[i][1] * weight_multiplier)

    if weights < threshold:
        return 'Haiyah'

    for i in range(0, len(recipe)):
        ingredients.append(recipe[i][0])

    if ('msg' in ingredients) and ('egg' in ingredients) \
            and ('rice' in ingredients):
        return 'Fuiyoh'
    return 'Haiyah'

# Question 5
def money_got(grades):
    """
    # Argument is a list of strings representing grades. Sums up
    # and returns the amount of money that should be received for
    # each report card.

    >>> money_got([])
    'Gapped'
    >>> money_got(["A+", 'A+', "A+", 'A', 'P'])
    90
    >>> money_got(["A+", "A+", "W"])
    0

    # Add at least 3 doctests below here #
    >>> money_got(["a+", "w", "A+", "b-"])
    8
    >>> money_got(["p", "W", "A-"])
    -170
    >>> money_got(["a+", "a", "a-", "b+", "b", "b-"])
    158
    """
    if len(grades) == 0:
        return 'Gapped'

    money = 0
    a_plus_value = 50
    a_value = 40
    a_minus_value = 30
    b_plus_value = 20
    b_value = 10
    b_minus_value = 8
    not_in_scale_value = -100

    for i in range(0, len(grades)):
        if grades[i].upper() == 'A+':
            money += a_plus_value
        elif grades[i].upper() == 'A':
            money += a_value
        elif grades[i].upper() == 'A-':
            money += a_minus_value
        elif grades[i].upper() == 'B+':
            money += b_plus_value
        elif grades[i].upper() == 'B':
            money += b_value
        elif grades[i].upper() == 'B-':
            money += b_minus_value
        else:
            money += not_in_scale_value

    return money

# Question 6
def number_bought(name, grades, product, price):
    """
    # Takes in arguments of a person's name, grades, the product
    # they want to buy, and the unit price of that product. Calculates
    # the amount of spending money based on their grades to determine
    # how many units of the product they can buy maximum.

    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'P'], "milk tea", 5)
    'Yi has bought 18 milk tea and has $0 left.'
    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'P'], "milk tea", 5.2)
    'System Error!'
    >>> number_bought("Weiyue", ["S"], "Football", 200)
    'Weiyue has bought 0 Football and has $-100 left.'

    # Add at least 3 doctests below here #
    >>> number_bought('William', ['A+', 'A', 'A-'], 'pc', 120)
    'William has bought 1 pc and has $0 left.'
    >>> number_bought('William', ['A+', 'A+', 'C'], 'dvd', 1)
    'William has bought 0 dvd and has $0 left.'
    >>> number_bought('', ['A+'], 'dvd', 3)
    ' has bought 16 dvd and has $2 left.'
    """
    if type(price) is not int:
        return 'System Error!'
    spending_money = money_got(grades)
    units_bought = spending_money // price
    remaining_money = spending_money % price

    if spending_money <= 0:
        units_bought = 0
        remaining_money = spending_money

    return name + ' has bought ' + str(units_bought) + ' ' + str(product) + \
        ' and has $' + str(remaining_money) + ' left.'

# Question 7
def report(people, their_grades, products, prices):
    """
    # Takes in lists of a people's name, grades, the product
    # they want to buy, and the unit price of that product. Calculates
    # the amount of spending money based on their grades to determine
    # how many units of the product they can buy maximum.

    >>> print(report(["Theo"], [["A+"]], ["iPad"], [1200]))
    Theo has bought 0 iPad and has $50 left.
    >>> print(report(["Yi", "Yi", "Weiyue", "Jianming"], \
    [["A+", 'A+', "A+", 'A', 'P'], ["A+", 'A+', "A+", 'A', 'P'],\
    ["S"], ["A"]], ["milk tea", "MILK TEA", "Football", "Flowers"], \
    [5,5.2,200,1]))
    Yi has bought 18 milk tea and has $0 left.
    Jianming has bought 40 Flowers and has $0 left.
    System Error!
    Weiyue has bought 0 Football and has $-100 left.
    >>> print(report(["Yi", "Weiyue", "Jianming"], \
    [["A+", 'A+', "A+", 'A', 'P'], \
    ["S"], ["A"]], ["milk tea", "Football", "Flowers"], \
    [5,200,1]))
    Yi has bought 18 milk tea and has $0 left.
    Jianming has bought 40 Flowers and has $0 left.
    Weiyue has bought 0 Football and has $-100 left.

    # Add at least 3 doctests below here #
    >>> print(report([''], ['A'], [''], ['']))
    System Error!
    >>> print(report(["Jim", "Joe", "Jack", "Jay", "Jin"], \
    [["A+", 'A+', "A+", 'A', 'P'], \
    ["S"], ["A"], ["F"], ["A", "A+"]],\
    ["boba", "ball", "bic", "bank", "boar"], [5,200,1,1,3]))
    Jim has bought 18 boba and has $0 left.
    Jin has bought 30 boar and has $0 left.
    Joe has bought 0 ball and has $-100 left.
    Jay has bought 0 bank and has $-100 left.
    Jack has bought 40 bic and has $0 left.
    >>> print(report(["John"], [["A-"]], ["cubes"], [14]))
    John has bought 2 cubes and has $2 left.
    """
    full_report = ""
    for_count = 0
    back_count = len(people) - 1

    while for_count < back_count:
        full_report += number_bought(people[for_count], their_grades[for_count]
                , products[for_count], prices[for_count]) + '\n'
        full_report += number_bought(people[back_count],
            their_grades[back_count], products[back_count], prices[back_count])

        for_count += 1
        back_count -= 1
        if (for_count == back_count) or for_count < back_count:
            full_report += '\n'

    if for_count == back_count:
        full_report += number_bought(people[for_count],
            their_grades[for_count], products[for_count], prices[for_count])
    return full_report

# Question 8
def pick_best_shoes(selections, numbers):
    """
    # Takes in a list of strings (shoe names) and a list of numbers.
    # Performs operations with the numbers to pick out a shoe
    # from the list.

    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,3,5,7,9])
    'AJ1'
    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,4,6])
    'AJ2'
    >>> pick_best_shoes(["Air Mag"], [2001])
    'Air Mag'

    # Add at least 3 doctests below here #
    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,3,5,7,11])
    'AJ1'
    >>> pick_best_shoes(['KD', 'MJ'], [2])
    'MJ'
    >>> pick_best_shoes(['Magnets'], [324894])
    'Magnets'
    """
    current_number = 1
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            current_number += numbers[i]
        elif numbers[i] % 3 == 0:
            current_number -= numbers[i]
        elif numbers[i] % 5 == 0:
            current_number /= numbers[i]
        elif numbers[i] % 7 == 0:
            current_number = current_number ** numbers[i]
        else:
            current_number = current_number // numbers[i]
    return selections[int(current_number) % len(selections)]

# Question 9
def concat_lyrics(lyrics, threshold):
    """
    # Accepts two arguments, a list of lists of strings
    # and an integer. Joins the lists if the word count would
    # remain below the given threshold and returns the joined
    # lists.

    >>> print(concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 10))
    We’re so young, boy
    We ain’t got nothin' to lose
    <BLANKLINE>
    >>> print(concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 9))
    We’re so young, boy
    <BLANKLINE>
    >>> concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 3)
    ''

    # Add at least 3 doctests below here #
    >>> print(concat_lyrics([['a'], ['a', 'a', 'a'], ['a']], 3))
    a
    a
    <BLANKLINE>
    >>> print(concat_lyrics(['a'], 1))
    a
    <BLANKLINE>
    >>> print(concat_lyrics(['apple', 'bottom', 'jeans'], 1))
    <BLANKLINE>
    """
    lyrics_sum = 0
    full_lyrics = ''
    for i in range(0, len(lyrics)):
        if lyrics_sum + len(lyrics[i]) <= threshold:
            lyrics_sum += len(lyrics[i])
            full_lyrics += ' '.join(lyrics[i]) + '\n'

    return full_lyrics

# Question 10
def in_festival(fest_coord, approx_loc, radius):
    """
    # Calculates the distance between two coordinates
    # using the distance formula. Returns true if distance
    # is less than or equal to the given radius
    # (festival is in GPS radius).

    >>> in_festival([1,2], [2,4], 2)
    False
    >>> in_festival([1,2], [3,2], 1)
    False
    >>> in_festival([1,2], [2,2], 1)
    True

    # Add at least 3 doctests below here #
    >>> in_festival([0, 0], [0, 0], 10000)
    True
    >>> in_festival([-1, 1], [1, 1], 4)
    True
    >>> in_festival([-1, 1], [1, 1], 1.5)
    False
    """
    return ((fest_coord[1] - approx_loc[1]) ** 2 +
            (fest_coord[0] - approx_loc[0]) ** 2) ** 1/2 <= radius
