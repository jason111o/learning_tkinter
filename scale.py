from tkinter import *

main = Tk()
main.title('Scale')
main.geometry('800x600')

scale = Scale(main, from_=20, to=1000, orient='horizontal')
scale.pack()

if __name__ == '__main__':
    main.mainloop()
