from tkinter import *


def click(event):
    global scavalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scavalue.get().isdigit():
            value = int(scavalue.get())
        else:
            value = eval(screen.get())

        scavalue.set(value)
        screen.update()

    elif text == "C":
        scavalue.set("")
        screen.update()

    else:
        scavalue.set(scavalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("Calculator By Divjot Singh")
scavalue = StringVar()
scavalue.set("")
screen = Entry(root, textvar=scavalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=15, pady=3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="8", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="7", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=15, pady=3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="5", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="4", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=15, pady=3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="2", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="1", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=15, pady=3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="-", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="*", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

f = Frame(root, bg="grey")
b = Button(f, text="/", padx=15, pady=3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)


fss = Frame(root, bg="grey")
bss = Button(f, text="C", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)


fss = Frame(root, bg="grey")
bss = Button(f, text="=", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="%", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

fss = Frame(root, bg="grey")
bss = Button(f, text="+", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)
root.mainloop()

fss = Frame(root, bg="grey")
bss = Button(f, text="%", padx=15, pady=3, font="lucida 35 bold")
fss.pack()
bss.pack(side=LEFT, padx=18, pady=5)
bss.bind("<Button-1>", click)

root.mainloop()

