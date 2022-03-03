"""
DSC 20 Homework 08
Name: William Trang
PID: A16679845
"""

# Question 1
def from_list_to_dict(lst):
    """
    >>> lst = [(1,2),(3,4),(5,6)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6}

    >>> lst = [("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {'one': 1, 'two': 2}

    >>> lst = []
    >>> from_list_to_dict(lst)
    {}

    # Add at least 3 doctests below #

    """
    #if len(lst) == 1:

    return dict(lst)


# Question 2
def make_two_dicts(str1, str2, key1, key2):
    """
    >>> s1 = "abc"
    >>> s2 = "abd"
    >>> make_two_dicts(s1, s2, "k1", "k2")
    {'k1': ['b', 'a'], 'k2': ['c']}

    >>> s1 = "abcd"
    >>> s2 = "hijkl"
    >>> make_two_dicts(s1, s2, "k1", "k2")
    {'k1': [], 'k2': ['d', 'c', 'b', 'a']}

    >>> s1 = "marina"
    >>> s2 = "langlois"
    >>> make_two_dicts(s1, s2, "key1", "key2")
    {'key1': ['a', 'n', 'i', 'a'], 'key2': ['r', 'm']}

    # Add at least 3 doctests below #

    """
    lst1 = []
    lst2 = []
    if len(str1) == 1:
        if str1 in str2:
            return lst1.append(str1), lst2
        else:
            return lst1, lst2.append(str1)

    return make_two_dicts(str1[0], str2, key1, key2), make_two_dicts(str1[1:], str2, key1, key2)


