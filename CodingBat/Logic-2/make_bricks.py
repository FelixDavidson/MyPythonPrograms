def make_bricks(small, big, goal):
    if goal > small + big*5:
        return False
    if goal % 5 > small:
        return False
    return True
# one line return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal
