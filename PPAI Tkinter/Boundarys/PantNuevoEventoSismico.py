import ttkbootstrap as ttk
from tkinter import messagebox
from recursos.VentanaGif import VentanaGif  # Importá la ventana

from ManejadorNuevoEventoSismico import ManejadorNuevoEventoSismico

class VentanaPantNuevoEventoSismico(ttk.Window):
    def __init__(self):
        super().__init__()
        self.punteroManejador = None
        self.inputFrame = ttk.Frame(master=self)
        self.strMagnitud = ttk.StringVar()
        self.strAlcance = ttk.StringVar()
        self.strOrigenDesc = ttk.StringVar()
        self.strOrigenName = ttk.StringVar()
        self.selectorOpciones = ttk.Combobox(master=self, state="readonly", font=("Arial", 12), values=["Confirmar Evento", "Rechazar Evento", "Solicitar Revisión a Experto"])
        self.btnConfirmarOpcion = ttk.Button(master=self, text="Confirmar Opción", style='my.TButton', command= self.tomarOptGrilla)
        self.btnEditar = ttk.Button(master=self.inputFrame, text="Modificar Datos", style='my.TButton', command= lambda: print("editar")) #TODO añadir funciones
        self.btnCancelar = ttk.Button(master=self.inputFrame, text="No Modificar", style='my.TButton', command= lambda: print("cancelar")) #TODO añadir funciones
        self.btnVolver = ttk.Button(master=self, text="Volver", style='my.TButton', command=self.volverApantallaPrincipal) #TODO añadir funciones
        self.lblEdicion = ttk.Label(master=self, text=f"Edición de Datos del evento sismico Seleccionado", font=("Arial", 20))
        self.lblOrigenDesc = ttk.Label(master=self.inputFrame, text=f"Descripción Origen: ", font=("Arial", 12))
        self.lblOrigenNom = ttk.Label(master=self.inputFrame, text=f"Nombre Origen: ", font=("Arial", 12))
        self.lblAlcance = ttk.Label(master=self.inputFrame, text=f"Alcance: ", font=("Arial", 12))
        self.lblMagnitud = ttk.Label(master=self.inputFrame, text=f"Magnitud:", font=("Arial", 12))
        self.inputMagnitud = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strMagnitud)
        self.inputAlcance = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strAlcance)
        self.inputOrigenDesc = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strOrigenDesc)
        self.inputOrigenName = ttk.Entry(master=self.inputFrame, font=("Arial", 12), textvariable=self.strOrigenName)
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
        #self.button_reg_rev_manual.pack()
        pass

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
            self.punteroManejador.noVisualizarSeleccionado()

    def seleccionarNoVisualizar(self):
        pass

    def habilitarEdicionDatos(self, alcance, origen, magnitud):
        self.cuadro.pack_forget()
        self.frame_cuadro.pack_forget()
        self.frame_superior_cuadro.place_forget()
        self.scrollbar.pack_forget()
        
        self.lblEdicion.pack(pady=10)
        self.habilitarEdicionMagnitud(magnitud)
        self.habilitarEdicionOrigen(origen)
        self.habilitarEdicionAlcance(alcance)
        self.btnEditar.grid(row=4, column=0, padx=10, pady=10)
        self.btnCancelar.grid(row=4, column=1, padx=10, pady=10)
        self.inputFrame.place(relx=0.5, rely=0.5, anchor='center')
        
    def habilitarEdicionMagnitud(self, magnitud):
        self.strMagnitud.set(magnitud)
        self.lblMagnitud.grid(row=0, column=0, padx=10, pady=10)
        self.inputMagnitud.grid(row=0, column=1, padx=10, pady=10)

    def habilitarEdicionAlcance(self, alcance):
        self.strAlcance.set(alcance)
        self.lblAlcance.grid(row=1, column=0, padx=10, pady=10)
        self.inputAlcance.grid(row=1, column=1, padx=10, pady=10)

    def habilitarEdicionOrigen(self, origen):
        self.strOrigenDesc.set(origen["descripcion"])
        self.strOrigenName.set(origen["nombre"])
        self.lblOrigenDesc.grid(row=2, column=0,padx=10, pady=10)
        self.lblOrigenNom.grid(row=3, column=0,padx=10, pady=10)
        self.inputOrigenDesc.grid(row=2, column=1, padx=10, pady=10)
        self.inputOrigenName.grid(row=3, column=1, padx=10, pady=10)

    def habilitarSelectorOpciones(self):
        self.selectorOpciones.pack()
        self.btnConfirmarOpcion.place(relx=0.5, rely=0.8, anchor='center')
        
    def seleccionarModificarDatos(self): #TODO TENGO DUDAS SERIAS SOBRE ESTO, CHEQUEAR DIAGRAMA
        pass

    def solicitarSeleccionOpciones(self): 
        pass

    def tomarOptGrilla(self):
        self.punteroManejador.tomarOptGrilla(self.selectorOpciones.get())

#################################################################################################################
    def habilitarBotonVolver(self):
        self.btnVolver.place(relx=0.8, rely=0.8, anchor='center')

    def volverApantallaPrincipal(self):
        self.lblEdicion.pack_forget()
        self.inputFrame.place_forget()
        self.selectorOpciones.pack_forget()
        self.btnConfirmarOpcion.place_forget()
        self.btnVolver.place_forget()
        self.punteroManejador.registrarNuevaRevision()

    