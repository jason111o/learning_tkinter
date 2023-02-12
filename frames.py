from tkinter import *


main = Tk()
main.geometry('600x400')
main.title('Frames')

frame1 = Frame(main)
frame2 = Frame(main)

label1_frame1 = Label(frame1, text='Label One in Frame One')
button1_frame1 = Button(frame1, text='Button One in Frame One')
label2_frame2 = Label(frame2, text='Label Two in Frame Two')
button2_frame2 = Button(frame2, text='Button Two in Frame Two')

frame1.pack(side='left')
frame2.pack(side='right')
label1_frame1.pack(padx=5, pady=5)
button1_frame1.pack(pady=5, padx=5)
label2_frame2.pack(padx=5, pady=5)
button2_frame2.pack(pady=5, padx=5)

if __name__ == '__main__':
    main.mainloop()