#1

def cat():
    s =     " /\\_/\\" +"\n"
    s = s + "( o.o )" + "\n"
    s = s + " > ^ < " +"\n" 
    return s

def dog():
    s =     "    / \\__" + "\n"
    s = s + "   (    @\\___" + "\n"
    s = s+  "  /         O" + "\n"
    s = s+  " /   (_____/" + "\n"
    s = s + "/_____/"      + "\n"
    return s

def rabbit():
    s =      " __    __" + "\n"
    s = s +  "/ \\\\..// \\" + "\n"
    s = s +  "  ( oo ) " + "\n"
    s = s +  "   \\__/"+"\n"
    return s

class Pets:
    """
    >>> cat1 = Pets("cat", "Fluffy", 4, "F")
    >>> cat2 = Pets("cat", "Buffy", 5, "M")
    >>> print(cat1)
    Fluffy
    <BLANKLINE>
     /\\_/\\
    ( o.o )
     > ^ < 
    <BLANKLINE>

    >>> cat1 < cat2
    True
    >>> cat1 == cat2
    False
    >>> cat1 > cat2
    False
    >>> cat1
    'Animal's type': cat
    'Animal's name: Fluffy
    'Animal's age': 4
    >>> cat3 = cat1 + cat2
    >>> cat3.pet_type
    'cat'
    >>> cat3.name
    'Fy'
    >>> cat3.age
    0
    >>> cat3.gender
    'F'

    >>> d = Pets('dog', 'Zh', 5, 'M')
    >>> cat3 + d
    "Can't add animals of different types or genders."

    >>> cat1 + cat3
    "Can't add animals of different types or genders."
    """

    ascii_art = {"cat": cat(), "dog": dog(), "rabbit": rabbit()}

    def __init__(self, pet_type, name, age, gender):
        self.pet_type = pet_type
        self.name = name
        self.age = age
        self.gender = gender

    def __str__ (self):
        return self.name + '\n\n' + self.ascii_art[self.pet_type]

    def __repr__(self):
        return "'Animal's type': " + self.pet_type + "\n'Animal's name: " + self.name + "\n'Animal's age': " + str(self.age)

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False

    def __eq__(self, other):
        if self.age == other.age:
            return True
        return False

    def __add__(self, other):
        if (self.pet_type == other.pet_type) and (self.gender != other.gender):
            name = ''
            if self.gender == 'F':
                name = self.name[0] + other.name[len(other.name) - 1]
            else:
                name = other.name[0] + self.name[len(self.name) - 1]
            return Pets(self.pet_type, name, 0, 'F') 
        return "Can't add animals of different types or genders."



#2

class Shopping_Cart():
    """
    >>> sh1 = Shopping_Cart()
    >>> sh1.add_item_to_cart("milk", 3, 4)
    >>> sh1.add_item_to_cart("eggs", 2, 2)
    >>> print(sh1.cart)
    {'milk': (3, 4), 'eggs': (2, 2)}
    >>> print(sh1)
    ['milk', 'eggs']
    >>> sh1
    ['milk', 'eggs']
    >>> sh2 = Shopping_Cart()
    >>> sh2.add_item_to_cart("milk", 5, 4)
    >>> sh3 = sh1 + sh2
    >>> print(sh3.cart)
    {'milk': (8, 4), 'eggs': (2, 2)}

    >>> sh1.total()
    16

    >>> sh1 < sh2
    True

    >>> sh1 > sh2
    False

    >>> sh1 == sh2
    False
    """

    def __init__(self):
        self.cart = {}

    def add_item_to_cart(self, item, weight, price_per_pound):
        if item not in self.cart:
            self.cart[item] = (weight, price_per_pound)
        else:
            self.cart[item] = (self.cart[item][0] + weight, price_per_pound)


    def total(self):
        spent = 0
        for _, values in self.cart.items():
            spent += values[1] * values[0]
        return spent

    def __repr__(self):
        return str([i for i in self.cart.keys()])

    def __lt__(self, other):
        if self.total() < other.total():
            return True
        return False

    def __eq__(self, other):
        if self.total() == other.total():
            return True
        return False

    def __add__(self, other):
        new_cart = Shopping_Cart()
        for item, prices in self.cart.items():
            new_cart.add_item_to_cart(item, prices[0], prices[1])
        
        for item, prices in other.cart.items():
            if item not in new_cart.cart.keys():
                new_cart.add_item_to_cart(item, prices[0], prices[1])
            else:
                new_cart.cart[item] = (new_cart.cart[item][0] + prices[0], prices[1])
        return new_cart