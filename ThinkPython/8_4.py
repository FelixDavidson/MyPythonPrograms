def find(word, letter, start):
    for char in word[start:]:
        if char == letter:
            return char
    return -1
