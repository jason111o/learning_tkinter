from tkinter import *

main = Tk()
main.geometry('600x400')
main.title('Adding Images')

us_flag = PhotoImage(file='./Pictures/us_flag_dark_bg.png')

label_us_flag = Label(main, image=us_flag)

label_us_flag.pack(padx=5, pady=5)

if __name__ == '__main__':
    main.mainloop()
