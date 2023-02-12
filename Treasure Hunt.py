from random import randint
from tkinter import Tk, Canvas, Label, Frame, TOP, BOTTOM, LEFT, RIGHT, PhotoImage, Button

WIDTH = 1000
HEIGHT = 800

main = Tk()
main.title('Treasure Hunt')
main.geometry(f'{WIDTH.__str__()}x{HEIGHT.__str__()}')
main.iconphoto(False, PhotoImage(file='/home/jason/PycharmProjects/learning_tkinter/Icons/treasure-map.png'))
# for counting clicks
counter = 0
# for storing mouse coordinates
xc, yc = 0, 0
# for generating random location within the size of the canvas
xr, yr = randint(100, WIDTH - 100), randint(100, HEIGHT - 100)


def make_a_mark(event):
    if event:
        global counter, xc, yc, xr, yr
        counter += 1
        numbers_of_clicks_label.config(text=counter)
        xc, yc = event.x, event.y
        if xc in range(xr - 5, xr + 5) and yc in range(yr - 5, yr + 5):
            how_close_label.config(text='You found the treasure!!!!')
            next_treasure_button.pack(side=TOP, padx=5, pady=5)
        elif xc in range(xr - 25, xr + 25) and yc in range(yr - 25, yr + 25):
            how_close_label.config(text='Hot!!!')
        elif xc in range(xr - 45, xr + 45) and yc in range(yr - 45, yr + 45):
            how_close_label.config(text='Warmer!!')
        elif xc in range(xr - 65, xr + 65) and yc in range(yr - 65, yr + 65):
            how_close_label.config(text='Warm!')
        elif xc in range(xr - 85, xr + 85) and yc in range(yr - 85, yr + 85):
            how_close_label.config(text='Cold!!')
        elif xc in range(xr - 105, xr + 105) and yc in range(yr - 105, yr + 105):
            how_close_label.config(text='Colder!!!')
        else:
            how_close_label.config(text='Freezing!!!!')
        if counter % 20 == 0:
            parrot_button.pack(side=TOP, padx=5, pady=5)
            x_treasure_coordinates_label.config(text=xr)
            y_treasure_coordinates_label.config(text=yr)
        x_coordinates_label.config(text=xc)
        y_coordinates_label.config(text=yc)
        canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill='NavajoWhite4')


def fly_parrot(event):
    if event:
        canvas.create_oval(xr - 80, yr - 80, xr + 80, yr + 80, outline='black')
        parrot_button.pack_forget()


def start_again(event):
    if event:
        next_treasure_button.pack_forget()
        global counter, xc, yc, xr, yr
        counter = 0
        xc, yc = 0, 0
        xr, yr = randint(100, WIDTH - 100), randint(100, HEIGHT - 100)
        x_coordinates_label.config(text=xc)
        y_coordinates_label.config(text=yc)
        x_treasure_coordinates_label.config(text=xc)
        y_treasure_coordinates_label.config(text=yc)
        numbers_of_clicks_label.config(text=counter)


top_frame = Frame(main)
top_frame.pack(side=TOP)
bottom_bottom_frame = Frame(main)
bottom_bottom_frame.pack(side=BOTTOM)
bottom_frame = Frame(main)
bottom_frame.pack(side=BOTTOM)
middle_frame = Frame(main)
middle_frame.pack(side=BOTTOM)

description_label = Label(top_frame, text='Click around on the island to find the treasure.')
description_label.pack(side=LEFT, padx=5, pady=5)
numbers_of_clicks_label = Label(top_frame, text='0')
numbers_of_clicks_label.pack(side=RIGHT, pady=5, padx=5)
numbers_of_clicks_description = Label(top_frame, text='Number of tries')
numbers_of_clicks_description.pack(side=RIGHT, padx=5, pady=5)

canvas = Canvas(main, width=WIDTH - 100, height=HEIGHT - 100, bg='forest green')
canvas.bind('<Button-1>', make_a_mark)
canvas.pack()

how_close_label = Label(middle_frame, text='How close are you mate?')
how_close_label.pack(pady=5, padx=5)

x_coordinates_label = Label(bottom_frame, text='0')
x_coordinates_label.pack(side=LEFT, pady=20, padx=20)
y_coordinates_label = Label(bottom_frame, text='0')
y_coordinates_label.pack(side=RIGHT, pady=20, padx=20)

parrot_button = Button(bottom_bottom_frame, text='Use Poly the Parrot')
parrot_button.bind('<Button-1>', fly_parrot)
next_treasure_button = Button(bottom_bottom_frame, text='Find the next treasure')
next_treasure_button.bind('<Button-1>', start_again)
x_treasure_label = Label(bottom_bottom_frame, text='Coordinates after 10 tries')
x_treasure_label.pack(side=TOP)
x_treasure_coordinates_label = Label(bottom_bottom_frame, text='0')
x_treasure_coordinates_label.pack(side=LEFT, pady=20, padx=20)
y_treasure_coordinates_label = Label(bottom_bottom_frame, text='0')
y_treasure_coordinates_label.pack(side=RIGHT, pady=20, padx=20)

if __name__ == '__main__':
    main.mainloop()
