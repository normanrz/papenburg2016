from query import query
from cgitb import text
from tkinter import *
from People.search import VectorSpace
query = VectorSpace.search
results=0
import os
import sys


top = Tk()
top.geometry("1050x300+300+100")
top.title("Find your Famous")
top.grid()
top.resizable(0, 0)
top.config(background='lightpink')


def suche():
	global results
	resultlbl.config(state="normal")
	resultlbl.delete(0,END)
	results=query(searchfield.get(),IndexPath="People//search//index")
	results2=results
	for i in results2:
			resultlbl.insert(END, i[0]) # name,text
	# resultlbl.config(state="disabled")
	countlbl.config(text=("Es wurden\n {} \nErgebnisse \n gefunden.").format(str(len(results2))))


def click(event):
	#print(event.widget())
	print(resultlbl.get(ACTIVE))
	listeAusgewaehlt = event.widget.curselection()
	print(listeAusgewaehlt)
	itemAusgewaehlt = listeAusgewaehlt[0]
	nameAusgewaehlt = resultlbl.get(itemAusgewaehlt)
	print(index, "HALOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
	erg=results[index][1]
	os.system(str(erg))

def internet():
	weblink = lb
global resultlbl
frame1 = Frame(top)
searchlbl = Label(top, text="Suche Eingeben:", font=("Arial", 25, "bold"))
searchlbl.config(background='lightskyblue')
searchfield = Entry(top, font=("Arial", 35, "bold"))
searchbutton = Button(top, text="Suchen", font=("Arial", 20, "bold"), command=suche)
searchbutton.config(background='hotpink')
resultscroller = Scrollbar(frame1)
resultlbl = Listbox(frame1, height=10, width=70, font=("Arial", 14, "bold"))
resultlbl.bind('<Double-Button-1>', click)
countlbl = Label(top, text=("Es wurden\n 0 \nErgebnisse \n gefunden."), width=10, font=("Arial", 12, "bold"))

resultscroller.config(command=resultlbl.yview)
resultlbl.config(yscrollcommand=resultscroller.set)
frame1.grid(row=1, columnspan=2)
# frame2.grid()
searchlbl.grid(row=0, column=0, sticky=N + S + E + W)
searchfield.grid(row=0, column=1, sticky=N + S + E + W)
searchbutton.grid(row=0, column=3, sticky=N + S + E + W)
countlbl.grid(row=1, column=3)
resultlbl.pack(side=LEFT, fill=Y)

resultscroller.pack(side=RIGHT, fill=Y)

def eingabe(event):
	suche()
searchfield.bind('<KeyPress-Return>',eingabe)

top.mainloop()

