def front_back(str):
    splitted = list(str)
    if len(str) <= 1:
        return str

    container = splitted.pop(0), splitted.pop(-1)
    splitted.insert(0, container[-1])
    splitted.append(container[0])
    return ''.join(splitted)

"""
Overall pretty good for me. The solution was a bit smaller.

def front_back(str):
  if len(str) <= 1:
    return str

  mid = str[1:len(str)-1]  # can be written as str[1:-1]

  # last + mid + first
  return str[len(str)-1] + mid + str[0]

Redid mine to get it a bit smaller

def front_back(str):
    if len(str) <= 1:
        return str

    center = str[1:-1]
    return str[-1] + mid + str[0]
"""
