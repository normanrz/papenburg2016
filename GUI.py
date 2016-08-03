from query import query
from cgitb import text
from tkinter import *

top = Tk()
top.geometry("1050x300+300+100")
top.title("Find your Famous")
top.grid()
top.resizable(0, 0)


def suche():
	results=query(searchfield.get())
	resultlbl.config(state="normal")
	resultlbl.insert(END, "hiiii")
	resultlbl.config(state="disabled")
	#pass
def ergebnisgeben(begriff):
	pass
	
	
text = "Hallo dies ist ein Text !!fgasdfjlasjflkjashdflheight=10,width=30ihasdfkhaskjfhasifhsivfhosahfopasdghpoasrjgüpoasdjfüsrajfoüisrhgoisdfasfhasizfsdhfoashfohsdfohsafhsaifh30ihasdfkhaskjfhasifhsivfhosahfopasdghpoasrjgüpoasdjfüsrajfoüisrhgo30ihasdfkhaskjfhasifhsivfhosahfopasdghpoasrjgüpoasdjfüsrajfoüisrhgoisdfasfhasizfsdhfoashfohsdfohsafhsaifhspfhhfsiasideisdfasfhasizfsdhfoashfohsdfohsafhsaifhspfhhfsiasidespfhhfsiaside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Ysdjgoüisagjü0sri!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
frame1 = Frame(top)

# frame2 = Frame(top)
searchlbl = Label(top, text="Suche Eingeben:", font=("Arial", 25, "bold"))
searchfield = Entry(top, font=("Arial", 35, "bold"))
searchbutton = Button(top, text="Suchen", font=("Arial", 20, "bold"), command=suche)
resultscroller = Scrollbar(frame1)
resultlbl = Text(frame1, height=10, font=("Arial", 14, "bold"))
countlbl = Label(top, text="Es wurden\n 0 \nErgebnisse \n gefunden.", width=10, font=("Arial", 12, "bold"))
resultlbl.insert(END, text)
resultscroller.config(command=resultlbl.yview)
resultlbl.config(yscrollcommand=resultscroller.set, state="disabled")
frame1.grid(row=1, columnspan=2)
# frame2.grid()
searchlbl.grid(row=0, column=0, sticky=N + S + E + W)
searchfield.grid(row=0, column=1, sticky=N + S + E + W)
searchbutton.grid(row=0, column=3, sticky=N + S + E + W)
countlbl.grid(row=1, column=3)
resultlbl.pack(side=LEFT, fill=Y)

resultscroller.pack(side=RIGHT, fill=Y)

top.mainloop()

'''other, unused stuff
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid(sticky=N + S + E + W)
		self.createWidgets()
	
	def createWidgets(self):
		top = self.winfo_toplevel()
		top.rowconfigure(0, weight=1)
		top.columnconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.frame1 = Frame(self)
		self.frame2 = Frame(self)
		self.searchlbl = Label(self.frame1, text="Suche Eingeben:")
		self.searchfield = Entry(self.frame1)
		self.searchbutton = Button(self.frame1, text="Suchen")
		self.resultscroller = Scrollbar(self.frame2)
		self.resultlbl = Text(self.frame2)
		self.resultlbl.insert(END, text)
		self.resultscroller.config(command=self.resultlbl.yview)
		self.resultlbl.config(yscrollcommand=self.resultscroller.set)
		
		self.frame1.grid(row=0, sticky=N + S + E + W)
		self.frame2.grid(row=1, sticky=N + S + E + W)
		
		self.searchlbl.grid(row=0, column=0, sticky=N + S + E + W)
		self.searchfield.grid(row=0, column=1, sticky=N + S + E + W)
		self.searchbutton.grid(row=0, column=3, sticky=N + S + E + W)
		self.resultlbl.pack(side=LEFT, fill=Y)
		self.resultscroller.pack(side=LEFT, padx=5, pady=5)
		
		



searchlbl.grid(side=LEFT, anchor=N, padx=5, pady=5)
searchfield.pack(side=LEFT, anchor=N, padx=5, pady=5)
searchbutton.pack(side=LEFT, padx=5, pady=5)
resultscroller.pack(side=RIGHT, fill=Y)

resultlbl.pack(side=LEFT, fill=Y)

app = Application()
app.master.title('Find Your Famous')
app.mainloop()

'''
