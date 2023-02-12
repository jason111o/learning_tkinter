from tkinter import *


def get_user_input():
    label_print_user_name.config(text="You said your name is {}".format(user_name.get()))


main = Tk()
main.geometry('600x400')
main.title('Getting User Input')

label_ask_user = Label(main, text='What\'s you name fool?!')
user_name = Entry(main, bg='white', fg='black')
submit_button = Button(main, text='Submit', command=get_user_input)
label_print_user_name = Label(main)

label_ask_user.pack(padx=5, pady=5)
user_name.pack(pady=5, padx=5)
submit_button.pack(padx=5, pady=5)
label_print_user_name.pack(pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()
