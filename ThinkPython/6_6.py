def first(word):
    return word[0]

def last(word):
    return word[-1] 

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if word[::-1] == word:
        return True
    return False

is_palindrome('noon')
