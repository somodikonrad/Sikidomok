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
#fajl
menu1=Menubutton(menusor, text='Fájl')
menu1.pack(side=LEFT)
FAJL = Menu(menu1)
FAJL.add_command(label="Névjegy", command=nevjegy)
FAJL.add_command(label="Kilépés", command=kilepes)
menu1.config(menu=FAJL)


#síkidomok
menu2 = Menubutton(menusor, text="Síkidomok")
menu2.pack(side=LEFT)
HAROMSZOG = Menu(menu2)
HAROMSZOG.add_command(label="Háromszög", command=haromszog)
HAROMSZOG.add_command(label="Kör", command=kor)
HAROMSZOG.add_command(label="Deltoid", command=deltoid)
HAROMSZOG.add_command(label="Négyzet", command=negyzet)
HAROMSZOG.add_command(label="Trapéz", command=trapez)
HAROMSZOG.add_command(label="Rombusz", command=rombusz)
HAROMSZOG.add_command(label="Paralelogramma", command=paralelogramma)
HAROMSZOG.add_command(label="Téglalap", command=teglalap)
menu2.config(menu=HAROMSZOG)


foablak.mainloop()