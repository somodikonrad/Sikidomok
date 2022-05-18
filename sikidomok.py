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

def haromszog():
    pass

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
def kharomszog():
    pass
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
#fajl
menu1=Menubutton(menusor, text='Fájl')
menu1.pack(side=LEFT)
FAJL = Menu(menu1)
FAJL.add_command(label="Névjegy", command=nevjegy)
FAJL.add_command(label="Kilépés", command=kilepes)
menu1.config(menu=FAJL)


#Terület
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