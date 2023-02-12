from tkinter import *

main = Tk()
main.geometry('800x600')
main.title('Aligning')

# when using grid you can align by using "sticky=N,E,S,W" (Nort, East, South, West)

user_label = Label(main, text="Email:")
user_entry = Entry(main, bg='white', fg='black')
password_label = Label(main, text='Password:')
password_entry = Entry(main, bg='white', fg='black', show='*')

user_label.grid(row=0, column=0, sticky=E, pady=5, padx=5)
user_entry.grid(row=0, column=1, pady=5, padx=5)
password_label.grid(row=1, column=0, sticky=E, pady=5, padx=5)
password_entry.grid(row=1, column=1, pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()