# Question 3
def dict_decompose(d):
    """
    >>> d={"M,L":["DSC20", "DSC30"], "A,B":["DSC20", "DSC30"],\
    "C,D":["DSC20", "DSC10"]}
    >>> l1, l2 = dict_decompose(d)
    >>> l1.sort()
    >>> l1
    ['A,B', 'C,D', 'M,L']
    >>> l2.sort()
    >>> l2
    ['DSC10', 'DSC20', 'DSC30']

    >>> d = {1:[1,2,3], 2:[3,4,5], 3:[]}
    >>> l1, l2 = dict_decompose(d)
    >>> l1.sort()
    >>> l1
    [1, 2, 3]
    >>> l2.sort()
    >>> l2
    [1, 2, 3, 4, 5]

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    return list(d), list(d)


# Question 4
def q4_doctests():
    """
    >>> Smurfette = Smurf(15, 500, 20, 100)
    >>> Jokey = Common_Smurf(20, 300, 15, 150)
    >>> papa_smurf = PaPa_Smurf(99, 1000, 150, 1000)
    >>> Smurfette.grow_plant(15)
    True
    >>> Smurfette.coin
    485
    >>> Smurfette.harvest(15, 35, 40)
    True
    >>> Smurfette.coin
    505
    >>> Smurfette.experience
    140
    >>> Jokey.count_level()
    'Your smurf is at level 31'
    >>> Smurfette.make_deal(Jokey, 10)
    True
    >>> Smurfette.coin
    495
    >>> Jokey.coin
    310
    >>> Jokey.make_deal(Smurfette, 200)
    True
    >>> Jokey.smurf_berry
    15
    >>> Jokey.make_deal(papa_smurf, 10)
    'Papa Smurf caught you!'
    >>> Jokey.coin
    0
    >>> papa_smurf.count_level()
    'Your smurf is at level 220'
    """
    return

class Smurf:
    """
    A class that abstracts the Smurf character of the game.
    """
    def __init__(self, age, coin, smurf_berry, experience):
        """
        Constructor of Smurf. Input validation not required
        Parameters:
            age (int): the age of a certain smurf
            coin (int): number of coin the smurf holds
            smurf_berry (int): number of smurf_berry the smurf holds
            experience (int): total experience of a certain smurf
        """
        self.age = age
        self.coin = coin
        self.smurf_berry = smurf_berry
        self.experience = experience


    def grow_plant(self, cost):
        """
        Return a boolean based on if we are able to successfully grow
        the plant. If successful, deduct the cost of the plant from coin.
        Otherwise, return False
        """
        if cost <= self.coin:
            self.coin -= cost
            return True
        return False

    
    def make_deal(self, other_smurf, val_item):
        """
        Makes a deal with another smurf for an item worth val_item amount
        of coins. If you don't have enough coins, attempt to use smurf berries.
        Return True if the deal is successful, and False otherwise.
        """
        berry_to_coins = 10
        if self.coin >= val_item:
            self.coin -= val_item
            other_smurf.coin += val_item
            return True
        elif self.smurf_berry * berry_to_coins >= val_item:
            val_berry = val_item / berry_to_coins
            if int(val_berry) != val_berry:
                val_berry = int(val_berry) + 1

            self.smurf_berry -= val_berry
            other_smurf.smurf_berry += val_berry
            return True
        return False
    

    def harvest(self, cost, revenue, experience):
        """
        Try to grow and harvest the plant based on the cost. If we are able
        to, increase coin and experienced based on revenue and experience,
        and return True.
        If not, return False
        """
        if self.grow_plant(cost):
            self.coin += revenue
            self.experience += experience
            return True
        return False

            
    def count_level(self):
        """
        Count the level of the smurf.
        Each level is based on experience in blocks of 5
        Return the string 'Your smurf is at level x', where x is the level
        """
        xp_per_level = 5
        level = int(self.experience / xp_per_level) + 1
        return 'Your smurf is at level ' + str(level)

class Common_Smurf(Smurf):
    """
    A class that abstracts the Common Smurf character of the game.
    """
    def make_deal(self, other_smurf,val_item):
        """
        Makes a deal with another smurf for an item worth val_item amount
        of coins.

        However, if you meet a Papa Smurf, you lose all your coins and return
        the string 'Papa Smurf caught you!'
        """
        if isinstance(other_smurf, PaPa_Smurf):
            self.coin = 0
            return 'Papa Smurf caught you!'
        return super().make_deal(other_smurf, val_item)
    
class PaPa_Smurf(Smurf):
    """
    A class that abstracts the Papa Smurf character of the game.
    """
    def count_level(self):
        """
        Count the level of the smurf.
        Each level is based on experience + age in blocks of 5
        Return the string 'Your smurf is at level x', where x is the level
        """
        xp_per_level = 5
        level = int((self.experience + self.age) / xp_per_level) + 1
        return 'Your smurf is at level ' + str(level)


# Question 5
def q5_doctests():
    """
    >>> kart_1 = Kart()
    >>> kart_2 = NormalKart()
    >>> kart_3 = CheaterKart()
    >>> kart_2.nitro(20)
    True
    >>> kart_1.attack(kart_2)
    False
    >>> kart_2.high_score()
    9100
    >>> kart_2.attack(kart_3)
    False
    >>> kart_2.speed
    30
    >>> kart_3.high_score()
    25750
    >>> kart_4 = CheaterKart()
    >>> kart_3.attack(kart_4)
    True
    >>> kart_4.size
    7
    >>> kart_4.speed
    20
    >>> kart_3.size
    8
    >>> kart_4.nitro(40)
    True
    >>> kart_4.lives
    6
    >>> kart_4.attack(kart_2)
    True
    >>> kart_4.high_score()
    24650
    >>> kart_4.size
    8
    >>> kart_2.speed
    50
    """
    return

class Kart:

    def __init__(self):
        self.speed = 50
        self.size = 5
        self.powerup = 3
        self.lives = 3
        return
    
    def nitro(self, boost):
        if self.powerup == 0:
            return False
        self.powerup -= 1
        orig_score = self.high_score()
        self.speed = int((((self.speed + boost) ** 2) + ((self.speed - boost) ** 2)) ** (1/2))
        new_score = self.high_score()
        if new_score >= orig_score * 2:
            self.lives += 1
        return True
        
    
    def set_speed(self, new_speed):
        self.speed = new_speed
        
    
    def set_lives(self, gains = True):
        if gains:
            self.lives += 1
        else:
            self.lives -= 1
        
            
    def set_size(self, new_size):
        self.size = new_size
        
        
    def attack(self, other_kart):
        speed_increment = 50

        if self.size > other_kart.size:
            self.speed += speed_increment
            other_kart.speed -= speed_increment
            if other_kart.speed < 0:
                other_kart.speed = speed_increment
                other_kart.lives -= 1
                self.size += 1
            return True
        elif self.size < other_kart.size:
            other_kart.speed += speed_increment
            self.speed -= speed_increment
            if self.speed < 0:
                self.speed = speed_increment
                self.lives -= 1
                other_kart.size += 1
        return False
        
    
    def high_score(self):
        speed_mult = 100
        lives_mult = 500
        return  self.speed * speed_mult + self.lives * lives_mult
    
class NormalKart(Kart):

    def attack(self, other_kart):
        if isinstance(other_kart, CheaterKart):
            self.lives -= 1
            self.speed = 30
            other_kart.size += 1
            other_kart.speed += 50
            return False
        return super().attack(other_kart)
        
class CheaterKart(Kart):

    def __init__(self):
        self.speed = 70
        self.size = 7
        self.powerup = 5
        self.lives = 5
        
    def high_score(self):
        speed_mult = 200
        lives_mult = 300
        score_mod = 250
        return self.speed * speed_mult + self.lives * lives_mult + score_mod