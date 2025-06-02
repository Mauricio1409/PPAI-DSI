import ttkbootstrap as ttk
from tkinter import messagebox
from recursos.VentanaGif import VentanaGif  # Importá la ventana

from ManejadorNuevoEventoSismico import ManejadorNuevoEventoSismico

class VentanaPantNuevoEventoSismico(ttk.Window):
    def __init__(self):
        super().__init__()


        self.imagen = None
        self.modificoDatos = None
        self.punteroManejador = None
        self.bodyFrame = ttk.Frame(master=self)
        self.imgFrame = ttk.Frame(master=self.bodyFrame)
        self.inputFrame = ttk.Frame(master=self.bodyFrame)
        self.strMagnitud = ttk.StringVar()
        self.strAlcance = ttk.StringVar()
        self.strOrigenName = ttk.StringVar()
        self.strClasificacion = ttk.StringVar()
        self.lblImagenSismograma = ttk.Label(master=self.imgFrame)
        self.opcionElegida= ttk.StringVar()
        self.lblTituloCuadro = ttk.Label(master=self, text="Eventos Sísmicos Pendientes de Revisión:", font=("Arial", 20, "bold"))
        self.lblTitulo = ttk.Label(master=self, text="Visualización del evento seleccionado", font=("Arial", 30, "bold"))
        self.lblSeleccionarOpcion = ttk.Label(master=self, text="Seleccione una acción para el evento sismico seleccionado:", font=("Arial", 14, "bold"))
        self.selectorOpciones = ttk.Combobox(master=self, state="readonly", font=("Arial", 12), textvariable=self.opcionElegida, values=["Confirmar Evento", "Rechazar Evento", "Solicitar Revisión a Experto"])
        self.btnConfirmarOpcion = ttk.Button(master=self, text="Confirmar Opción", style='my.TButton', command= self.tomarOptGrilla)
        self.btnEditar = ttk.Button(master=self.inputFrame, text="Modificar Datos", style='my.TButton', command= lambda: self.seleccionarModificarDatos(True))
        self.btnVolver = ttk.Button(master=self, text="Volver", style='my.TButton', command=self.volverApantallaPrincipal)
        self.lblClasificacion = ttk.Label(master=self.inputFrame, text="Clasificación del Evento Sísmico: ", font=("Arial", 12))
        self.lblEdicion = ttk.Label(master=self.bodyFrame, text=f"Edición de datos del evento sismico Seleccionado", font=("Arial", 20, "bold"))
        self.lblTituloSismograma = ttk.Label(master=self.bodyFrame, text="Sismograma del Evento Sísmico",font=("Arial", 20, "bold"))
        self.lblOrigenName = ttk.Label(master=self.inputFrame, text=f"Nombre Origen: ", font=("Arial", 12))
        self.lblAlcance = ttk.Label(master=self.inputFrame, text=f"Alcance: ", font=("Arial", 12))
        self.lblMagnitud = ttk.Label(master=self.inputFrame, text=f"Magnitud:", font=("Arial", 12))
        self.lblTituloSismograma = ttk.Label(master=self.bodyFrame, text="Sismograma del Evento Sísmico", font=("Arial", 20, "bold"))
        self.inputMagnitud = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strMagnitud, state="readonly")
        self.inputAlcance = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strAlcance, state="readonly")
        self.inputOrigenName = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strOrigenName, state="readonly")
        self.lblClasificacionActual = ttk.Label(master=self.inputFrame, textvariable=self.strClasificacion, font=("Arial", 12, "bold"))
        self.style.theme_use("darkly")
        self.title("Nuevo Evento Sísmico")
        self.geometry("1600x900")

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
        self.button_reg_rev_manual = ttk.Button(master=self.buttons_frame, text="Revisión Manual", style='my.TButton', command=self.opcionRegistrarRevisionManual) #comand # FALTA COMMAND

        self.cuadro = None
        self.scrollbar = None

        # ESTILOS

        # Packing inicial

        self.buttons_frame.pack()
        
    def opcionRegistrarRevisionManual(self):
        self.habilitarVentana()
        self.punteroManejador = ManejadorNuevoEventoSismico(punteroPantalla=self)
        self.punteroManejador.registrarNuevaRevision()

    def habilitarVentana(self):
        self.lblTituloCuadro.pack()

    def presentarEventosNoRevisados(self, arrayDatos):
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

        #for i in range(len(arrayFechaHoras)):
            # Agregar los elementos a la tabla
        #    self.cuadro.insert("", "end", text=arrayFechaHoras[i], values=(arrayUbicaciones[i][0][0], arrayUbicaciones[i][0][1],arrayUbicaciones[i][1][0],arrayUbicaciones[i][1][1], arrayMagnitudes[i]))

        for datosEvento in arrayDatos:
            self.cuadro.insert("", "end", 
                               text=datosEvento['fechaHoraOcurrencia'], 
                               values=(datosEvento['ubicacion'][0][0], 
                                       datosEvento['ubicacion'][0][1],
                                       datosEvento['ubicacion'][1][0],
                                       datosEvento['ubicacion'][1][1],
                                       datosEvento['valorMagnitud']))

        self.cuadro.pack(fill="both", expand=True)
        self.frame_cuadro.pack(fill="both", expand=True)
        self.frame_superior_cuadro.place(relx=0.5, rely=0.4, relwidth=0.9, relheight=0.6, anchor="center")

        # Event Listeners
        self.cuadro.bind("<Return>", self.seleccionaEventoSismico)
        self.cuadro.bind("<Double-1>", self.seleccionaEventoSismico)

    def seleccionaEventoSismico(self, event):
        seleccion = self.cuadro.selection()
        if seleccion is not None:
            item_id = seleccion[0]
            index = self.cuadro.index(item_id)
            self.punteroManejador.eventoSismicoSeleccionado(index)

    def mostrarOpcionMapa(self):
        respuesta = messagebox.askquestion("Visualizar Mapa", "¿Desea visualizar el mapa?")

        if respuesta == "yes":
            gif_path = "recursos/sismo.gif"
            ventana = VentanaGif(gif_path)
            ventana.grab_set()  # bloquea la ventana principal si querés
        elif respuesta == "no":
            self.seleccionarNoVisualizar()

    def seleccionarNoVisualizar(self):
        self.punteroManejador.noVisualizarSeleccionado()

