from tkinter import *

main = Tk()
main.title('Storing Scale')
main.geometry('800x600')


def check_temp():
    current_temp = temp_scale.get()
    print(current_temp)
    if current_temp in range(60, 70):
        temp_label.config(text='Livable')
    elif current_temp in range(70, 80):
        temp_label.config(text='Too hot')
    elif current_temp in range(50, 60):
        temp_label.config(text='Too cold')
    else:
        temp_label.config(text='Death is eminent')


temp_scale = Scale(main)
temp_scale.pack()

button1 = Button(main, text='Check Temperature', command=check_temp)
button1.pack()

temp_label = Label(main, text="Temperature Status")
temp_label.pack()

if __name__ == '__main__':
    main.mainloop()
