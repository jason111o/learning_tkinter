from tkinter import *
from tkinter import messagebox

main = Tk()
main.title('Message Box')
main.geometry('800x600')


def error_message():
    messagebox.showerror(title='Message Box Error')


button1 = Button(main, text='Do not click me', command=error_message)
button1.pack()

if __name__ == '__main__':
    main.mainloop()
