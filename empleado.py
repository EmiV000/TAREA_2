from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre, apellido, cedula, telefono, email, direccion, horario):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.horario = horario
        
        @abstractmethod
        def mostrarEmpleado(self):
            pass
        
class Medico(Empleado):
    def __init__(self, nombre, apellido, cedula, especialidad, telefono, email, direccion, horario):
        super().__init__(nombre, apellido, cedula, telefono, email, direccion, horario)
        self.especialidad = especialidad
        
    def mostrarEmpleado(self): 
        print("Medico.", self.especialidad,  self.nombre, self.apellido)
        print("C.I.", self.cedula)
        print("Contacto:", self.telefono, " - ", self.email)
        print("Direccion: ", self.direccion)
        print("Horario:" , self.horario)
        
            
                
class Enfermera(Empleado):
    def __init__(self, nombre, apellido, cedula, area, telefono, email, direccion, horario):
        super().__init__(nombre, apellido, cedula,  telefono, email, direccion, horario)
        self.area = area
        
    def mostrarEmpleado(self):
        print(self.nombre, self.apellido)
        print("C.I.", self.cedula)
        print("Area:", self.area)
        print("Contacto:", self.telefono , "-" , self.email)
        print("Direccion: ", self.direccion)
        print("Horario:" , self.horario)


if __name__ == '__main__':
    print("---------Empleados--------")       
    medico1 = Medico("Luis", "Gonzales Perez","0908754326", "Pediatra", "0974297563", "luisgp@hotmail.com", "Bucay", "Matutino")       
    enfermera1 = Enfermera("Estela", "Ruiz Correa", "0693784623", "Hospitalizacion", "0978397654", "estelarc@hotmail.com", "Bucay", "Vespertino")
    medico1.mostrarEmpleado()
    enfermera1.mostrarEmpleado()