from tkinter import *

main = Tk()
main.title('Drawings #2')
main.geometry('800x600')

canvas = Canvas(main, width=200, height=200)
canvas.pack()

canvas.create_oval(50, 50, 200, 100, fill='yellow')

canvas.create_polygon(30, 30, 100, 30, 45, 80, outline='red', width=2)

if __name__ == '__main__':
    main.mainloop()
