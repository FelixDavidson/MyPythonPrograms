prefixes = 'JKLMNOPQ'
suffix = 'ack'
fixed_suffix = 'uack'

for letter in prefixes:
    if letter in ['O', 'Q']:
        print letter + fixed_suffix
    print letter + suffix

