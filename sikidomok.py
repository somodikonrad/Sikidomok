from tkinter import *

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
    pass

def kilepes():
    pass





#fajl
menu1=Menubutton(menusor, text='Fájl')
menu1.pack(side=LEFT)
FAJL = Menu(menu1)
FAJL.add_command(label="Névjegy", command=nevjegy)
FAJL.add_command(label="Kilépés", command=kilepes)
menu1.config(menu=FAJL)


#Terület

def haromszog():
    def szamitas():
        pass
    haromszog = Toplevel(foablak)
    haromszog.title("Háromszög-Terület")
    haromszog.geometry("450x450")
    haromszog.resizable(False,False)
    img_haromszog = PhotoImage(file="iconkombó.png")
    haromszog.iconphoto(True, img_haromszog)

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
    eredmeny_mezo = Entry(haromszog)
    eredmeny_mezo.grid(row = 4, column  = 3)




    haromszog.mainloop()
def kor():
    pass
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
#Kerület

def kharomszog():
    kharomszog = Toplevel(foablak)
    kharomszog.title("Háromszög-Kerület")
    kharomszog.geometry("450x450")
    kharomszog.resizable(False,False)
    img_haromszog = PhotoImage(file="iconkombó.png")
    kharomszog.iconphoto(True, img_haromszog)

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
    gomb1.grid(row = 3, column = 3)
    szoveg_eredmeny = Label(kharomszog, text = 'Eredmény: ')
    szoveg_eredmeny.grid(row = 4, column = 2)
    eredmeny_mezo = Entry(kharomszog)
    eredmeny_mezo.grid(row = 4, column  = 3)



    kharomszog.mainloop()
def kkor():
    pass
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