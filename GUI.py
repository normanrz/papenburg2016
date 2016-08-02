# import query
from tkinter import *

top = Tk()
top.geometry("900x900+300+100")
top.title("Find you Famous")


text = "Hallo dies ist ein Text !!fgasdfjlasjflkjashdflihasdfkhaskjfhasifhsivfhosahfopasdghpoasrjgüpoasdjfüsrajfoüisrhgoisdfasfhasizfsdhfoashfohsdfohsafhsaifhspfhhfsiaside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Yside=RIGHT, fill=Ysdjgoüisagjü0sri!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"



frame1 = Frame(top)

frame2 = Frame(top)
searchlbl = Label(frame1, text="Suche Eingeben:")
searchfield = Entry(frame1)
searchbutton = Button(frame1, text="Suchen",height = 15)
resultscroller = Scrollbar(frame2)
resultlbl = Text(frame2, height=10, width=50)
resultlbl.insert(END, text)
resultscroller.config(command=resultlbl.yview)
resultlbl.config(yscrollcommand=resultscroller.set)

frame1.pack()
frame2.pack()

searchlbl.pack(side=LEFT, anchor=N, padx=5, pady=5)
searchfield.pack(side=LEFT, anchor=N, padx=5, pady=5)
searchbutton.pack(side=LEFT, padx=5, pady=5)
resultscroller.pack(side=RIGHT, fill=Y)

resultlbl.pack(side=LEFT, fill=Y)

top.mainloop()
