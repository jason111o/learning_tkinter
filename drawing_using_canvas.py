from tkinter import *

main = Tk()
main.title('Drawing using Canvas')
# main.geometry('800x600')

canvas = Canvas(width=500, height=500)
canvas.pack()

canvas.create_line(250, 125, 125, 375, fill='green')
canvas.create_oval(150, 100, 100, 50, fill='red')
canvas.create_rectangle(100, 100, 20, 40, fill='blue')

if __name__ == '__main__':
    main.mainloop()
