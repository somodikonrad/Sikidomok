from tkinter import *
from tkinter.messagebox import showerror

foablak = Tk()
foablak.geometry('900x500')
foablak.title("Síkidomok")
foablak.resizable(False, False)
img = PhotoImage(file="matek-icon.png")
foablak.iconphoto(True, img)
foablak.configure(bg="grey")

#MENU
menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)

def nevjegy():
    nevjegy_ablak = Toplevel(foablak)
    szoveg = Label(nevjegy_ablak, text="Készítették:").pack()
    sk = Label(nevjegy_ablak, text="Somodi Konrád").pack()
    vvj = Label(nevjegy_ablak, text="Varga Viktor József").pack()
    svm = Label(nevjegy_ablak, text="Simon Valentin Márk").pack()
    kilepes_gomb = Button(nevjegy_ablak, text="Kilépés", command=nevjegy_ablak.destroy).pack()
    nevjegy_ablak.mainloop()

def kilepes():
    foablak.destroy()

#FAJL
menu1=Menubutton(menusor, text='Fájl')
menu1.pack(side=LEFT)
FAJL = Menu(menu1)
FAJL.add_command(label="Névjegy", command=nevjegy)
FAJL.add_command(label="Kilépés", command=kilepes)
menu1.config(menu=FAJL)


#TERÜLET
def haromszog():
    def szamitas():
        try:
            a = int(mezo1.get())
            m = int(mezo2.get())
            if a == 0:
                showerror("Hiba", "Nem lehet egyik oldal sem nulla!")
            elif m == 0:
                showerror("Hiba", "Nem lehet egyik oldal sem nulla!")
            else:
                terulet = a*m/2
                eredmeny_mezo.configure(state=NORMAL)
                eredmeny_mezo.delete(0, END)
                eredmeny_mezo.insert(0, terulet)
                eredmeny_mezo.configure(state=DISABLED)
        except:
            showerror("Hiba", "Csak számokat adj meg/Minden mezőbe írj számot!")
            mezo1.delete(0, END)
            mezo2.delete(0, END)
            eredmeny_mezo.configure(state=NORMAL)
            eredmeny_mezo.delete(0, END)
            eredmeny_mezo.configure(state=DISABLED)

    haromszog = Toplevel(foablak)
    haromszog.title("Háromszög-Terület")
    haromszog.geometry("200x220")
    haromszog.resizable(False,False)
    img_haromszog = PhotoImage(file="iconkombó.png")
    haromszog.iconphoto(True, img_haromszog)
    c = Canvas(haromszog, width= 100, height=100)
    c.create_polygon((0, 100, 50, 0, 100, 100), fill="red")
    c.grid(row=7, column=3)

    szoveg1 = Label (haromszog, text='a:')
    szoveg2 = Label (haromszog, text='m:')
    szoveg1.grid(row = 1, column = 2)
    szoveg2.grid(row = 2, column = 2)

    mezo1 = Entry(haromszog)
    mezo2 = Entry(haromszog)
    mezo1.grid(row = 1, column = 3)
    mezo2.grid(row = 2, column = 3)
    gomb1 = Button(haromszog, text = 'Számítás', command = szamitas)
    gomb1.grid(row = 3, column = 3)
    szoveg_eredmeny = Label(haromszog, text = 'Eredmény: ')
    szoveg_eredmeny.grid(row = 4, column = 2)
    eredmeny_mezo = Entry(haromszog, state=DISABLED)
    eredmeny_mezo.grid(row = 4, column  = 3)
    kilepes_gomb = Button(haromszog, text="Kilépés", command=haromszog.destroy)
    kilepes_gomb.grid(row=5, column=3)
    haromszog.mainloop()

