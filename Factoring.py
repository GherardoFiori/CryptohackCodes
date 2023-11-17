import math
number = 510143758735509025530880200653196460532653147
def print_factors(number):
    return [(x, number / x)  for x in range(int(math.sqrt(number)))[2:] if not number % x]

print (print_factors)