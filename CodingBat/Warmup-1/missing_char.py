def missing_char(str, n):
    splitted = list(str)
    splitted.pop(n)
    joined = ''.join(splitted)
    return joined
