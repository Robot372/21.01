   
from tkinter import *

root = Tk() #6 i 11
root.title("Raspisanie")

a = StringVar()
a.set('')
b = StringVar()
b.set('')
c = StringVar()
c.set('')

def urok1(event):
    okno1=Toplevel()
    okno1.grab_set()
    okno1.geometry("275x300")
    logw=Label(okno1, text="Logistikateenused ja varude juhtimine.\nÕpetaja nimi: Inessa Klimanskaja B002", width=40,height=20)
    logw.grid(row=0, column=0)
    okno1.mainloop()

def urok2(event):
    okno2=Toplevel()
    okno2.grab_set()
    okno2.geometry("275x300")
    logw=Label(okno2, text="Programeerimise alused(eesti keeles).\nÕpetaja nimi:Marina Oleinik E07", width=40,height=20)
    logw.grid(row=0, column=0)
    okno2.mainloop()

def urok3(event):
    okno3=Toplevel()
    okno3.grab_set()
    okno3.geometry("275x300")
    logw=Label(okno3, text="Kunstiained(eesti keeles).\nÕpetaja nimi:Norkevits Aleksandra B232", width=40,height=20)
    logw.grid(row=0, column=0)
    okno3.mainloop()

   
def urok4(event):
    okno4=Toplevel()
    okno4.grab_set()
    okno4.geometry("275x300")
    logw=Label(okno4, text="Inglise keel.\nÕpetaja nimi:Olga Poskotinova B138", width=40,height=20)
    logw.grid(row=0, column=0)
    okno4.mainloop()

def urok5(event):
    okno5=Toplevel()
    okno5.grab_set()
    okno5.geometry("275x300")
    logw=Label(okno5, text="Arenduskeskkonna loomine.\nÕpetaja nimi:Irina Merkulova E10 ", width=40,height=20)
    logw.grid(row=0, column=0)
    okno5.mainloop()

   
def urok6(event):
    okno6=Toplevel()
    okno6.grab_set()
    okno6.geometry("275x300")
    logw=Label(okno6, text="Eesti Keel.\nÕpetaja nimi:Olesja Ojamäe B227 ", width=40,height=20)
    logw.grid(row=0, column=0)
    okno6.mainloop()

def urok7(event):
    okno7=Toplevel()
    okno7.grab_set()
    okno7.geometry("275x300")
    logw=Label(okno7, text="Arenduskeskkonna loomine.\nÕpetaja nimi:Irina Merkulova E10 ", width=40,height=20)
    logw.grid(row=0, column=0)
    okno7.mainloop()

def urok8(event):
    okno8=Toplevel()
    okno8.grab_set()
    okno8.geometry("275x300")
    logw=Label(okno8, text="Eesti Keel.\nÕpetaja nimi:Alina Läänevali-Toots B236", width=40,height=20)
    logw.grid(row=0, column=0)
    okno8.mainloop()

def urok9(event):
    okno9=Toplevel()
    okno9.grab_set()
    okno9.geometry("275x300")
    logw=Label(okno9, text="Arenduskeskkonna loomine.\nÕpetaja nimi:Irina Merkulova E10", width=40,height=20)
    logw.grid(row=0, column=0)
    okno9.mainloop()

def urok10(event):
    okno10=Toplevel()
    okno10.grab_set()
    okno10.geometry("275x300")
    logw=Label(okno10, text="Programeerimise alused(eesti keeles).\nÕpetaja nimi:Marina Oleinik E07", width=40,height=20)
    logw.grid(row=0, column=0)
    okno10.mainloop()

def urok11(event):
    okno11=Toplevel()
    okno11.grab_set()
    okno11.geometry("275x300")
    logw=Label(okno10, text="Arenduskeskkonna loomine.\nÕpetaja nimi:Irina Merkulova E10", width=40,height=20)
    logw.grid(row=0, column=0)
    okno10.mainloop()

def urok12(event):
    okno12=Toplevel()
    okno12.grab_set()
    okno12.geometry("275x300")
    logw=Label(okno12, text="Inglise keel.\nÕpetaja nimi:Olga Poskotinova B138", width=40,height=20)
    logw.grid(row=0, column=0)
    okno12.mainloop()

Label(text="").grid(row=0, column=0)
table_name = Label(width=50)
table_name.grid(row=0, column=1, columnspan=3)
Label(text="").grid(row=1, column=0)
Label(text="").grid(row=3, column=0)
Label(text="").grid(row=5, column=0)
Label(text="").grid(row=7, column=0)
Label(text="").grid(row=9, column=0)
Label(text="").grid(row=11, column=0)
Label(text="Понедельник").grid(row=2, column=0)
Label(text="Вторник").grid(row=4, column=0)
Label(text="Среда").grid(row=6, column=0)
Label(text="Четверг").grid(row=8, column=0)
Label(text="Пятница").grid(row=10, column=0)
Label(text="0\n7:40-8:25").grid(row=0, column=1)
Label(text="1\n8:20-9:15").grid(row=0, column=2)
Label(text="2\n9:20-10:05").grid(row=0, column=3)
Label(text="3\n10:10-10:55").grid(row=0, column=4)
Label(text="4\n11:00-11:45").grid(row=0, column=5)
Label(text="5\n11:50-12:35").grid(row=0, column=6)
Label(text="6\n12:40-13:25").grid(row=0, column=7)
Label(text="7\n13:30-14:15").grid(row=0, column=8)
Label(text="8\n14:20-15:05").grid(row=0, column=9)
Label(text="9\n15:10-15:55").grid(row=0, column=10)
Button(text="Eesti keel", bg="grey").grid(row=1, column=2)
btn1=Button(text="Logistikateenused\nja varude juhtimine", bg="green")
btn1.grid(row=1, column=3, columnspan=2)
Button(text="Matemaatika", bg="pink").grid(row=1, column=5)
Button(text="Matemaatika", bg="pink").grid(row=1, column=6)
Label(text="").grid(row=1, column=7)
Button(text="Keel ja\nkirjandus", bg="green").grid(row=1, column=8)
Button(text="Keel ja\nkirjandus", bg="green").grid(row=1, column=9)
Button(text="Tugiope\n(keemia)", bg="purple").grid(row=4, column=2)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=4, column=3, columnspan=3)
Label(text="").grid(row=4, column=6)
Button(text="Füüsika", bg="pink").grid(row=4, column=7, columnspan=2)
Label(text="").grid(row=6, column=1)
Button(text="Eesti keel\nkui teine", bg="purple").grid(row=6, column=2)

