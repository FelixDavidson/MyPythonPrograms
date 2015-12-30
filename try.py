while True:
    try:
        x = int(raw_input("Enter a number: "))
        print "Nice number."
    except Exception as e:
        print "That's not a number"
