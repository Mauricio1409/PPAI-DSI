import tkinter
import subprocess
import ttkbootstrap as ttk

def RegistrarResultadoDeRevisionManual():
    ventana.destroy()
    subprocess.run(["python", "main.py"], check=True)

ventana = ttk.Window(themename="superhero")  # Usa un tema vistoso
ventana.title("Pantalla Principal")
ventana.geometry("500x300")  # Ventana más grande

frame = ttk.Frame(ventana, padding=40)
frame.pack(expand=True)

label = ttk.Label(frame, text="Bienvenido al Sistema", font=("Segoe UI", 20, "bold"))
label.pack(pady=(0, 30))

boton = ttk.Button(
    frame,
    text="Registrar Resultado de Revisión Manual",
    command=RegistrarResultadoDeRevisionManual,
    bootstyle="success",
    width=35,
    style="TButton"
)
boton.pack(pady=10)

ventana.mainloop()