def kor():
    def szamitas():
        try:
            r = int(mezo1.get())
            if r == 0 or r < 0:
                showerror("Hiba", "Nem lehet nulla, vagy nullánál kisebb!")
            else:
                terulet = r*r*3.14
                eredmeny_mezo.configure(state=NORMAL)
                eredmeny_mezo.delete(0, END)
                eredmeny_mezo.insert(0, terulet)
                eredmeny_mezo.configure(state=DISABLED)
        except:
            showerror("Hiba", "Csak számokat adj meg/Minden mezőbe írj számot!")
            mezo1.delete(0, END)
            eredmeny_mezo.configure(state=NORMAL)
            eredmeny_mezo.delete(0, END)
            eredmeny_mezo.configure(state=DISABLED)

    kor = Toplevel(foablak)
    kor.title("Kör-Terület")
    kor.geometry("200x220")
    kor.resizable(False,False)

    szoveg1 = Label (kor, text='r:')
    szoveg1.grid(row = 1, column = 2)
    mezo1 = Entry(kor)
    mezo1.grid(row = 1, column = 3)

    gomb1 = Button(kor, text = 'Számítás', command = szamitas)
    gomb1.grid(row = 3, column = 3)
    szoveg_eredmeny = Label(kor, text = 'Eredmény: ')
    szoveg_eredmeny.grid(row = 4, column = 2)
    eredmeny_mezo = Entry(kor, state=DISABLED)
    eredmeny_mezo.grid(row = 4, column  = 3)
    kilepes_gomb = Button(kor, text="Kilépés", command=kor.destroy)
    kilepes_gomb.grid(row=5, column=3)
    haromszog= Canvas(kor,width=250, height=250)
    haromszog.grid()
    haromszog.create_oval(60,60,210,210)

    kor.mainloop()














def deltoid():
    pass
def negyzet():
    pass
def trapez():
    pass
def rombusz():
    pass
def paralelogramma():
    pass
def teglalap():
    pass

menu2 = Menubutton(menusor, text="Terület")
menu2.pack(side=LEFT)
Terulet = Menu(menu2)
Terulet.add_command(label="Háromszög", command=haromszog)
Terulet.add_command(label="Kör", command=kor)
Terulet.add_command(label="Deltoid", command=deltoid)
Terulet.add_command(label="Négyzet", command=negyzet)
Terulet.add_command(label="Trapéz", command=trapez)
Terulet.add_command(label="Rombusz", command=rombusz)
Terulet.add_command(label="Paralelogramma", command=paralelogramma)
Terulet.add_command(label="Téglalap", command=teglalap)
menu2.config(menu=Terulet)
#KERÜLET

def kharomszog():
    def szamitas():
        try:
            a = int(mezo0.get())
            b = int(mezo1.get())
            c = int(mezo2.get())
            if a == 0:
                showerror("Hiba", "Nem lehet egyik oldal sem nulla!")
            elif b == 0:
                showerror("Hiba", "Nem lehet egyik oldal sem nulla!")
            elif c == 0:
                showerror("Hiba", "Nem lehet egyik oldal sem nulla!")
            else:
                kerulet = a+b+c
                eredmeny_mezo.configure(state=NORMAL)
                eredmeny_mezo.delete(0, END)
                eredmeny_mezo.insert(0, kerulet)
                eredmeny_mezo.configure(state=DISABLED)
        except:
            showerror("Hiba", "Csak számokat adj meg/Minden mezőbe írj számot!")
            mezo0.delete(0, END)
            mezo1.delete(0, END)
            mezo2.delete(0, END)
            eredmeny_mezo.configure(state=NORMAL)
            eredmeny_mezo.delete(0, END)
            eredmeny_mezo.configure(state=DISABLED)
    kharomszog = Toplevel(foablak)
    kharomszog.title("Háromszög-Kerület")
    kharomszog.geometry("200x250")
    kharomszog.resizable(False,False)
    img_haromszog = PhotoImage(file="iconkombó.png")
    kharomszog.iconphoto(True, img_haromszog)
    c = Canvas(kharomszog, width= 100, height=100)
    c.create_polygon((0, 100, 50, 0, 100, 100), fill="red")
    c.grid(row=7, column=3)

    szoveg1 = Label (kharomszog, text='a:')
    szoveg2 = Label (kharomszog, text='b:')
    szoveg3 = Label (kharomszog, text='c:')
    szoveg1.grid(row = 1, column = 2)
    szoveg2.grid(row = 2, column = 2)
    szoveg3.grid(row = 3, column = 2)
    mezo0 = Entry(kharomszog)
    mezo1 = Entry(kharomszog)
    mezo2 = Entry(kharomszog)
    mezo1.grid(row = 1, column = 3)
    mezo2.grid(row = 2, column = 3)
    mezo0.grid(row = 3, column = 3)
    gomb1 = Button(kharomszog, text = 'Számítás', command = szamitas)
    gomb1.grid(row = 4, column = 3)
    szoveg_eredmeny = Label(kharomszog, text = 'Eredmény: ')
    szoveg_eredmeny.grid(row = 4, column = 2)
    eredmeny_mezo = Entry(kharomszog, )
    eredmeny_mezo.grid(row = 5, column  = 3)
    kilepes_gomb = Button(kharomszog, text="Kilépés", command=kharomszog.destroy)
    kilepes_gomb.grid(row=6, column=3)
    kharomszog.mainloop()

