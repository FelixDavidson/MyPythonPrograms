# This is copied directly from StackOverflow
import win32api, win32con, time
def click(x,y):
    # counter = 0
    # while counter < 1000:
    # I hate while loops. Let's just say that
    for i in range(500):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        time.sleep(.05)
click(1200, 400)
