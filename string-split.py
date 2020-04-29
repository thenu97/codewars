# split string in pair and if odd, pair it with '_'


def soluton(s):
    if len(s) % 2 == 0:
        l = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s) % 2 == 1:
        l = [s[i:i+2] for i in range(0, len(s) - 1, 2)]
        l2 = s[-1] + "_"
        print(l2)
        #l3 = str(l2)
        l.append(l2)
    return l
