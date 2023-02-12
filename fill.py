from tkinter import *

main = Tk()
main.geometry('600x400')
main.title('Fill')

label1 = Label(main, text='Blue', bg='blue')
label2 = Label(main, text='Green', bg='green')
label3 = Label(main, text='Red', bg='red')

label1.pack(padx=5, pady=5, fill='x')
label2.pack(padx=5, pady=5, fill='x')
label3.pack(padx=5, pady=5, fill='x')

if __name__ == '__main__':
    main.mainloop()