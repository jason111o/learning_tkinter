from tkinter import *

main = Tk()
main.geometry('1200x900')
main.title('Adding text via Label()')

label1 = Label(main, text='Here is label1')
label2 = Label(main, text='And here is label2')

label1.pack(pady=5, padx=5)
label2.pack(padx=5, pady=5)

if __name__ == '__main__':
    main.mainloop()