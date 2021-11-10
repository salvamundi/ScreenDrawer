from tkinter import *


class Canvas:
    def __init__(self):
        window = Tk()
        window.title("ScreenDrawer") # title actually is not necessary since I want the window frames to be invisible

        w_wdth = window.winfo_screenwidth() # get screen width
        w_hgth = window.winfo_screenheight() # get screen height

        # I use entire screen dimensions since the canvas that I want to write on
        # must be on entire screen
        window.geometry(f"{w_wdth}x{w_hgth}") # geometry(widthxheight)
        window.attributes("-alpha", 0.1) # this sets window transparency

        window.mainloop()
