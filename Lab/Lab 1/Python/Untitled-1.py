from tkinter import *

root = Tk()
root.title("Погода Симферопль")
root.geometry('230x250')

the_label1 = Label(root, text="Симферопль", bg="yellow", fg="black")
the_label1.pack(fill = X)

the_label2 = Label(root, bg="yellow", fg="black")
the_label2.pack(fill = X)

the_label3 = Label(root, bg="white", fg="black", font=("Arial Bold", 40))
the_label3.pack(fill = X)

the_label4 = Label(root, bg="yellow")
the_label4.pack(fill = X)

the_label1.grid(row = 0)
the_label2.grid(row = 1)
the_label3.grid(row = 2)
the_label4.grid(row = 3)
root.mainloop()
