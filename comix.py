from tkinter import *

root = Tk()
root.geometry("500x200")
PYGlabel1 = Label(root, text="안녕하세요? 박이건입니다", bg="red", fg ="yellow",width=70, height=3)
PYGlabel2 = Label(root, text="제가 좋아하는 과일은 딸기입니다", bg="red", fg="yellow",width=70, height=3, font=("궁서체",30))

PYGlabel1.pack()
PYGlabel2.pack()
root.mainloop()