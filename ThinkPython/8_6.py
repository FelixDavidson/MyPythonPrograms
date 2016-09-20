def loop_count(word, letter, start):
    count = 0
    for char in word[start:]:
        if char == letter:
            count = count + 1
    print count

loop_count('hello', 'l', 2)
