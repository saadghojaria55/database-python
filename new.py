v = StringVar()

e = Entry(master, textvariable=v)
e.pack()

v.set("a default value")
s = v.get()
