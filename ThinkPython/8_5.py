def loop_count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print count

loop_count('hello', 'l')
