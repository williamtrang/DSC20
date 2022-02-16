# Question 1.

class Mascot:
    """ 
    Creates a simple Mascot class with 1 class attribute (type)
    and 3 instance attributes (color, nickname, event)
    >>> mascot1 = Mascot("black and white", "Bing Dwen Dwen", "Olympic Games")
    >>> Mascot.brings
    'Luck'
    >>> mascot1.color
    'black and white'
    >>> mascot1.sing_song("Together for a shared future")
    "Bing Dwen Dwen sings 'Together for a shared future' at Olympic Games"
    >>> mascot1.change_nickname("Puff Puff")
    >>> mascot1.nickname
    'Puff Puff'
    >>> mascot1.event
    'Olympic Games'

    >>> mascot2 = Mascot("brown", "Mishka", "Olympic Games")
    >>> Mascot.brings
    'Luck'
    >>> mascot2.color
    'brown'
    >>> mascot2.sing_song("Goodbye, Moscow!")
    "Mishka sings 'Goodbye, Moscow!' at Olympic Games"
    >>> mascot2.change_nickname("The Olympic Mishka")
    >>> mascot2.nickname
    'The Olympic Mishka'
    """
    brings = 'Luck'
    
    # Initializer (Constructor) / Instance Attributes
    def __init__ (self, color, nickname, event):
        self.color = color
        self.nickname = nickname
        self.event = event

    def sing_song(self, song):
        return self.nickname + '\'' + song + '\'' + ' at ' + self.event

    def change_nickname (self, new_name):
        self.nickname = new_name


# Question 2

class Winter_Olympics:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Winter_Olympics.mascot
    'Bing Dwen Dwen'
    >>> Winter_Olympics.starts()
    'Friday, February 4'
    >>> Winter_Olympics.ends()
    'Sunday, February 20'
    """

    # YOUR CODE GOES HERE #


# Question 3

class Phone:
    """
    Creates a Phone class 3 instance attributes (brand, battery,
    storage) passed to the constructor. Then add 5 more attributes
    (charge, drain_rate,charge_rate, num_apps, apps), derived from the
    three given instance attributes and 3 methods (use, recharge, install)

    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Robinhood')
    'App installed'
    >>> my_phone.apps
    {'Robinhood'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    """
    # Initializer
    def ******(self, brand, ******, ******):
        self.brand = brand
        self.battery = ******
        self.storage = ******
        self.charge = ******
        # Drain rate will differ based on brand
        # Create if-else structure
        self.drain_rate = ******
        self.charge_rate = ******
        self.num_apps = ******
        self.apps = set()

    def use(self, minutes):
        # TODO: Update charge
        self.****** = ******
        if ******: # Handles case when we run out of charge
            ******
            return 'Out of charge'

    def recharge(self, minutes):
        # TODO: Update charge
        ******.****** = ******

    def install(self, app_size, app_name):
        # Cannot install apps when we don't have charge
        if ******:
            return 'Out of charge'
        # Cannot install apps when we don't have sufficient storage
        if ******:
            return 'Not enough storage'
        # Cannot install apps that are already installed
        if ******:
            return 'App already installed'

        # Have dealt with all potential issues. Install app now
        # TODO: Update storage
        ******
        # TODO: Update num_apps
        ******
        # TODO: Update apps
        ******
        return 'App installed'

# Question 4

def max_recursion(tup):
    """
    Returns the largest element in the tuple.

    >>> max_recursion((1,2,3,4))
    4
    >>> max_recursion((13,2,3,4))
    13
    >>> max_recursion((13,2,33,4))
    33
    """

    # Your code is here

# Question 5

def max_or_min_recursion(tup, find_max = True):
    """
    Returns the largest or smallest element in the tuple,
    depending on the optinal parameter.

    >>> max_or_min_recursion((1,2,3,4))
    4
    >>> max_or_min_recursion((13,2,3,4), False)
    2
    >>> max_or_min_recursion((13,2,33,-4), True)
    33
    """

    # Your code is here

# Question 6

def find_winner(record, find_max=True):
    """
    
    Returns the name of the country with either largest or
    smallest score, depending on the optional parameter.

    >>> find_winner([('Germany',23),('USA', 49), ('South Korea', 32)])
    'USA'
    >>> find_winner([('China', 12.88),('Japan', 15)], find_max=False)
    'China'
    >>> find_winner([('France', 10), ('UK', 10), ('Spain', 5)], find_max=True)
    'France'
    """
    # Your code is here
    
    # somewhere here you may want to use a call to a helper recursive function:
    # find_winner_helper(record, find_max)



# Recursive function. Think, what does it return?
def find_winner_helper(record, find_max):
    # add your own doct tests to check correctness. 


