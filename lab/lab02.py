"""
DSC 20 Lab 02
Name: William Trang
PID: A16679845
"""

# Question 1
def pick_username(names):
    """
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li"])
    'JonaThan TanoTo'
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li", "ShuBham KauShal"])
    'ShuBham KauShal'
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li", \
"ShuBham KauShal", "MARINA"])
    'MARINA'
    """
    max_index = 0
    max_upper = 0
    current_upper = 0

    for i in range(0, len(names)):
        current_upper = 0
        for j in range(0, len(names[i])):
            if names[i][j].isupper():
                current_upper += 1
        if current_upper >= max_upper:
            max_index = i
            max_upper = current_upper

    return names[max_index]


# Question 2
def username_2(names):
    """
    >>> username_2(["", "Marina"])
    "uncle roger's biggest fan"
    >>> username_2(["LaiCaiJDanHenRoLu", "JJ~", "Chilli Jam Haiyah"])
    'hilli Jam Haiya'
    >>> username_2(["TUTU", "QIQI", "CECE"])
    'EC'
    """
    adjusted_name = "uncle roger's biggest fan"
    i = 0

    while i < len(names):
        if len(names[i]) < 3:
            break
        adjusted_name = names[i][1:len(names[i]) - 1]
        i += 1
    return adjusted_name


# Question 3
def replace_text(text, target, desired):
    """
    >>> replace_text("Fuiyoh, this Lab is short! We love it!", "Lie", "Haiyah")
    'FUIYOH, THIS LAB IS SHORT! WE LOVE IT!'
    >>> replace_text("Chilli Jam is the king of flavor. " + \
"We love Chilli Jam. Chilli Jam makes everything better", "Chilli Jam", "MSG")
    'MSG is the king of flavor. We love Chilli Jam. MSG makes everything better'
    >>> replace_text("I put my leg down from chair,", '', ' Haiyah! ')
    ' Haiyah! I put my leg down from chair, Haiyah! '
    """
    if target not in text:
        return text.upper()

    text = text.replace(target, desired, 1)

    if text.rfind(target) != -1:
        text = text[0:text.rfind(target)] + text[text.rfind(target):].replace(target, desired)
    return text


# Question 4
def convert_password(pass_dict):
    """
    >>> convert_password({'Hu': 5, 'aO': -2, '15': 3})
    'HuHuHuHuHu****151515'
    >>> convert_password({'1': 3, 'mar': 0, 'ker': -1})
    '111.***'
    >>> convert_password({'hellO': 4, '2': -7, 'end': 2})
    'hellOhellOhellOhellO*******endend'
    >>> convert_password({})
    ''
    """
    if len(pass_dict) == 0:
        return ''
    
    password = ''

    for key, value in pass_dict.items():
        if int(value) < 0:
            password += '*' * len(key) * abs(value)
        elif int(value) > 0:
            password += key * value
        else:
            password += '.'

    return password


# Question 5
def most_damage_taken(input_dict):
    """
    >>> most_damage_taken({'Larry': ['Jonathan', 'Marina', 'Theo'], \
'Marina': ['Larry', 'Theo'], 'Jonathan': ['Marina', 'Theo'], \
'Theo': []})
    'Theo'
    >>> most_damage_taken({'Marina': ['Shubham', 'Shubham', 'Kent'], \
'Kent': ['Marina', 'Marina', 'Marina', 'Shubham'], \
'Shubham': ['Kent', 'Marina']})
    'Marina'
    >>> most_damage_taken({'Jonathan': [], 'Larry': ['Jonathan']})
    'Jonathan'
    >>> most_damage_taken({})
    """
    if len(input_dict) == 0:
        return None

    damage_dict = {}
    damage_names = []
    
    for _, values in input_dict.items():
        damage_names += values

    unique_names = list(set(damage_names))

    for i in range(0, len(unique_names)):
        damage_dict[unique_names[i]] = 0

    for i in range(0, len(damage_names)):
        damage_dict[damage_names[i]] += 1

    return max(damage_dict, key = damage_dict.get)
