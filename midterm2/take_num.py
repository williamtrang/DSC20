from re import L


def take_num(num):
    def is_even():
        if num % 2 == 0:
            return True
        return False
    def is_greater(limit):
        if num > limit:
            return True
        return False
    def is_sum_prime(to_add):
        return is_prime(num + to_add)
    return is_even, is_greater, is_sum_prime
