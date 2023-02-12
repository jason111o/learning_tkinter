from tkinter import *

main = Tk()
main.geometry('600x400')
main.title('Grid')

email_label = Label(main, text='Email:')
password_label = Label(main, text='Password:')

email_entry = Entry(main, bg='white', fg='black')
password_entry = Entry(main, bg='white', fg='black', show="*")

email_label.grid(column=0, row=0, pady=5, padx=5)
email_entry.grid(column=1, row=0, pady=5, padx=5)
password_label.grid(column=0, row=1, pady=5, padx=5)
password_entry.grid(column=1, row=1, pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()