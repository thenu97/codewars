# counter for numbers divisible by 3 and 5

var_total = 0
for x in range(number):
    if (x % 3 == 0 or x % 5 == 0):
        var_total == var_total + x
    else:
        pass
    return var_total