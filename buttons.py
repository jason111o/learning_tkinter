from tkinter import *

main = Tk()
main.geometry('1200x900')
main.title('Buttons')

label1 = Label(main, text='Label One')
button1 = Button(main, text="Button One")

label1.pack(side=LEFT, padx=5, pady=5)
button1.pack(side=LEFT, padx=5, pady=5)

if __name__ == '__main__':
    main.mainloop()
