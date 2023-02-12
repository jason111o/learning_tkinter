from tkinter import *

main = Tk()
main.geometry('800x600')
main.title('Spanning Colums')

keep_me_logged_in_label = Label(main, text='Keep me logged in')
keep_me_logged_in_check = Checkbutton(main, fg='black')

keep_me_logged_in_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
keep_me_logged_in_check.grid(row=1, column=0, pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()