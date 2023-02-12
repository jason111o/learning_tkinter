from tkinter import *


main = Tk()


def destroy_window():
    main.destroy()


class OneButton:
    def __init__(self, master, master_title, master_geometry):
        left_frame = Frame(master)
        left_frame.pack(side=LEFT)
        right_frame = Frame(master)
        right_frame.pack(side=RIGHT)
        master.title(master_title)
        master.geometry(master_geometry)

        self.printButton = Button(left_frame, text='Submit', command=self.print_message)
        self.printButton.pack(padx=5, pady=5)
        self.buttonLabel = Label(right_frame, text='Stuff here')
        self.buttonLabel.pack(pady=5, padx=5)
        self.closeButton = Button(right_frame, text='Close', command=destroy_window)
        self.closeButton.bind('<Button-1>', destroy_window)
        self.closeButton.pack(side=BOTTOM, pady=5, padx=5)

    def print_message(self):
        self.buttonLabel.config(text='Button Clicked!')


button1 = OneButton(main, 'Creating Classes', '800x600')

if __name__ == '__main__':
    main.mainloop()
