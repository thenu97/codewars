#capitalise first letter of every word in a sentence

def to_jaden_case(string):
    return ' '.join(s[:1].upper() + s[1:] for s in string.split(' '))