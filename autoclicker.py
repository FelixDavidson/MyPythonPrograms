# This is copied directly from StackOverflow
import win32api, win32con, time, os

clear = lambda: os.system('cls')

def click(x, y, z):
    # counter = 0
    # while counter < 1000:
    # I hate while loops. Let's just say that
    for i in range(z):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        time.sleep(.03)


def clickany(z):
    for i in range(z):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(.03)


def choose():
    print '1. Click at x 1200 y 400\n2. Click anywhere you want'
    choice = raw_input('> ')

    print 'How many times?'
    amount = int(raw_input('> '))

    print "Use it more than once or not?"
    more = raw_input('> ')

    if choice == '1' and more == 'y':
        click(1200, 400, amount)
        clear()
        choose()

    elif choice == '1' and more == 'n':
        click(1200, 400, amount)

    elif choice == '2' and more == 'y':
        clickany(amount)
        clear()
        choose()

    elif choice == '2' and more == 'n':
        clickany(amount)

    else:
        print "Feature not yet implimented"
        choose()

choose()
