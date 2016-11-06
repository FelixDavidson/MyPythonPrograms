import pyautogui, time

print "Welcome to Escapists Gym trainer 1.0!"
print "This program allows you to train hands free in the Escapists"

def train():
    print "Would you like to use the treadmill or the weights?"

    choice = raw_input('> ')

    if choice in {'1', 'treadmill', 'Treadmill'}:
        print "Here we go!"

        treadmill()

def treadmill():
    for i in range(100):
        pyautogui.keyDown('q')
        pyautogui.keyUp('q')
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')

train()
