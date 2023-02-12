from tkinter import *

main = Tk()
main.title('Creating a Basic Paint Program')


def paint_func(event):
    canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill='green')


welcome = Label(main, text="Click and hold left button to draw")
welcome.pack()
canvas = Canvas(main, width=500, height=500, bg='white')
canvas.bind("<B1-Motion>", paint_func)
canvas.pack()

if __name__ == '__main__':
    main.mainloop()
