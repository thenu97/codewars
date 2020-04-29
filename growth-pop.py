#population growth

import math
def nb_year(p0, percent, aug, p):
    n = 1
    while n >= 0:
        incre = percent / 100
        p_i = int(p0 + p0*incre + aug)
        print(p_i)
        if p_i >= p:
            break
        else:
            n = n + 1
            p0 = p_i
    return n