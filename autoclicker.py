import win32api, win32con, time, os, sys

clear = lambda: os.system('cls')

def click(x, y, amount, sleep):
    for i in range(amount):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        time.sleep(0.03)
        if win32api.GetAsyncKeyState(ord('P')):
            break


def clickany(amount, sleep):
    for i in range(amount):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.03)
        if win32api.GetAsyncKeyState(ord('P')):
            break


def choose():
    print 'Press P at anytime to stop the program.'
    print '1. Click at x 1200 y 400\n2. Click anywhere you want'
    choice = raw_input('> ')

    print 'How many times?'
    amount = int(raw_input('> '))

    print 'How much sleep?'
    sleep = float(raw_input('> '))

    if sleep <= 0:
        print "Please don't do that. It won't turn out good for you."
        print "Try again"
        sleep = float(raw_input('> '))

    print "Use it more than once or not?"
    more = raw_input('> ')

    if choice == '1' and more == 'y':
        click(1200, 400, amount, sleep)
        clear()
        choose()

    elif choice == '1' and more == 'n':
        click(1200, 400, amount, sleep)

    elif choice == '2' and more == 'y':
        clickany(amount, sleep)
        clear()
        choose()

    elif choice == '2' and more == 'n':
        clickany(amount, sleep)

    elif choice == 'exit':
        sys.exit()

    else:
        print "Feature not yet implimented"
        clear()
        choose()

choose()
