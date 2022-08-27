from tkinter import *
def toplama():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    s3=str(s1+s2)
    etikets['text']=s3
    
def cikarma():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    s3=str(s1-s2)
    etikets['text']=s3
    
def carpma():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    s3=str(s1*s2)
    etikets['text']=s3#şeklindede yazılabilir
    
def bolme():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    s3=str(s1/s2)
    etikets.config(text=s3)#şeklindede yazılabilir
    
pen=Tk()
pen.geometry("700x400+100+100")
etiket=Label(text="DÖRT İŞLEM",bg="blue",fg="grey",font="verdana 15 bold")
etiket.place(x=200,y=10)

etiket=Label(text="Sayı Bir",bg="blue",fg="grey",font="verdana 10 bold")
etiket.place(x=125,y=50)

etiket=Label(text="Sayı iki ",bg="blue",fg="grey",font="verdana 10 bold")
etiket.place(x=125,y=80)

sayi1=Entry(width=10,bg="grey",fg="blue",font="verdana 12 bold")
sayi1.place(x=200,y=50)

sayi2=Entry(width=10,bg="grey",fg="blue",font="verdana 12 bold")
sayi2.place(x=200,y=80)

topla=Button(text="Topla",width=5,command=toplama)
topla.place(x=125,y=120)

cikar=Button(text="Çıkar",width=5,command=cikarma)
cikar.place(x=205,y=120)

carp=Button(text="Çarp",width=5,command=carpma)
carp.place(x=285,y=120)

bol=Button(text="Böl",width=5,command=bolme)
bol.place(x=355,y=120)

etikets=Label(text="Sonuç",bg="blue",fg="grey",font="verdana 15 bold")
etikets.place(x=340,y=55)

pen.mainloop()
