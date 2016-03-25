def pos_neg(a, b, negative):
    return (a < 0 and b < 0 and negative) or (a > 0 and b < 0 and not negative) or (a < 0 and b > 0 and not negative)

# I am very dumb for trying to put this whole thing on one line
# Here is the solution on codingbat
'''
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
'''