Button(text="Kunstiained\n(eesti keeles)", bg="purple").grid(row=6, column=3, columnspan=2)
Label(text="").grid(row=6, column=5)
Button(text="   Kehaline kasvatus   ", bg="purple").grid(row=6, column=6, columnspan=2)
Button(text="Logistikateenused\nja varude juhtimine", bg="green").grid(row=7, column=2,columnspan=2)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=7, column=5, columnspan=2)
Button(text="Inglise keel", bg="lightyellow").grid(row=7, column=7, columnspan=2)
Button(text="Arenduskeskkonna loomine", bg="pink").grid(row=8, column=7, columnspan=2)
Button(text="Eesti keel", bg="grey").grid(row=8, column=9, columnspan=7)
Button(text="Arenduskeskkonna loomine", bg="pink").grid(row=7, column=9, columnspan=2)
Button(text="Eesti keel", bg="pink").grid(row=9, column=2, columnspan=2)
Button(text="Arenduskeskkonna loomine", bg="pink").grid(row=10, column=2, columnspan=2)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=10, column=3, columnspan=5)
Button(text="Arenduskeskkonna loomine", bg="pink").grid(row=9, column=9, columnspan=2)
Button(text="Inglise keel", bg="green").grid(row=10, column=9, columnspan=2)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=10, column=5, columnspan=5)

btn3=Button(text="Kunstiained\n(eesti keeles)", bg="purple")
btn3.grid(row=6, column=3, columnspan=2,sticky=N+S+W+E)
Label(text="").grid(row=6, column=5)
Button(text="   Kehaline kasvatus   ", bg="purple").grid(row=6, column=6, columnspan=2,sticky=N+S+W+E)
btn1=Button(text="Logistikateenused\nja varude juhtimine", bg="green")
btn1.grid(row=7, column=2,columnspan=2,sticky=N+S+W+E)
btn2=Button(text="Programeerimise alused(eesti keeles)", bg="lightblue")
btn2.grid(row=7, column=5, columnspan=2,sticky=N+S+W+E)
btn4=Button(text="Inglise keel", bg="lightyellow")
btn4.grid(row=7, column=7, columnspan=2,sticky=N+S+W+E)
btn5=Button(text="Arenduskeskkonna loomine", bg="pink")
btn5.grid(row=8, column=7, columnspan=2,sticky=N+S+W+E)
btn6=Button(text="Eesti keel", bg="grey")
btn6.grid(row=8, column=9, columnspan=7,sticky=N+S+W+E)
btn7=Button(text="Arenduskeskkonna loomine", bg="pink")
btn7.grid(row=7, column=9, columnspan=2,sticky=N+S+W+E)
btn8=Button(text="Eesti keel", bg="pink")
btn8.grid(row=9, column=2, columnspan=2,sticky=N+S+W+E)
btn9=Button(text="Arenduskeskkonna loomine", bg="pink")
btn9.grid(row=10, column=2, columnspan=2,sticky=N+S+W+E)
btn10=Button(text="Programeerimise alused(eesti keeles)", bg="lightblue")
btn10.grid(row=10, column=3, columnspan=5,sticky=N+S+W+E)
btn11=Button(text="Arenduskeskkonna loomine", bg="pink")
btn11.grid(row=9, column=9, columnspan=2,sticky=N+S+W+E)
btn12=Button(text="Inglise keel", bg="green")
btn12.grid(row=10, column=9, columnspan=2,sticky=N+S+W+E)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=10, column=4, columnspan=4,sticky=N+S+W+E)
Exit = Button(root, text = "ВЫХОД", command = root.quit).grid(row = 0, column = 0)

btn1.bind("<Button-1>",
           lambda e="Description": urok1(e))

btn2.bind("<Button-1>",
           lambda e="Description": urok2(e))

btn3.bind("<Button-1>",
           lambda e="Description": urok3(e))

btn4.bind("<Button-1>",
           lambda e="Description": urok4(e))

btn5.bind("<Button-1>",
           lambda e="Description": urok5(e))

btn6.bind("<Button-1>",
           lambda e="Description": urok6(e))

btn7.bind("<Button-1>",
           lambda e="Description": urok7(e))

btn8.bind("<Button-1>",
           lambda e="Description": urok8(e))

btn9.bind("<Button-1>",
           lambda e="Description": urok9(e))

btn10.bind("<Button-1>",
           lambda e="Description": urok10(e))

btn11.bind("<Button-1>",
           lambda e="Description": urok11(e))

btn12.bind("<Button-1>",
           lambda e="Description": urok12(e))

root.geometry("1200x600")

root.mainloop()