from tkinter import *

main = Tk()
main.title('Common Event Labels')
main.geometry('800x600')

show_pressed_key_label = Label(main, text='Pressed keys will replace this text\nand pressing "q" will close this window')
show_pressed_key_label.pack(padx=50, pady=50)


def q_pressed(event):
    main.destroy()


def you_pressed(event):
    show_pressed_key_label.config(text=event)


main.bind('<Key>', you_pressed)
main.bind('<q>', q_pressed)

if __name__ == '__main__':
    main.mainloop()
