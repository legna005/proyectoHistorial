from.conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion=ConexionDB()
    listaHistoria=[]
    sql=f'SELECT  h.idHistoriaMedica, p.nombre || " " || p.apellidoPaterno || " "||p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.temperaturaCorporal, h.pulso, h.frecuenciaRespiratoria, h.presionArterial, h.peso, h.altura, h.imc FROM historiaMedica h INNER JOIN Persona p ON p.idPersona=h.idPersona WHERE p.idPersona={idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)

    return listaHistoria

def guardarHistoria(idPersona,fechaHistoria,temperaturaCorporal,pulso,frecuenciaRespiratoria,presionArterial,peso,altura,imc):
    conexion=ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona,fechaHistoria,temperaturaCorporal , pulso,
          frecuenciaRespiratoria, presionArterial, peso, altura, imc ) VALUES
          ({idPersona},'{fechaHistoria}','{temperaturaCorporal}',{pulso},'{frecuenciaRespiratoria}',{presionArterial},'{peso}','{altura}','{imc}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Medica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Medica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)

class historiaMedica:
    def _init_(self,idPersona,fechaHistoria,temperaturaCorporal,pulso,frecuenciaRespiratoria,presionArterial,peso,altura,imc):
        self.idHistoriaMedica=None
        self.idPersona=idPersona
        self.fechaHistoria=fechaHistoria
        self.temperaturaCorporal=temperaturaCorporal
        self.pulso=pulso
        self.frecuenciaRespiratoria=frecuenciaRespiratoria
        self.presionArterial=presionArterial
        self.peso=peso
        self.altura=altura
        self.imc=imc

    def _str_(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.temperaturaCorporal},{self.pulso},{self.frecuenciaRespiratoria},{self.presionArterial},{self.peso},{self.altura},{self.imc}]'