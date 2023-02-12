from tkinter import *

main = Tk()
main.title('Buttons')

label1 = Label(main, text='Label One', fg='blue', bg='red')
button1 = Button(main, text="Button One", pady=200, padx=300, fg="black", bg="white")

label1.pack(pady=5, padx=5)
button1.pack(side=LEFT, padx=5, pady=5)

if __name__ == '__main__':
    main.mainloop()
