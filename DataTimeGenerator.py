import time
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
dataTime=time.strftime("%Y-%m-%d %H:%M")
print dataTime
r.clipboard_append(dataTime)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
