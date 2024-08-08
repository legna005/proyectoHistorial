from.conexion import ConexionDB
from tkinter import messagebox


def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}',
            apellidoMaterno = '{persona.apellidoMaterno}', dni = '{persona.dni}', fechaNacimiento = '{persona.fechaNacimiento}',
            edad = {persona.edad}, antecedentes = '{persona.antecedentes}', correo = '{persona.correo}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showinfo(title, mensaje)

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno,
          dni, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES
          ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}',
          {persona.dni},'{persona.fechaNacimiento}',{persona.edad},'{persona.antecedentes}',
          '{persona.correo}','{persona.telefono}',1)"""
    #este try es para agregar pacientes
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title='Registrar paciente'
        mensaje='Paciente registrado exitosamente'
        messagebox.showinfo(title,mensaje)

    except: 
        title='registrar paciente'
        mensaje='error al registrar paciente'
        messagebox.showerror(title,mensaje)  

#este es para ver el servidor
def listar():
    conexion=ConexionDB()

    listaPersona=[]
    sql='SELECT * FROM Persona WHERE activo=1'

    try:
       conexion.cursor.execute(sql)
       listaPersona=conexion.cursor.fetchall()
       conexion.cerrarConexion()
    except: 
        title='Datos'
        mensaje='registro no existen'
        messagebox.showwarning(title,mensaje)
    return listaPersona

#aqui para ver el registro
def listarCondicion(where):
    conexion=ConexionDB()
    listaPersona=ConexionDB()
    listaPersona=[]
    sql=f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona=conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except: 
        title='Datos'
        mensaje='registro no existe'
        messagebox.showwarning(title,mensaje)
    return listaPersona

#y aqui para eliminar pacientes
def eliminarPaciente(idPersona):
    conexion=ConexionDB()
    sql=f"""UPDATE Persona SET activo=0 WHERE idPersona= {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title='Eliminar Paciente'
        mensaje='Paciente Eliminado Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title='Eliminar Paciente'
        mensaje='Error al eliminar paciente'
        messagebox.showwarning(title,mensaje)


class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, antecedentes, correo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo 
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno},{self.apellidoMaterno},{self.dni},{self.fechaNacimiento},{self.edad},{self.antecedentes},{self.correo},{self.telefono}]'