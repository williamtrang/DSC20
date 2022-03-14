from re import T


class UCSD_Dragon:
    total_number_of_dragons = 0
    def __init__(self, name, cost_per_day):
        self.name = name
        self.cost_per_day = cost_per_day
        UCSD_Dragon.total_number_of_dragons += 1
    
    def set_color(self, color):
        self.color = color
    
    def number_of_dragons():
        return UCSD_Dragon.total_number_of_dragons

    def __str__(self):
        try:
            return self.name + ' is ' + self.color
        except:
            raise AttributeError('No Such Attribute')

    def cost_per_week(self, cleaning_fee):
        return self.cost_per_day * 7 + cleaning_fee
    
    def __lt__(self, other):
        if self.cost_per_week(0) < other.cost_per_week(0):
            return True
        return False
