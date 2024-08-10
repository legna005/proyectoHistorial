from calendar import LocaleHTMLCalendar
import tkinter as tk 
from tkinter import *
from tkinter import Button, ttk, scrolledtext,Toplevel,StringVar,LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion,listar,editarDatoPaciente,eliminarPaciente
from modelo.HistoriaMedicaDao import historiaMedica,guardarHistoria,listarHistoria,eliminarHistorial,editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime,date

class Frame(tk.Frame):
    def __init__(self,root):

        super().__init__(root,width=1280, height=720)
        self.root=root
        self.pack()
        self.config(bg="#CDD8FF")
        self.idPersonaHistoria=None
        self.idPersona=None
        self.idHistoriaMedica=None
        self.idHistoriaMedicaEditar=None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()
        
        
#estos son las letras que aparecen a lado de las casillas de texto
    def camposPaciente(self):
        self.lblNombre=tk.Label(self,text="Nombre: ")
        self.lblNombre.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)
        
        self.lblApePaterno=tk.Label(self,text="Apellido Paterno: ")
        self.lblApePaterno.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblApePaterno.grid(column=0, row=1, padx=10, pady=5)

        self.lblApeMaterno=tk.Label(self,text="Apellido Materno: ")
        self.lblApeMaterno.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblApeMaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblDni=tk.Label(self,text="DNI: ")
        self.lblDni.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblDni.grid(column=0, row=3, padx=10, pady=5)

        self.lblFechNacimiento=tk.Label(self,text="Fecha de nacimiento: ")
        self.lblFechNacimiento.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblFechNacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lblEdad=tk.Label(self,text="Edad: ")
        self.lblEdad.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblEdad.grid(column=0, row=5, padx=10, pady=5)

        self.lblAntecedentes=tk.Label(self,text="Antecedentes: ")
        self.lblAntecedentes.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblAntecedentes.grid(column=0, row=6, padx=10, pady=5)

        self.lblCorreo=tk.Label(self,text="Correo: ")
        self.lblCorreo.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblCorreo.grid(column=0, row=7, padx=10, pady=5)

        self.lblTelefono=tk.Label(self,text="Telefono: ")
        self.lblTelefono.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblTelefono.grid(column=0, row=8, padx=10, pady=5)

        #entrys son las tablas de texto

        self.svNombre=tk.StringVar()
        self.entryNombre=tk.Entry(self,textvariable=self.svNombre)
        self.entryNombre.config(width=50,font=("ARIAL",15))
        self.entryNombre.grid(column=1,row=0, padx=10,pady=5,columnspan=2)

        self.svApePaterno=tk.StringVar()
        self.entryApePaterno=tk.Entry(self,textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50,font=("ARIAL",15))
        self.entryApePaterno.grid(column=1,row=1, padx=10,pady=5,columnspan=2)

        self.svApeMaterno=tk.StringVar()
        self.entryApeMaterno=tk.Entry(self,textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50,font=("ARIAL",15))
        self.entryApeMaterno.grid(column=1,row=2, padx=10,pady=5,columnspan=2)

        self.svDni=tk.StringVar()
        self.entryDni=tk.Entry(self,textvariable=self.svDni)
        self.entryDni.config(width=50,font=("ARIAL",15))
        self.entryDni.grid(column=1,row=3, padx=10,pady=5,columnspan=2)

        self.svFecNacimiento=tk.StringVar()
        self.entryFecNacimiento=tk.Entry(self,textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50,font=("ARIAL",15))
        self.entryFecNacimiento.grid(column=1,row=4, padx=10,pady=5,columnspan=2)

        self.svEdad=tk.StringVar()
        self.entryEdad=tk.Entry(self,textvariable=self.svEdad)
        self.entryEdad.config(width=50,font=("ARIAL",15))
        self.entryEdad.grid(column=1,row=5, padx=10,pady=5,columnspan=2)

        self.svAntecedentes=tk.StringVar()
        self.entryAntecedentes=tk.Entry(self,textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50,font=("ARIAL",15))
        self.entryAntecedentes.grid(column=1,row=6, padx=10,pady=5,columnspan=2)

        self.svCorreo=tk.StringVar()
        self.entryCorreo=tk.Entry(self,textvariable=self.svCorreo)
        self.entryCorreo.config(width=50,font=("ARIAL",15))
        self.entryCorreo.grid(column=1,row=7, padx=10,pady=5,columnspan=2)

        self.svTelefono=tk.StringVar()
        self.entryTelefono=tk.Entry(self,textvariable=self.svTelefono)
        self.entryTelefono.config(width=50,font=("ARIAL",15))
        self.entryTelefono.grid(column=1,row=8, padx=10,pady=5,columnspan=2)

        #los hermosos botones pa

        self.btnNuevo=tk.Button(self, text="Nuevo",command=self.habilitar)
        self.btnNuevo.config(width=20, font=("ARIAL",12,"bold"),fg="#DAD5D6",bg="#158645",cursor="hand2",activebackground="#35BD6F")
        self.btnNuevo.grid(column=0,row=9,padx=10,pady=5)

        self.btnGuardar=tk.Button(self, text="Guardar",command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=("ARIAL",12,"bold"),fg="#DAD5D6",bg="#000000",cursor="hand2",activebackground="#5F5F5F")
        self.btnGuardar.grid(column=1,row=9,padx=10,pady=5)

        self.btnCancelar=tk.Button(self, text="Cancelar",command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=("ARIAL",12,"bold"),fg="#DAD5D6",bg="#B00000",cursor="hand2",activebackground="#D27C7C")
        self.btnCancelar.grid(column=2,row=9,padx=10,pady=5)

        #BUSCADOR LABEL BUSCADOR
        self.lblbuscarDni=tk.Label(self, text='Buscar Dni')
        self.lblbuscarDni.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblbuscarDni.grid(column=3,row=0,padx=10,pady=5)

        self.lblbuscarApellido=tk.Label(self, text='Buscar Apellido')
        self.lblbuscarApellido.config(font=("ARIAL",15,"bold"),bg="#CDD8FF")
        self.lblbuscarApellido.grid(column=3,row=1,padx=10,pady=5)

        #Entry buscador
        self.svBuscarDni=tk.StringVar()
        self.entryBuscarDni=tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20,font=("ARIAL",15))
        self.entryBuscarDni.grid(column=4,row=0, padx=10,pady=5,columnspan=2)

        self.svBuscarApellido=tk.StringVar()
        self.entryBuscarApellido=tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20,font=("ARIAL",15))
        self.entryBuscarApellido.grid(column=4,row=1, padx=10,pady=5,columnspan=2)

        #boton buscar

        self.btnBuscarCondicion=tk.Button(self, text="Buscar",command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#170095',activebackground='#9379E0',cursor='hand2')
        self.btnBuscarCondicion.grid(column=3,row=2,padx=10,pady=5,columnspan=1) 

        self.btnLimpiarBuscador=tk.Button(self, text="Limpiar",command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#120061',activebackground='#7C6DC1',cursor='hand2')
        self.btnLimpiarBuscador.grid(column=4,row=2,padx=10,pady=5,columnspan=1)

        #boton calendario
        self.btnCalendario=tk.Button(self, text="Calendario",command=self.vistaCalendario)
        self.btnCalendario.config(width=12,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#120061',activebackground='#7C6DC1',cursor='hand2')
        self.btnCalendario.grid(column=3,row=4,padx=10,pady=5,columnspan=1)

    
    def vistaCalendario(self):
        self.calendario=Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar(value="01/01/1990")
        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1990, month=1, day=1,locale ='es_US',bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE',textvariable=self.svCalendario,cursor = 'hand2', date_pattern='dd/mm/Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column=0)
        #fecha,
        self.svCalendario.trace('w',self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFecNacimiento.set(''+self.svCalendario.get())

        if len(self.calendar.get_date())>1:
            self.svCalendario.trace('w',self.calcularEdad)


    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d/%m/%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)


    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where='WHERE 1=1'
            if(len(self.svBuscarDni.get())) > 0:
                where="WHERE dni="+self.svBuscarDni.get()+""#Where dni=12
            if(len(self.svBuscarApellido.get()))>0:
                where="WHERE apellidoPaterno LIKE'"+self.svBuscarApellido.get()+"%' AND activo=1"

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(),
            self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(), self.svAntecedentes.get(),
            self.svCorreo.get(), self.svTelefono.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        self.deshabilitar()
        self.tablaPaciente()
        self.calendario.destroy()
        
    def habilitar(self):
         
         self.svNombre.set('')
         self.svApePaterno.set('')
         self.svApeMaterno.set('')
         self.svDni.set('')
         self.svFecNacimiento.set('')
         self.svEdad.set('')
         self.svAntecedentes.set('')
         self.svCorreo.set('')
         self.svTelefono.set('')
         
         self.entryNombre.config(state='normal')
         self.entryApePaterno.config(state='normal')
         self.entryApeMaterno.config(state='normal')
         self.entryDni.config(state='normal')
         self.entryFecNacimiento.config(state='normal')
         self.entryEdad.config(state='normal')
         self.entryAntecedentes.config(state='normal')
         self.entryCorreo.config(state='normal')
         self.entryTelefono.config(state='normal')

         self.btnGuardar.config(state='normal')
         self.btnCancelar.config(state='normal')
         self.btnCalendario.config(state='normal')


    def deshabilitar(self):
        self.idPersona=None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        
        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFecNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'APaterno', 'AMaterno','Dni','FNacimiento','Edad','Antecedentes','Correo','Telefono'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Ap. Paterno')
        self.tabla.heading('#3',text='Ap. Materno')
        self.tabla.heading('#4',text='Dni')
        self.tabla.heading('#5',text='F. Nacimiento')
        self.tabla.heading('#6',text='Edad')
        self.tabla.heading('#7',text='Antecedentes')
        self.tabla.heading('#8',text='Correo')
        self.tabla.heading('#9',text='Telefono')

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=300)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=82)

        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow',))

        self.btnEditarPaciente=tk.Button(self,text='Editar paciente',command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#170095',activebackground='#9379E0',cursor='hand2')
        self.btnEditarPaciente.grid(row=11,column=0,padx=10,pady=5)

        self.btnEliminarPaciente=tk.Button(self,text='Eliminar paciente',command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#8A0000',activebackground='#D58A8A',cursor='hand2')
        self.btnEliminarPaciente.grid(row=11,column=1,padx=10,pady=5)

        self.btnHistorialPaciente=tk.Button(self,text='Historial paciente',command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#007C79',activebackground='#99F2F0',cursor='hand2')
        self.btnHistorialPaciente.grid(row=11,column=2,padx=10,pady=5)

        self.btnSalir=tk.Button(self,text='Salir',command=self.root.destroy)
        self.btnSalir.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#000000',activebackground='#5E5E5E',cursor='hand2')
        self.btnSalir.grid(row=11,column=4,padx=10,pady=5)

    def historiaMedica(self):
        try:
            if self.idPersona==None:
                self.idPersona=self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria=self.tabla.item(self.tabla.selection())['text']
            if(self.idPersona>0):
                idPersona=self.idPersona
                
            self.topHistoriaMedica=Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.config(bg='#CDD8FF')

            self.listaHistoria=listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, columns=('Apellidos', 'fechaHistoria', 'temperaturaCorporal', 'pulso', 'frecuenciaRespiratoria', 'presionArterial', 'peso', 'altura', 'imc'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=10,sticky='nse')

            self.scrollHistoria=ttk.Scrollbar(self.topHistoriaMedica,orient='vertical',command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0,column=10,sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0',text='ID')
            self.tablaHistoria.heading('#1',text='Apellidos')
            self.tablaHistoria.heading('#2',text='Fecha y Hora')
            self.tablaHistoria.heading('#3',text='temperatura corporal')
            self.tablaHistoria.heading('#4',text='Pulso')
            self.tablaHistoria.heading('#5',text='frecuencia respiratoria')
            self.tablaHistoria.heading('#6',text='presion arterial')
            self.tablaHistoria.heading('#7',text='peso')
            self.tablaHistoria.heading('#8',text='altura')
            self.tablaHistoria.heading('#9',text='imc')

            self.tablaHistoria.column('#0',anchor=W,width=50)
            self.tablaHistoria.column('#1',anchor=W,width=100)
            self.tablaHistoria.column('#2',anchor=W,width=100)
            self.tablaHistoria.column('#3',anchor=W,width=120)
            self.tablaHistoria.column('#4',anchor=W,width=250)
            self.tablaHistoria.column('#5',anchor=W,width=150)
            self.tablaHistoria.column('#6',anchor=W,width=50)
            self.tablaHistoria.column('#7',anchor=W,width=50)
            self.tablaHistoria.column('#8',anchor=W,width=150)
            self.tablaHistoria.column('#9',anchor=W,width=150)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0,text=p[0],values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]))
            
            self.btnGuardarHistoria=tk.Button(self.topHistoriaMedica, text='Agregar Historia',command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#002771',cursor='hand2',activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2,column=0,padx=10,pady=5)

            self.btnEditarHistoria=tk.Button(self.topHistoriaMedica, text='Editar Historia',command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#3A005D',cursor='hand2',activebackground='#B47CD6')
            self.btnEditarHistoria.grid(row=2,column=1,padx=10,pady=5)

            self.btnEliminarHistoria=tk.Button(self.topHistoriaMedica, text='Eliminar Historia',command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#890011',cursor='hand2',activebackground='#DB939C')
            self.btnEliminarHistoria.grid(row=2,column=2,padx=10,pady=5)

            self.btnCerrarHistoria=tk.Button(self.topHistoriaMedica, text='Cerrar Historia',command=self.salirTop)
            self.btnCerrarHistoria.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#000000',cursor='hand2',activebackground='#6F6F6F')
            self.btnCerrarHistoria.grid(row=2,column=3,padx=10,pady=5)
        except:
            title='Historia medica'
            mensaje='Error al mostrar historial'
            messagebox.showerror(title,mensaje)

    def topAgregarHistoria(self):
        self.topAHistoria=Toplevel()
        self.topAHistoria.title('Agregar Historia')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg='#CDD8FF')

        self.frameDatosHistoria=tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill="both",expand="yes",pady=10,padx=20)

        #LABELS AGREGAR HISTORIA MEDICA
        
        self.lblSignosVitalesHistoria=tk.Label(self.frameDatosHistoria,text='Signos vitales:',width=20,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblSignosVitalesHistoria.grid(row=1,column=0,padx=5,pady=3)
    
        self.lbltemperaturaCorporalHistoria=tk.Label(self.frameDatosHistoria,text='Temperatura Corporal',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lbltemperaturaCorporalHistoria.grid(row=2,column=0,padx=5,pady=3)

        self.lblpulsoHistoria=tk.Label(self.frameDatosHistoria,text='Pulso',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblpulsoHistoria.grid(row=3,column=0,padx=5,pady=3)

        self.lblfrecuenciaRespiratoriaHistoria=tk.Label(self.frameDatosHistoria,text='Frecuencia respiratoria',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblfrecuenciaRespiratoriaHistoria.grid(row=4,column=0,padx=5,pady=3)

        self.lblpresionArterialHistoria=tk.Label(self.frameDatosHistoria,text='Presion arterial',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblpresionArterialHistoria.grid(row=5,column=0,padx=5,pady=3)

        self.lblpesoHistoria=tk.Label(self.frameDatosHistoria,text='Peso',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblpesoHistoria.grid(row=6,column=0,padx=5,pady=3)

        self.lblalturaHistoria=tk.Label(self.frameDatosHistoria,text='Altura',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblalturaHistoria.grid(row=7,column=0,padx=5,pady=3)

        self.lblimcHistoria=tk.Label(self.frameDatosHistoria,text='Imc',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblimcHistoria.grid(row=8,column=0,padx=5,pady=3)

        self.lblParametrosHistoria=tk.Label(self.frameDatosHistoria,text='Parámetros',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblParametrosHistoria.grid(row=1,column=3,padx=5,pady=3)

        self.lblPTemperaturaHistoria=tk.Label(self.frameDatosHistoria,text='36.5°C - 37.3°C',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblPTemperaturaHistoria.grid(row=2,column=3,padx=5,pady=3)

        self.lblPPulsoHistoria=tk.Label(self.frameDatosHistoria,text='60 - 100 latidos',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblPPulsoHistoria.grid(row=3,column=3,padx=5,pady=3)

        self.lblPFrecuenciarespiratoriaHistoria=tk.Label(self.frameDatosHistoria,text='12 - 18 respiraciones x min.',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblPFrecuenciarespiratoriaHistoria.grid(row=4,column=3,padx=5,pady=3)

        self.lblPPresionarterial=tk.Label(self.frameDatosHistoria,text='60 - 100 latidos x min.',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
        self.lblPPresionarterial.grid(row=5,column=3,padx=5,pady=3)

        #ENTRYS AGREGAR HISTORIA MEDICA
        self.svTemperaturaCorporalHistoria=tk.StringVar()
        self.TemperaturaCorporalHistoria=tk.Entry(self.frameDatosHistoria,textvariable=self.svTemperaturaCorporalHistoria)
        self.TemperaturaCorporalHistoria.config(width=15,font=('ARIAL',15))
        self.TemperaturaCorporalHistoria.grid(row=2,column=1,padx=5,pady=3,columnspan=2)

        self.svPulsoHistoria=tk.StringVar()
        self.PulsoHistoria=tk.Entry(self.frameDatosHistoria,textvariable=self.svPulsoHistoria)
        self.PulsoHistoria.config(width=15,font=('ARIAL',15))
        self.PulsoHistoria.grid(row=3,column=1,padx=5,pady=3,columnspan=2)

        self.svFrecuenciaRespiratoriaHistoria=tk.StringVar()
        self.FrecuenciaRespiratoriaHistoria=tk.Entry(self.frameDatosHistoria,textvariable=self.svFrecuenciaRespiratoriaHistoria)
        self.FrecuenciaRespiratoriaHistoria.config(width=15,font=('ARIAL',15))
        self.FrecuenciaRespiratoriaHistoria.grid(row=4,column=1,padx=5,pady=3,columnspan=2)

        self.svPresionArterialHistoria=tk.StringVar()
        self.PresionArterialHistoria=tk.Entry(self.frameDatosHistoria,textvariable=self.svPresionArterialHistoria)
        self.PresionArterialHistoria.config(width=15,font=('ARIAL',15))
        self.PresionArterialHistoria.grid(row=5,column=1,padx=5,pady=3,columnspan=2)

        self.svPesoHistorial=tk.StringVar()
        self.PesoHistorial=tk.Entry(self.frameDatosHistoria,textvariable=self.svPesoHistorial)
        self.PesoHistorial.config(width=15,font=('ARIAL',15))
        self.PesoHistorial.grid(row=6,column=1,padx=5,pady=3,columnspan=2)

        self.svAlturaHistorial=tk.StringVar()
        self.AlturaHistorial=tk.Entry(self.frameDatosHistoria,textvariable=self.svAlturaHistorial)
        self.AlturaHistorial.config(width=15,font=('ARIAL',15))
        self.AlturaHistorial.grid(row=7,column=1,padx=5,pady=3,columnspan=2)

        self.svImcHistorial=tk.StringVar()
        self.TemperaturaHistorial=tk.Entry(self.frameDatosHistoria,textvariable=self.svImcHistorial)
        self.TemperaturaHistorial.config(width=15,font=('ARIAL',15))
        self.TemperaturaHistorial.grid(row=8,column=1,padx=5,pady=3,columnspan=2)

        self.frameFechaHistoria=tk.Label(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both",expand="yes",padx=20,pady=10)

        self.svFechaHistoria=tk.StringVar()
        self.entryFechaHistoria=tk.Entry(self.frameFechaHistoria,textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=15,font=('ARIAL',15))
        self.entryFechaHistoria.grid(row=1,column=1,padx=5,pady=3)

        self.lblfechaHistoria=tk.Label(self.frameFechaHistoria,text='fecha y hora',width=15,font=('ARIAL',15),bg='#CDD8FF')
        self.lblfechaHistoria.grid(row=1,column=0,padx=3,pady=3)

        self.svFechaHistoria.set(datetime.today().strftime('%d/%m/%Y %H:%M'))

        self.btnImcHistoria=tk.Button(self.frameFechaHistoria,text='Calcular Imc',command=self.calcularIMC)
        self.btnImcHistoria.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000992',cursor='hand2',activebackground='#4E56C6')
        self.btnImcHistoria.grid(row=2,column=1,padx=9,pady=5)

        self.btnGuardarHistoria=tk.Button(self.frameFechaHistoria,text='Guardar Historia',command=self.guardarHistorialMedico)
        self.btnGuardarHistoria.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000992',cursor='hand2',activebackground='#4E56C6')
        self.btnGuardarHistoria.grid(row=2,column=0,padx=9,pady=5)

        self.btnSalirAgregarHistoria=tk.Button(self.frameFechaHistoria,text='Salir',command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000000',cursor='hand2',activebackground='#646464')
        self.btnSalirAgregarHistoria.grid(row=2,column=3,padx=10,pady=5)

        
    def guardarHistorialMedico(self):
        try:
            if self.idHistoriaMedica==None:
                guardarHistoria(self.idPersonaHistoria,self.svFechaHistoria.get(),self.svTemperaturaCorporalHistoria.get(),self.svPulsoHistoria.get(),self.svFrecuenciaRespiratoriaHistoria.get(),self.svPresionArterialHistoria.get(),self.svPesoHistorial.get(),self.svAlturaHistorial.get(),self.svImcHistorial.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title='Agregar Historia'
            mensaje='Error al agregar historia medica'
            messagebox.showerror(title,mensaje)

    def eliminarHistorialMedico(self):
        try:
             self.idHistoriaMedica=self.tablaHistoria.item(self.tablaHistoria.selection())['text']
             eliminarHistorial(self.idHistoriaMedica)
             self.idHistoriaMedica=None
             self.topHistoriaMedica.destroy()
        except:
             title='Eliminar historia'
             mensaje='Error al eliminar'
             messagebox.showerror(title,mensaje)

    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica=self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.TemperaturaCorporalEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.PulsoEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.FrecuenciaRespiratoriaEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.PresionArterialEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]
            self.PesoEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][6]
            self.AlturaEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][7]
            self.ImcEditar=self.tablaHistoria.item(self.tablaHistoria.selection())['values'][8]

            self.topEditarHistoria=Toplevel()
            self.topEditarHistoria.title('Editar historia medica')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.config(bg='#CDD8FF')

            self.frameEditarHistoria=tk.Label(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#CDD8FF')
            self.frameEditarHistoria.pack(fill="both",expand="yes",padx=20,pady=10)

            #label
            self.lblSignosVitalesHistoriaEditar=tk.Label(self.frameEditarHistoria,text='Signos vitales:',width=20,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblSignosVitalesHistoriaEditar.grid(row=1,column=0,padx=5,pady=3)
    
            self.lblTemperaturaCorporalEditar=tk.Label(self.frameEditarHistoria,text='Temperatura Corporal',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblTemperaturaCorporalEditar.grid(row=2,column=0,padx=5,pady=3)

            self.lblPulsoEditar=tk.Label(self.frameEditarHistoria,text='Pulso',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblPulsoEditar.grid(row=3,column=0,padx=5,pady=3)

            self.lblFrecuenciaRespiratoriaEditar=tk.Label(self.frameEditarHistoria,text='Frecuencia respiratoria',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblFrecuenciaRespiratoriaEditar.grid(row=4,column=0,padx=5,pady=3)

            self.lblPresionArterialEditar=tk.Label(self.frameEditarHistoria,text='Presion arterial',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblPresionArterialEditar.grid(row=5,column=0,padx=5,pady=3)

            self.lblPesoEditar=tk.Label(self.frameEditarHistoria,text='Peso',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblPesoEditar.grid(row=6,column=0,padx=5,pady=3)

            self.lblAlturaEditar=tk.Label(self.frameEditarHistoria,text='Altura',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblAlturaEditar.grid(row=7,column=0,padx=5,pady=3)

            self.lblImcEditar=tk.Label(self.frameEditarHistoria,text='Imc',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblImcEditar.grid(row=8,column=0,padx=5,pady=3)

            self.lblParametrosHistoria=tk.Label(self.frameEditarHistoria,text='Parámetros',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblParametrosHistoria.grid(row=1,column=3,padx=5,pady=3)

            self.lblPTemperaturaHistoria=tk.Label(self.frameEditarHistoria,text='36.5°C - 37.3°C',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblPTemperaturaHistoria.grid(row=2,column=3,padx=5,pady=3)

            self.lblPPulsoHistoria=tk.Label(self.frameEditarHistoria,text='60 - 100 latidos',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblPPulsoHistoria.grid(row=3,column=3,padx=5,pady=3)

            self.lblPFrecuenciarespiratoriaHistoria=tk.Label(self.frameEditarHistoria,text='12 - 18 respiraciones x min.',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblPFrecuenciarespiratoriaHistoria.grid(row=4,column=3,padx=5,pady=3)

            self.lblPPresionarterial=tk.Label(self.frameEditarHistoria,text='60 - 100 latidos x min.',width=21,font=('ARIAL',15,'bold'),bg='#8AF334')
            self.lblPPresionarterial.grid(row=5,column=3,padx=5,pady=3)

            self.svTemperaturaCorporalEditar=tk.StringVar()
            self.entryTemperaturaCorporalEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svTemperaturaCorporalEditar)
            self.entryTemperaturaCorporalEditar.config(width=20,font=('ARIAL',15))
            self.entryTemperaturaCorporalEditar.grid(row=2,column=1,pady=3,padx=5,columnspan=2)

            self.svPulsoEditar=tk.StringVar()
            self.entryPulsoEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svPulsoEditar)
            self.entryPulsoEditar.config(width=20,font=('ARIAL',15))
            self.entryPulsoEditar.grid(row=3,column=1,pady=3,padx=5,columnspan=2)

            self.svFrecuenciaRespiratoriaEditar=tk.StringVar()
            self.entryFrecuenciaRespiratoriaEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svFrecuenciaRespiratoriaEditar)
            self.entryFrecuenciaRespiratoriaEditar.config(width=20,font=('ARIAL',15))
            self.entryFrecuenciaRespiratoriaEditar.grid(row=4,column=1,pady=3,padx=5,columnspan=2)

            self.svPresionArterialEditar=tk.StringVar()
            self.entryPresionArterialEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svPresionArterialEditar)
            self.entryPresionArterialEditar.config(width=20,font=('ARIAL',15))
            self.entryPresionArterialEditar.grid(row=5,column=1,pady=3,padx=5,columnspan=2)

            self.svPesoEditar=tk.StringVar()
            self.entryPesoEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svPesoEditar)
            self.entryPesoEditar.config(width=20,font=('ARIAL',15))
            self.entryPesoEditar.grid(row=6,column=1,pady=3,padx=5,columnspan=2)

            self.svAlturaEditar=tk.StringVar()
            self.entryAlturaEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svAlturaEditar)
            self.entryAlturaEditar.config(width=20,font=('ARIAL',15))
            self.entryAlturaEditar.grid(row=7,column=1,pady=3,padx=5,columnspan=2)

            self.svImcEditar=tk.StringVar()
            self.entryImcEditar=tk.Entry(self.frameEditarHistoria,textvariable=self.svImcEditar)
            self.entryImcEditar.config(width=20,font=('ARIAL',15))
            self.entryImcEditar.grid(row=8,column=1,pady=3,padx=5,columnspan=2)

            self.framefechaEditar=tk.LabelFrame(self.topEditarHistoria)
            self.framefechaEditar.config(bg='#CDD8FF')
            self.framefechaEditar.pack(fill="both",expand="yes",padx=20,pady=10)

            self.lblfechaHistoriaEditar=tk.Label(self.framefechaEditar,text='Fecha y hora',width=20,font=('ARIAL',15,'bold'),bg='#CDD8FF')
            self.lblfechaHistoriaEditar.grid(row=1,column=0,padx=3,pady=5)


            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.framefechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=('ARIAL', 15))
            self.entryFechaHistoriaEditar.grid(row = 1, column=1, pady=3, padx=5)

            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)
            self.entryTemperaturaCorporalEditar.insert(0,self.TemperaturaCorporalEditar)
            self.entryPulsoEditar.insert(0,self.PulsoEditar)
            self.entryFrecuenciaRespiratoriaEditar.insert(0,self.FrecuenciaRespiratoriaEditar)
            self.entryPresionArterialEditar.insert(0,self.PresionArterialEditar)
            self.entryPesoEditar.insert(0,self.PesoEditar)
            self.entryAlturaEditar.insert(0,self.AlturaEditar)
            self.entryImcEditar.insert(0,self.ImcEditar)
            
            self.btnEditarHistoriaMedica=tk.Button(self.framefechaEditar,text='Editar historia',command=self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#030058',cursor='hand2',activebackground='#8986DA')
            self.btnEditarHistoriaMedica.grid(row=2,column=0,padx=10,pady=5)

            self.btnSalirEditarHistoriaMedica=tk.Button(self.framefechaEditar,text='Salir',command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000000',cursor='hand2',activebackground='#676767')
            self.btnSalirEditarHistoriaMedica.grid(row=2,column=3,padx=10,pady=5)

            self.btncalcularImcEditarHistoriaMedica=tk.Button(self.framefechaEditar,text='Calcular imc',command=self.calcularIMCEditar)
            self.btncalcularImcEditarHistoriaMedica.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000992',cursor='hand2',activebackground='#4E56C6')
            self.btncalcularImcEditarHistoriaMedica.grid(row=1,column=3,padx=10,pady=5)

            if self.idHistoriaMedicaEditar==None:
                self.idHistoriaMedicaEditar=self.idHistoriaMedica
            self.idHistoriaMedica=None

        except:
            title='Editar historia'
            mensaje='Error al editar historia'
            messagebox.showerror(title,mensaje)
            

    def calcularIMCEditar(self):
      try:
        peso = float(self.svPesoEditar.get())
        altura = float(self.svAlturaEditar.get())
        imc = peso / (altura ** 2)
        self.svImcEditar.set(f"{imc:.2f}")
        
        if imc < 18.5:
            messagebox.showinfo("Recomendación", "Peso bajo:  Sería bueno que comas un poco más, incluyendo alimentos nutritivos como frutas, nueces, y pan integral. Además, trata de hacer algo de ejercicio para ganar fuerza, como levantar pequeñas pesas o hacer ejercicios en casa.")
        elif 18.5 <= imc < 24.9:
            messagebox.showinfo("Recomendación", "Peso normal: Estás en un buen camino! Sigue comiendo equilibrado, incluyendo frutas, verduras, proteínas, y carbohidratos. Mantente activo con ejercicios que disfrutes, como caminar, nadar, o montar en bici. Así mantendrás tu salud en buen estado.")
        elif 25 <= imc < 29.9:
            messagebox.showinfo("Recomendación", "Peso medio (sobrepeso):  Estás bien, pero hay un pequeño margen para mejorar. Intenta ajustar un poco tus porciones y elegir opciones más saludables cuando puedas. Un poco más de ejercicio te ayudará a sentirte aún mejor y mantenerte en forma.")
        else:
            messagebox.showinfo("Recomendación", "Peso alto (obesidad): Tu peso está un poco alto. Intenta comer de manera más equilibrada y agrega un poco más de actividad física a tu rutina diaria. Esto te ayudará a sentirte mejor y a mantener un peso más saludable.")
        
      except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el peso y la altura.")     

        
    def calcularIMC(self):
      try:
        peso = float(self.svPesoHistorial.get())
        altura = float(self.svAlturaHistorial.get())
        imc = peso / (altura ** 2)
        self.svImcHistorial.set(f"{imc:.2f}")
        
        if imc < 18.5:
            messagebox.showinfo("Recomendación", "Peso bajo:  Sería bueno que comas un poco más, incluyendo alimentos nutritivos como frutas, nueces, y pan integral. Además, trata de hacer algo de ejercicio para ganar fuerza, como levantar pequeñas pesas o hacer ejercicios en casa.")
        elif 18.5 <= imc < 24.9:
            messagebox.showinfo("Recomendación", "Peso normal: Estás en un buen camino! Sigue comiendo equilibrado, incluyendo frutas, verduras, proteínas, y carbohidratos. Mantente activo con ejercicios que disfrutes, como caminar, nadar, o montar en bici. Así mantendrás tu salud en buen estado.")
        elif 25 <= imc < 29.9:
            messagebox.showinfo("Recomendación", "Peso medio (sobrepeso):  Estás bien, pero hay un pequeño margen para mejorar. Intenta ajustar un poco tus porciones y elegir opciones más saludables cuando puedas. Un poco más de ejercicio te ayudará a sentirte aún mejor y mantenerte en forma.")
        else:
            messagebox.showinfo("Recomendación", "Peso alto (obesidad): Tu peso está un poco alto. Intenta comer de manera más equilibrada y agrega un poco más de actividad física a tu rutina diaria. Esto te ayudará a sentirte mejor y a mantener un peso más saludable.")
        
      except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el peso y la altura.")

    
        


    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(),self.svTemperaturaCorporalEditar.get(),self.svPulsoEditar.get(),self.svFrecuenciaRespiratoriaEditar.get(),self.svPresionArterialEditar.get(),self.svPesoEditar.get(),self.svAlturaEditar.get(),self.svImcEditar.get(),self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar=None
            self.idHistoriaMedica=None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title='Editar historia'
            mensaje='Error al editar historia'
            messagebox.showinfo(title,mensaje)
            self.topEditarHistoria.destroy()

        





        


    def salirTop(self):
        self.topHistoriaMedica.destroy()


        
            
    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFecNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryAntecedentes.insert(0,self.antecedentesPaciente)
            self.entryCorreo.insert(0,self.correoPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)

            self.entryNombre.config(state='disabled')
            self.entryApePaterno.config(state='disabled')
            self.entryApeMaterno.config(state='disabled')
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona=self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)

            self.tablaPaciente()
            self.idPersona=None
        except:
            title='Eliminar Paciente'
            mensaje='No se pudo eliminar el paciente'
            messagebox.showerror(title,mensaje)

    