# region HABILITAR EDICION DE DATOS
    def habilitarEdicionDatos(self):
        self.lblTituloCuadro.pack_forget()
        self.cuadro.pack_forget()
        self.frame_cuadro.pack_forget()
        self.frame_superior_cuadro.place_forget()
        self.scrollbar.pack_forget()

        self.lblTitulo.pack()
        self.lblEdicion.grid(row=0, column=0, padx=10, pady=10)
        self.btnEditar.grid(row=4, column=1, padx=10, pady=10)
        #self.bodyFrame.pack(fill="x", expand=True, padx=150)
        self.bodyFrame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6, anchor="center")
        self.inputFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        #self.inputFrame.place(relx=0.5, rely=0.5, anchor='center')
        
    def habilitarEdicionMagnitud(self, magnitud):
        self.strMagnitud.set(magnitud)
        self.lblMagnitud.grid(row=1, column=0, padx=10, pady=10)
        self.inputMagnitud.grid(row=1, column=1, padx=10, pady=10)

    def habilitarEdicionAlcance(self, alcance):
        self.strAlcance.set(alcance)
        self.lblAlcance.grid(row=2, column=0, padx=10, pady=10)
        self.inputAlcance.grid(row=2, column=1, padx=10, pady=10)

    def habilitarEdicionOrigen(self, origen):
        self.strOrigenName.set(origen)
        self.lblOrigenName.grid(row=3, column=0, padx=10, pady=10)
        self.inputOrigenName.grid(row=3, column=1, padx=10, pady=10)
# endregion
    def habilitarSelectorOpciones(self):
        self.lblSeleccionarOpcion.place(relx=0.5, rely=0.75, anchor='center')
        self.opcionElegida.set("Elija una opción")
        self.selectorOpciones.place(relx=0.49, rely=0.8, anchor='e')
        self.btnConfirmarOpcion.place(relx=0.51, rely=0.8, anchor='w')

    def seleccionarModificarDatos(self, modifico):
        self.modificoDatos = modifico
        # Habilitar los campos de entrada para editar
        self.inputAlcance.config(state="normal")
        self.inputMagnitud.config(state="normal")
        self.inputOrigenName.config(state="normal")

    def mostrarDetallesEvento(self, clasifciacion, rutaSismograma):
        self.strClasificacion.set(clasifciacion)
        self.lblClasificacion.grid(row=0, column=0, padx=10, pady=10)
        self.lblClasificacionActual.grid(row=0, column=1, padx=10, pady=10)

        print(rutaSismograma)
        self.imagen = ttk.PhotoImage(file=rutaSismograma)


        self.lblTituloSismograma.grid(row=0, column=1, padx=10, pady=10)
        self.lblImagenSismograma.config(image=self.imagen)
        self.lblImagenSismograma.pack()
        self.imgFrame.grid(row=1, column=1, padx=10, pady=10, sticky="ne")





    def tomarOptGrilla(self):
        opcionElegida = self.selectorOpciones.get()
        if opcionElegida == "Elija una opción":
            messagebox.showwarning("Advertencia", "Por favor, seleccione una acción válida.")
            return
        self.punteroManejador.tomarOptGrilla(opcionElegida, self.strAlcance.get(), self.strMagnitud.get(), self.strOrigenName.get(), self.modificoDatos)

#################################################################################################################
    def habilitarBotonVolver(self):
        self.btnVolver.place(relx=0.8, rely=0.8, anchor='center')

    def volverApantallaPrincipal(self):
        self.lblEdicion.pack_forget()
        self.inputFrame.place_forget()
        self.selectorOpciones.place_forget()
        self.btnConfirmarOpcion.place_forget()
        self.btnVolver.place_forget()
        self.punteroManejador.registrarNuevaRevision()
        self.lblTitulo.pack_forget()
        self.lblSeleccionarOpcion.place_forget()
        self.bodyFrame.place_forget()

    