from tkinter import *
import os

main = Tk()
main.geometry('600x400')
main.title('Adding an Icon')
if "nt" == os.name:
    main.wm_iconbitmap(bitmap="./Icons/us_flag_dark_bg.ico")
else:
    main.iconbitmap(bitmap='@./Icons/us_flag_dark_bg.xbm')

if __name__ == '__main__':
    main.mainloop()

#### This file is a bust. No real workaround for the bitmap of icons