def kkor():
    def szamitas():
        try:
            r = int(mezo1.get())
            if r == 0 or r < 0:
                showerror("Hiba", "Nem lehet nulla, vagy nullánál kisebb!")
            else:
                kerulet = 2*r*3.14
                kerulet = round(kerulet, 2)
                eredmeny_mezo.configure(state=NORMAL)
                eredmeny_mezo.delete(0, END)
                eredmeny_mezo.insert(0, kerulet)
                eredmeny_mezo.configure(state=DISABLED)
        except:
            showerror("Hiba", "Csak számokat adj meg/Minden mezőbe írj számot!")
            mezo1.delete(0, END)
            eredmeny_mezo.configure(state=NORMAL)
            eredmeny_mezo.delete(0, END)
            eredmeny_mezo.configure(state=DISABLED)

    kkor = Toplevel(foablak)
    kkor.title("Kör-Kerület")
    kkor.geometry("200x220")
    kkor.resizable(False,False)

    szoveg1 = Label (kkor, text='r:')
    szoveg1.grid(row = 1, column = 2)
    mezo1 = Entry(kkor)
    mezo1.grid(row = 1, column = 3)

    gomb1 = Button(kkor, text = 'Számítás', command = szamitas)
    gomb1.grid(row = 3, column = 3)
    szoveg_eredmeny = Label(kkor, text = 'Eredmény: ')
    szoveg_eredmeny.grid(row = 4, column = 2)
    eredmeny_mezo = Entry(kkor, state=DISABLED)
    eredmeny_mezo.grid(row = 4, column  = 3)
    kilepes_gomb = Button(kkor, text="Kilépés", command=kkor.destroy)
    kilepes_gomb.grid(row=5, column=3)
    haromszog= Canvas(kkor,width=250, height=250)
    haromszog.grid()
    haromszog.create_oval(60,60,210,210)


def kdeltoid():
    pass

def knegyzet():
    pass

def ktrapez():
    pass

def krombusz():
    pass

def kparalelogramma():
    pass

def kteglalap():
    pass

menu3 = Menubutton(menusor, text="Kerület")
menu3.pack(side=LEFT)
Kerulet = Menu(menu3)
Kerulet.add_command(label="Háromszög", command=kharomszog)
Kerulet.add_command(label="Kör", command=kkor)
Kerulet.add_command(label="Deltoid", command=kdeltoid)
Kerulet.add_command(label="Négyzet", command=knegyzet)
Kerulet.add_command(label="Trapéz", command=ktrapez)
Kerulet.add_command(label="Rombusz", command=krombusz)
Kerulet.add_command(label="Paralelogramma", command=kparalelogramma)
Kerulet.add_command(label="Téglalap", command=kteglalap)
menu3.config(menu=Kerulet)

foablak.mainloop()