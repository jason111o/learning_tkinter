from tkinter import *

main = Tk()
main.title('How to keep improving')
main.geometry('800x600')

how_to_list = ['Go over concepts', 'Stay practical', 'Get creative', 'New content']
rownum, colnum = 0, 0
for num in range(len(how_to_list)):
    label = Label(main, text=f'{rownum}.\t{how_to_list[num]}')
    label.grid(row=rownum, column=colnum, pady=2, padx=2, sticky=W)
    rownum += 1

if __name__ == '__main__':
    main.mainloop()
