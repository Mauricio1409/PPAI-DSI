import ttkbootstrap as ttk
#from tkinter import simpledialog, messagebox
from ManejadorNuevoEventoSismico import ManejadorNuevoEventoSismico


class VentanaPantNuevoEventoSismico(ttk.Window):


    def seleccionaEventoSismico(self, event):
        seleccion = self.cuadro.selection()
        if seleccion:
            item_id = seleccion[0]
            index = self.cuadro.index(item_id)
            self.punteroManejador.eventoSismicoSeleccionado(index)

    def habilitar_ventana(self):
        #self.button_reg_rev_manual.pack()
        pass
        

    def opcion_registrar_revision_manual(self):
        self.habilitar_ventana()
        self.punteroManejador = ManejadorNuevoEventoSismico(punteroPantalla=self)
        self.punteroManejador.registrarNuevaRevision()

    def presentarEventosNoRevisados(self, arrayFechaHoras, arrayUbicaciones, arrayMagnitudes):
        # Crear la tabla

        #region CUADRO
        self.style.configure('Treeview', rowheight=30)
        self.cuadro = ttk.Treeview(master=self.frame_cuadro, columns=("col1", "col2", "col3", "col4", "col5"))
        self.cuadro.column("#0")
        self.cuadro.column("col1")
        self.cuadro.column("col2")
        self.cuadro.column("col3")
        self.cuadro.column("col4")
        self.cuadro.column("col5")

        self.cuadro.heading("#0", text="Fecha Hora Ocurrencia", anchor='center')
        self.cuadro.heading("col1", text="Latitud Epicentro", anchor='center')
        self.cuadro.heading("col2", text="Longitud Epicentro", anchor='center')
        self.cuadro.heading("col3", text="Latitud Hipocentro", anchor='center')
        self.cuadro.heading("col4", text="Longitud Hipocentro", anchor='center')
        self.cuadro.heading("col5", text="Magnitud", anchor='center')

        self.cuadro.column("#0", anchor="center")
        self.cuadro.column("col1", anchor="center")
        self.cuadro.column("col2", anchor="center")
        self.cuadro.column("col3", anchor="center")
        self.cuadro.column("col4", anchor="center")
        self.cuadro.column("col5", anchor="center")
        #endregion

        #region SCROLLBAR
        # Crear el scrollbar

        self.scrollbar = ttk.Scrollbar(self.frame_cuadro, orient="vertical", command=self.cuadro.yview)
        self.scrollbar.pack(side="right", fill="y")

        style_scroll = ttk.Style()
        style_scroll.configure("Vertical.TScrollbar", troughcolor="white")
        #endregion


        self.cuadro.delete(*self.cuadro.get_children())  # Limpiar el cuadro antes de agregar nuevos elementos

        for i in range(len(arrayFechaHoras)):
            # Agregar los elementos a la tabla
            self.cuadro.insert("", "end", text=arrayFechaHoras[i], values=(arrayUbicaciones[i][0][0], arrayUbicaciones[i][0][1],arrayUbicaciones[i][1][0],arrayUbicaciones[i][1][1], arrayMagnitudes[i]))

        self.cuadro.pack(fill="both", expand=True)
        self.frame_cuadro.pack(fill="both", expand=True)
        self.frame_superior_cuadro.place(relx=0.5, rely=0.4, relwidth=0.9, relheight=0.6, anchor="center")

        # Event Listeners
        self.cuadro.bind("<Return>", self.seleccionaEventoSismico)
        self.cuadro.bind("<Double-1>", self.seleccionaEventoSismico)

    def __init__(self):
        super().__init__()
        self.punteroManejador = None
        self.style.theme_use("journal")
        self.title("Nuevo Evento Sísmico")
        self.geometry("800x600")

        #para estetica (añadir icono a la app)

        #self.icon_path = "path/to/icon.ico"  # Cambia esto a la ruta de tu icono
        #self.img = Image.open(self.icon_path)
        #self.icon = ImageTk.PhotoImage(self.img)
        #self.wm_iconphoto(False, self.icon)

        # FRAMES 

            # frame de botones es como un div de HTML
        self.buttons_frame = ttk.Frame(master=self)
        self.frame_superior_cuadro = ttk.Frame(master=self)
        self.frame_cuadro = ttk.Frame(master=self.frame_superior_cuadro)
        

        # BOTONES Y OTROS ELEMENTOS

        # Estilo de los botones        # boton, como button de HTML
        self.button_reg_rev_manual = ttk.Button(master=self.buttons_frame, text="Revisión Manual", style='my.TButton', command=self.opcion_registrar_revision_manual) #comand # FALTA COMMAND

        self.cuadro = None
        self.scrollbar = None

        # ESTILOS

        # Packing inicial

        self.buttons_frame.pack()