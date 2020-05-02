import tkinter as tk

def init():
    win.quit()

win = tk.Tk()
win.title("Snake")

mode = tk.Frame()
modetxt = tk.Label(master = mode, text = 'Select Colour Scheme')
dark = tk.Button(master = mode, text = 'DARK MODE', bg = 'black', fg = 'yellow')
light = tk.Button(master = mode, text = 'LIGHT MODE', bg = 'white', fg = 'green')

mode.pack()
modetxt.pack()
dark.pack()
light.pack()

speed = tk.Frame()
speedtxt = tk.Label(speed, text = 'Select Speed of Snake')
scale = tk.Scale(speed, from_ = 0, to = 50, orient = 'horizontal')

speed.pack()
speedtxt.pack()
scale.pack()

butt = tk.Button(win, text = 'Play',bg = 'blue', fg = 'white', command = init())
butt.pack()

win.mainloop()
