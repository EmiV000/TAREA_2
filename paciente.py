class Paciente:
    _secuencia = 0
    def __init__(self, nombre, apellido, fecha_nac, edad, genero, tipo_san, telefono, direccion, diagnostico):
        Paciente._secuencia += 1
        self.__hc = Paciente._secuencia
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = fecha_nac
        self.edad = edad
        self.genero = genero
        self.sangre = tipo_san
        self.telefono = telefono
        self.direccion = direccion
        self.diagnostico = diagnostico
        
    @property
    def hc(self):
        return self.__hc
    
    def mostrarPaciente(self):
        print("Paciente: ", '\n', "H.C.", self.hc, "-", self.nombre, self.apellido)
        print( self.genero, "-", self.edad, "Años")
        print("F. Nacimiento:", self.nacimiento,  " - " , "Tipo de Sangre:", self.sangre)
        print("Telefono:", self.telefono,   "  Direccion:", self.direccion)
        print("Diagnostico: ", self.diagnostico)
        
if __name__ == '__main__':
    paciente1 = Paciente("Francisco", "Mera Gomez", "12/04/2018", 4, "Masculino", "O+", "0988667243", "Bucay", "Gripe")
    paciente1.mostrarPaciente()