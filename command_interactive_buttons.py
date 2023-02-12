from tkinter import *
from functions import button_press_print_random_phrases, random_directions

main = Tk()
main.title('Command - Interactive Buttons')
main.geometry('600x400')


def random_button():
    some_phrase = str(button_press_print_random_phrases())
    button1.config(text=some_phrase)
    button1.pack(side=random_directions())


button1 = Button(main, text='Button One', command=random_button)
button1.pack()

if __name__ == '__main__':
    main.mainloop()
