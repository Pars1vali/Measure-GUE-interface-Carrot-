from tkinter import *
from tkinter import ttk
from tkinter import *
from PIL import *
from PIL import Image, ImageTk

def measure():
    sqr = int(len_et.get()) * int(len_et.get())
    sqr2 = sqr
    sqr_carrot = 40
    self = Toplevel()
    self.title('открытое окно')
    self.geometry('400x400')
    count = 1

    self.img = ImageTk.PhotoImage(Image.open("carrot3.png").resize((50,50), Image.LANCZOS))
    while sqr2>0:
        self.panel = Label(self, image=self.img).grid(padx=1+count,pady=1+count)
        # self.panel.grid()
        sqr2 = sqr2-sqr_carrot
        if(sqr2<0):
            sqr_last_pcocent= ((abs(sqr2)*100)/sqr)/100
            if(sqr_last_pcocent<0.2):
                sqr2-=sqr2
        count+=1




main_w = Tk()
main_w.geometry("550x350")
main_w["bg"] = '#F3943A'
main_w.resizable(0, 0)

length_l = Label(text="Length", bg='#FFFFFF', width=10, font="Terminal", borderwidth=7).place(x=110, y=120)
width_l = Label(text="Width", bg='#FFFFFF', width=10, font="Terminal", borderwidth=7).place(x=330, y=120)

len_et = Entry(width=11, font='Terminal',borderwidth=3, bg="#FFFFFF")
len_et.place(x=105, y=165)

wid_et = Entry(width=11, font='Terminal',borderwidth=3, bg="#FFFFFF").place(x=345, y=165)

carrot_img = PhotoImage(file=r"C:\Users\parsi\PycharmProjects\measurer\carrot3.png").subsample(3,3)

calc_b = Button(main_w,image=carrot_img,command=measure, borderwidth=5).place(x=240, y=120)

main_w.mainloop()
