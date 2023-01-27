import tkinter as tk

from funcion import comparacion

window = tk.Tk()
window.title("Piedra, Papel o Tijera")
window.geometry("400x300")
window.configure(bg="SlateGray1")

hello = tk.Label(text="\n¡BIENVENIDO A PIEDRA, PAPEL O TIJERA!\n\n¿PODRAS VENCERME?\n\nELIJE!\n\n",font="helvetica",bg="SlateGray1")
hello.pack()

def comparacion_piedra():
  resultado=comparacion("PIEDRA")
  etiqueta["text"]=resultado
  

def comparacion_papel():
  resultado=comparacion("PAPEL")
  etiqueta["text"]=resultado
  
def comparacion_tijera():
  resultado=comparacion("TIJERA")
  etiqueta["text"]=resultado


button = tk.Button(text="PIEDRA",font="italic",command=comparacion_piedra)
button.pack()
e1=tk.Label(text=" ",bg="SlateGray1")
e1.pack()
button1 = tk.Button(text="PAPEL",font="italic",command=comparacion_papel)
button1.pack()
e2=tk.Label(text=" ",bg="SlateGray1")
e2.pack()
button2 = tk.Button(text="TIJERA",font="italic",command=comparacion_tijera)
button2.pack()


etiqueta= tk.Label(text="",font="italic",fg="red",bg="SlateGray1")
etiqueta.pack()

tk.mainloop()