from tkinter import *

main = Tk()
main.title('Creating Menus')
main.geometry('800x600')

my_menu = Menu(main)
main.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label='New')
file_menu.add_command(label='Exit', command=main.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_cascade(label='Preferences')

if __name__ == '__main__':
    main.mainloop()
