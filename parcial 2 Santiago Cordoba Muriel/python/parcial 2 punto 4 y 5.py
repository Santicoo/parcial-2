from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
def ZeroDivisionError():
    messagebox.showerror("Error: La division no se puede realizar")
    
    
def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = ""

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":

             resultado = num1 / num2  # Se debe manejar la división por cero
        # Falta implementar potencia aquí
        elif operacion == "potencia":
            if num2 !=0:
             resultado = num1  ** num2
            else:
              ZeroDivisionError()
        label_resultado.config(text="Resultado: " + str(resultado))
   
   
   
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        ZeroDivisionError()

# Configuración de la interfaz gráfica
root = Tk()
root.title("Calculadora")
label_num1 = Label(root, text="Número 1:")
label_num1.pack()
entry_num1 = Entry(root)
entry_num1.pack()

label_num2 = Label(root, text="Número 2:")
label_num2.pack()
entry_num2 = Entry(root)
entry_num2.pack()

label_resultado = Label(root, text="Resultado:")
label_resultado.pack()

boton_suma = Button(root, text="potencia", command=lambda: realizar_operacion("potencia"))
boton_suma.pack()

boton_suma = Button(root, text="Sumar", command=lambda: realizar_operacion("suma"))
boton_suma.pack()

boton_resta = Button(root, text="Restar", command=lambda: realizar_operacion("resta"))
boton_resta.pack()

boton_multiplicacion = Button(root, text="Multiplicar", command=lambda: realizar_operacion("multiplicacion"))
boton_multiplicacion.pack()

boton_division = Button(root, text="Dividir", command=lambda: realizar_operacion("division"))
boton_division.pack()

# Aquí se deben agregar botones para la nueva operación de potencia
root.mainloop()
