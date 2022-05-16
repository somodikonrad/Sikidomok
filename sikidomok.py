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

# def nevjegy():
#     masodikAblak = Toplevel(foablak)
#     fejlesztok = Message(masodikAblak, text="Készítők: ")

#fajl
menu1=Menubutton(menusor, text='Fájl')
menu1.pack(side=LEFT)
FAJL = Menu(menu1)
FAJL.add_command(label="Névjegy", command=nevjegy)
FAJL.add_command(label="Kilépés", command=foablak.destroy)


#síkidomok


foablak.mainloop()