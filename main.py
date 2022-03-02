import tkinter as tk

window = tk.Tk()
window.title("Calculadora")


def crear_botones():
    for i in range(4):
        for j in range(5):
            frame = tk.Frame(master=window, borderwidth=2)
            frame.grid(row=i, column=j)
            btn = tk.Button(text="A", width=20, height=10, master=frame)
            btn.pack()

crear_botones()
window.mainloop()
