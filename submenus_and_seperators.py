from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring

main = Tk()
main.title('Sub Menus and Separators')
main.geometry('800x600')


def label_maker():
    label_text = askstring('Making Words on the Window', 'Enter a label name')
    new_label = Label(main, text=f'{label_text}')
    new_label.pack()


my_menu = Menu(main)
main.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=label_maker)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=main.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_cascade(label='Preferences')

if __name__ == '__main__':
    main.mainloop()
