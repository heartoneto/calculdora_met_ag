import tkinter as tk


class Calc:
    def __init__(self):
        # Crear la ventana
        self.window = tk.Tk()
        self.window.title("Calculadora")
        self.window.geometry("264x372")

        # Equacion a evaluar
        self.equation = tk.StringVar()
        self.expression = ""
        self.expression_field = tk.Entry(self.window, textvariable=self.equation)
        self.expression_field.grid(columnspan=4)

    # Cuando se presiona cualquier boton de número u operador
    def press(self, num):
        # global expression
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    # Cuando se presiona el boton de =

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)

            self.expression = ""
        except:
            self.equation.set("error")
            self.expression = ""

    # Cuando se presiona el boton de limpiar

    def clearfield(self):
        global expression
        self.expression = ""
        self.equation.set("")

    # Crear los botonoes y asociarlos a su controlador de eventos
    def crear_botones(self):
        button1 = tk.Button(self.window, text=' 1 ', fg='black',
                            command=lambda: self.press(1), height=4, width=8)
        button1.grid(row=2, column=0)

        button2 = tk.Button(self.window, text=' 2 ', fg='black',
                            command=lambda: self.press(2), height=4, width=8)
        button2.grid(row=2, column=1)

        button3 = tk.Button(self.window, text=' 3 ', fg='black',
                            command=lambda: self.press(3), height=4, width=8)
        button3.grid(row=2, column=2)

        button4 = tk.Button(self.window, text=' 4 ', fg='black',
                            command=lambda: self.press(4), height=4, width=8)
        button4.grid(row=3, column=0)

        button5 = tk.Button(self.window, text=' 5 ', fg='black',
                            command=lambda: self.press(5), height=4, width=8)
        button5.grid(row=3, column=1)

        button6 = tk.Button(self.window, text=' 6 ', fg='black',
                            command=lambda: self.press(6), height=4, width=8)
        button6.grid(row=3, column=2)

        button7 = tk.Button(self.window, text=' 7 ', fg='black',
                            command=lambda: self.press(7), height=4, width=8)
        button7.grid(row=4, column=0)

        button8 = tk. Button(self.window, text=' 8 ', fg='black',
                             command=lambda: self.press(8), height=4, width=8)
        button8.grid(row=4, column=1)

        button9 = tk.Button(self.window, text=' 9 ', fg='black',
                            command=lambda: self.press(9), height=4, width=8)
        button9.grid(row=4, column=2)

        button0 = tk.Button(self.window, text=' 0 ', fg='black',
                            command=lambda: self.press(0), height=4, width=8)
        button0.grid(row=5, column=0)

        plus = tk.Button(self.window, text=' + ', fg='black',
                         command=lambda: self.press("+"), height=4, width=8)
        plus.grid(row=2, column=3)

        minus = tk.Button(self.window, text=' - ', fg='black',
                          command=lambda: self.press("-"), height=4, width=8)
        minus.grid(row=3, column=3)

        multiply = tk.Button(self.window, text=' * ', fg='black',
                             command=lambda: self.press("*"), height=4, width=8)
        multiply.grid(row=4, column=3)

        divide = tk.Button(self.window, text=' / ', fg='black',
                           command=lambda: self.press("/"), height=4, width=8)
        divide.grid(row=5, column=3)

        point = tk.Button(self.window, text=' . ', fg='black',
                          command=lambda: self.press('.'), height=4, width=8)
        point.grid(row=5, column=2)

        clear = tk.Button(self.window, text='Clear', fg='black',
                          command=self.clearfield, height=4, width=8)
        clear.grid(row=5, column='1')

        equal = tk.Button(self.window, text=' = ', fg='black',
                          command=self.equalpress, height=4, width=8)
        equal.grid(row=6, column=0, columnspan=4)

    def run(self):
        # Creat los botones
        self.crear_botones()
        # ciclo de eventos
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calc()
    calc.run()
