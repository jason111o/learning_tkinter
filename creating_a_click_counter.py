from tkinter import *

count = 0

main = Tk()
main.title('Creating a Click Counter')
main.geometry('800x600')

counter_label = Label(main, text=count, bg='white', fg='black')
instruction_label = Label(main, text='Left click to add, Right click to subtract, and\n"Space" to reset')
click_button = Button(main, text='Click or Treat')


def minus_count(event):
    global count
    if event:
        count -= 1
    counter_label.config(text=count)


def plus_count(event):
    global count
    if event:
        count += 1
    counter_label.config(text=count)


def reset_count(event):
    global count
    if event:
        count = 0
    counter_label.config(text=count)


click_button.bind('<Button-1>', minus_count)
click_button.bind('<Button-3>', plus_count)
main.bind('<Key>', reset_count)

counter_label.pack(pady=5, padx=5)
instruction_label.pack(padx=5, pady=5)
click_button.pack(pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()
