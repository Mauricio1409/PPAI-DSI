import tkinter as tk
import subprocess
import ttkbootstrap as ttk

USUARIO = "Juan Pérez"  # Cambia esto por el nombre del usuario logueado

def RegistrarResultadoDeRevisionManual():
    ventana.destroy()
    subprocess.run(["python", "main.py"], check=True)

ventana = ttk.Window(themename="superhero")
ventana.title("Sistema de Sismos - Analista")
ventana.geometry("800x500")
ventana.minsize(600, 400)

# Barra superior simulando header web
header = ttk.Frame(ventana, bootstyle="dark", padding=(10, 5))
header.pack(side="top", fill="x")

# Logo ficticio
logo = tk.Canvas(header, width=40, height=40, bg="#2d3e50", highlightthickness=0)
logo.pack(side="left", padx=(0, 10))
logo.create_rectangle(5, 5, 35, 35, fill="#2980b9", outline="#2980b9")
logo.create_text(20, 20, text="SS", fill="white", font=("Segoe UI", 16, "bold"))

# Título del sistema
titulo = ttk.Label(header, text="Sistema de Sismos", font=("Segoe UI", 16, "bold"), bootstyle="inverse-dark")
titulo.pack(side="left", padx=(0, 20))

# Espaciador
header_spacer = ttk.Label(header, text="")
header_spacer.pack(side="left", expand=True)

# Ícono de usuario y nombre
user_icon = tk.Canvas(header, width=30, height=30, bg="#2d3e50", highlightthickness=0)
user_icon.pack(side="left", padx=(0, 5))
user_icon.create_oval(5, 5, 25, 25, fill="#f5d6b4", outline="#b89b72")
user_icon.create_oval(10, 17, 20, 27, fill="#3a5a99", outline="#2a3a59")
user_label = ttk.Label(header, text=USUARIO, font=("Segoe UI", 12), bootstyle="inverse-dark")
user_label.pack(side="left", padx=(0, 10))

# Frame principal
frame = ttk.Frame(ventana, padding=20)
frame.pack(expand=True, fill="both")

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# Dibujo de Analista (círculo con corbata)
canvas = tk.Canvas(frame, width=80, height=120, bg="white", highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=2, padx=(0, 20), pady=10, sticky="n")
canvas.create_oval(20, 10, 60, 50, fill="#f5d6b4", outline="#b89b72")
canvas.create_rectangle(30, 50, 50, 100, fill="#3a5a99", outline="#2a3a59")
canvas.create_polygon(40, 60, 40, 80, 45, 90, 50, 80, 50, 60, fill="#e74c3c", outline="#c0392b")

# Etiqueta de bienvenida
label = ttk.Label(frame, text="Bienvenido Analista", font=("Segoe UI", 18, "bold"))
label.grid(row=0, column=1, sticky="w", pady=(10, 0))

# Dibujo de sismógrafo y ondas sísmicas
canvas_sismo = tk.Canvas(frame, width=350, height=100, bg="white", highlightthickness=1, highlightbackground="#bbb")
canvas_sismo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
canvas_sismo.create_rectangle(10, 80, 340, 95, fill="#888")
canvas_sismo.create_rectangle(160, 30, 190, 80, fill="#444")
canvas_sismo.create_line(175, 30, 175, 10, width=3, fill="#222")
canvas_sismo.create_oval(170, 5, 180, 15, fill="#e74c3c", outline="#c0392b")
points = [
    (20, 90), (40, 70), (60, 90), (80, 60), (100, 90), (120, 80), (140, 90),
    (160, 60), (180, 90), (200, 70), (220, 90), (240, 60), (260, 90), (280, 80), (300, 90), (320, 70), (340, 90)
]
for i in range(len(points)-1):
    canvas_sismo.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="#e67e22", width=2)

# Botón de acción
boton = ttk.Button(
    frame,
    text="Registrar Resultado de Revisión Manual",
    command=RegistrarResultadoDeRevisionManual,
    bootstyle="success",
    width=35,
    style="TButton"
)
boton.grid(row=2, column=0, columnspan=2, pady=(30, 10), sticky="ew")

ventana.mainloop()