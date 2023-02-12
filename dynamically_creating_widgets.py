from tkinter import *

main = Tk()
main.title('Dynamically Creating Widgets')
main.geometry('800x600')

for num in range(10):
    button = Button(main, text=num)
    button.pack()

if __name__ == '__main__':
    main.mainloop()
