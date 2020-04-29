#move zeros to the end


def move_zeros(array):
    first = []
    second = []
    for i in array:
        if type(i) == int and i == 0:
            second.append(i)
        elif type(i) == float and i == 0.0:
            second.append(i)
        else:
            first.append(i)
    return first + second