def not_string(str):
    splitted = str.split()
    if splitted[0] == 'not':
        return str
    else:
        splitted.insert(0, 'not')
        splitted = ' '.join(splitted)
        return splitted
