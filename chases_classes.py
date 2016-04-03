import time # import datetime instead because you could show the date
from os import system

clear = lambda: os.system('cls')

class Subject(object):


# Most of your else statments don't really do anything useful
# this is manily because they are not in functions meaning they just kill the program after running
a_day = "A"
b_day = "B"
c_day = "C"
d_day = "D"
e_day = "E"
f_day = "F"

#dicts work like this
classes = {"English":eng, "History":hist, "Biology":bio,
            "Biology Lab":biolab, "Lunch":lun, "Spanish":span,
            "Religion":rel, "Math":math, "Gym":gym, "Computer Seminar":comp,
            "Health":health}

english_rm = 607
history_rm = 503
biologylab_rm = 409
biology_rm = 416
lunch_rm = "Cafeteria"
spanish_rm = 304
religion_rm = 608
math_rm = 113
gym_rm = "Gym"
health_rm = 504
computerseminar_rm = 105

print "Schedule system now running. What letter day would you like to see?"
letter_day = raw_input('Enter a letter:')

if letter_day == "A" or "B" or "C" or "D" or "E" or "F": #this doesn't work. you are first asking if letter_day is A then asking if B. All non-empty strings return true.
    print 'Working...'
    time.sleep(2) # why do you sleep?
else:
    print 'Input a letter'

print "Now what period would you like to know?"
period = raw_input('Enter a number: ')
# this is extremely long
def classname():
    if letter_day == "A" and period == "1": # this doesn't work. Input is not a int. use int(raw_input()) for that
        print a_1
    elif letter_day == "A" and period == "2":
        print a_2
    elif letter_day == "A" and period == "3":
        print a_3
    elif letter_day == "A" and period == "4":
        print a_4
    elif letter_day == "A" and period == "5":
        print a_5
    elif letter_day == "A" and period == "6":
        print a_6
    elif letter_day == "A" and period == "7":
        print a_7
    elif letter_day == "A" and period == "8":
        print a_8
    elif letter_day == "B" and period == "1": # same here as above. You just copy and pasted this didn't you
        print b_1
    elif letter_day == "B" and period == "2":
        print b_2
    elif letter_day == "B" and period == "3":
        print b_3
    elif letter_day == "B" and period == "4":
        print b_4
    elif letter_day == "B" and period == "5":
        print b_5
    elif letter_day == "B" and period == "6":
        print b_6
    elif letter_day == "B" and period == "7":
        print b_7
    elif letter_day == "B" and period == "8":
        print b_8
    elif letter_day == "C" and period == "1": # again
        print c_1
    elif letter_day == "C" and period == "2":
        print c_2
    elif letter_day == "C" and period == "3":
        print c_3
    elif letter_day == "C" and period == "4":
        print c_4
    elif letter_day == "C" and period == "5":
        print c_5
    elif letter_day == "C" and period == "6":
        print c_6
    elif letter_day == "C" and period == "7":
        print c_7
    elif letter_day == "C" and period == "8":
        print c_8
    elif letter_day == "D" and period == "1": # one more time
        print d_1
    elif letter_day == "D" and period == "2":
        print d_2
    elif letter_day == "D" and period == "3":
        print d_3
    elif letter_day == "D" and period == "4":
        print d_4
    elif letter_day == "D" and period == "5":
        print d_5
    elif letter_day == "D" and period == "6":
        print d_6
    elif letter_day == "D" and period == "7":
        print d_7
    elif letter_day == "D" and period == "8":
        print d_8
    elif letter_day == "E" and period == "1": # we're getting there
        print e_1
    elif letter_day == "E" and period == "2":
        print e_2
    elif letter_day == "E" and period == "3":
        print e_3
    elif letter_day == "E" and period == "4":
        print e_4
    elif letter_day == "E" and period == "5":
        print e_5
    elif letter_day == "E" and period == "6":
        print e_6
    elif letter_day == "E" and period == "7":
        print e_7
    elif letter_day == "E" and period == "8":
        print e_8
    elif letter_day == "F" and period == "1": # here we are
        print f_1
    elif letter_day == "F" and period == "2":
        print f_2
    elif letter_day == "F" and period == "3":
        print f_3
    elif letter_day == "F" and period == "4":
        print f_4
    elif letter_day == "F" and period == "5":
        print f_5
    elif letter_day == "F" and period == "6":
        print f_6
    elif letter_day == "F" and period == "7":
        print f_7
    elif letter_day == "F" and period == "8":
        print f_8
    else:
        print "Could not find class." # should say can't find class fuck off because this exits the program
        time.sleep(2)
        clear()

time.sleep(2) # why do you have the program sleep. Everyone would want this instantaneously

print "Would you like to know the room number of a class?"
answer = raw_input("Yes or No?")
if answer == "Yes": # this does not account for someone typing yes which ends the program
    print 'Ok, what class?'
else:
    print 'Ok!' # what is the point of this else statement. It says ok and then exits

class_name = raw_input('Class name:')
if class_name == "History":
    print history_rm
elif class_name == "English":
    print english_rm
elif class_name == "Biology":
    print biology_rm
elif class_name == "Biology Lab":
    print biologylab_rm
elif class_name == "Lunch":
    print lunch_rm
elif class_name == "Spanish":
    print Spanish_rm
elif class_name == "Religion":
    print religion_rm
elif class_name == "Math":
    print math_rm
elif class_name == "Gym":
    print gym_rm
elif class_name == "Computer Seminar":
    print computerseminar_rm
elif class_name == "Health":
    print health_rm
else:
    print "Class not found." # Should also say fuck off because it exits the program
