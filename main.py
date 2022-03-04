import tkinter as tk

# Crear la ventana
window = tk.Tk()
window.title("Calculadora")
window.geometry("264x372")

# Equacion a evaluar
equation = tk.StringVar()
expression = ""
expression_field = tk.Entry(window, textvariable=equation)
expression_field.grid(columnspan=4)

# Cuando se presiona cualquier boton de número u operador
def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)


# Cuando se presiona el boton de =
def equalpress():

    try:
        global expression

        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("error")
        expression = ""


# Cuando se presiona el boton de limpiar
def clearfield():
    global expression
    expression = ""
    equation.set("")

# Crear los botonoes y asociarlos a su controlador de eventos
def crear_botones():
    button1 = tk.Button(window, text=' 1 ', fg='black',
                        command=lambda: press(1), height=4, width=8)
    button1.grid(row=2, column=0)

    button2 = tk.Button(window, text=' 2 ', fg='black',
                        command=lambda: press(2), height=4, width=8)
    button2.grid(row=2, column=1)

    button3 = tk.Button(window, text=' 3 ', fg='black',
                        command=lambda: press(3), height=4, width=8)
    button3.grid(row=2, column=2)

    button4 = tk.Button(window, text=' 4 ', fg='black',
                        command=lambda: press(4), height=4, width=8)
    button4.grid(row=3, column=0)

    button5 = tk.Button(window, text=' 5 ', fg='black',
                        command=lambda: press(5), height=4, width=8)
    button5.grid(row=3, column=1)

    button6 = tk.Button(window, text=' 6 ', fg='black',
                        command=lambda: press(6), height=4, width=8)
    button6.grid(row=3, column=2)

    button7 = tk.Button(window, text=' 7 ', fg='black',
                        command=lambda: press(7), height=4, width=8)
    button7.grid(row=4, column=0)

    button8 = tk. Button(window, text=' 8 ', fg='black',
                         command=lambda: press(8), height=4, width=8)
    button8.grid(row=4, column=1)

    button9 = tk.Button(window, text=' 9 ', fg='black',
                        command=lambda: press(9), height=4, width=8)
    button9.grid(row=4, column=2)

    button0 = tk.Button(window, text=' 0 ', fg='black',
                        command=lambda: press(0), height=4, width=8)
    button0.grid(row=5, column=0)

    plus = tk.Button(window, text=' + ', fg='black',
                     command=lambda: press("+"), height=4, width=8)
    plus.grid(row=2, column=3)

    minus = tk.Button(window, text=' - ', fg='black',
                      command=lambda: press("-"), height=4, width=8)
    minus.grid(row=3, column=3)

    multiply = tk.Button(window, text=' * ', fg='black',
                         command=lambda: press("*"), height=4, width=8)
    multiply.grid(row=4, column=3)

    divide = tk.Button(window, text=' / ', fg='black',
                       command=lambda: press("/"), height=4, width=8)
    divide.grid(row=5, column=3)

    point = tk.Button(window, text=' . ', fg='black',
                      command=lambda: press('.'), height=4, width=8)
    point.grid(row=5, column=2)

    clear = tk.Button(window, text='Clear', fg='black',
                      command=clearfield, height=4, width=8)
    clear.grid(row=5, column='1')

    equal = tk.Button(window, text=' = ', fg='black',
                      command=equalpress, height=4, width=8)
    equal.grid(row=6, column=0, columnspan=4)


# Creat los botones
crear_botones()
# ciclo de eventos
window.mainloop()
