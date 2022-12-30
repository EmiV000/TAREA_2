from datetime import datetime,date
from sistema import Sistema
from empleado import Medico, Enfermera
from paciente import Paciente

class Medicamento:
    _secuencia=0
    def __init__(self,nombre,precio,stock):
        Medicamento._secuencia += 1
        self.__codigo = Medicamento._secuencia
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrarMedicamento(self):
        print(self.codigo,self.nombre)
        
        
class DetalleReceta:
    def __init__(self, medicamento, cantidad, indicacion):
        self.medicamento = medicamento
        self.cantidad = cantidad
        self.indicacion = indicacion
        self.precio = medicamento.precio
        
class Receta:
    _numero=0
    _iva=0.12
    def __init__(self, medico, paciente):
        Receta._numero = Receta._numero + 1
        self.numero = str(Receta._numero)
        self.fecha = date.today()
        self.medico = medico
        self.paciente = paciente
        self.subtotal = 0
        self.iva = 0 
        self.total = 0
        self.detalleReceta = []
    
    def agregarReceta(self, medicamento, cantidad, indicacion):
        detalle = DetalleReceta(medicamento, cantidad, indicacion)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*Receta._iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleReceta.append(detalle)    
    
    def mostrarReceta(self, sisNombre, sisDireccion, sisTelefono):
        print("___________________________________________________________")
        print(">>>>>         Sistema Medico: {:17}       <<<<<".format(sisNombre))  
        print("          Direccion: {:10} ".format(sisDireccion))  
        print(">>>>>               Tel.: {:10}                 <<<<<".format(sisTelefono))
        print("___________________________________________________________")
        print("Receta #: {:13}                  Fecha:  {}".format(self.numero, self.fecha))
        self.medico.mostrarEmpleado()
        print("___________________________________________________________")
        self.paciente.mostrarPaciente()
        print("___________________________________________________________")
        print("Codigo Medicamento Cantidad   Indicacion    Precio Subtotal")
        for det in self.detalleReceta:
            print("{:5}  {:} {:5}     {:10} {:7} {:5}".format(det.medicamento.codigo,det.medicamento.nombre,det.cantidad,det.indicacion,det.precio,det.precio*det.cantidad))  
        print("_"*39,"Subtotal=> ",self.subtotal)
        print("_"*44,"Iva=>  ",self.iva)
        print("_"*42,"Total=> ",self.total)    

sistema = Sistema()
medico1 = Medico("Luis", "Gonzales Perez","0908754326", "Pediatra", "0974297563", "luisgp@hotmail.com", "Bucay", "Matutino")        
enfermera1 = Enfermera("Estela", "Ruiz Correa", "0693784623", "Hospitalizacion", "0978397654", "estelarc@hotmail.com", "Bucay", "Vespertino")
paciente1 = Paciente("Francisco", "Mera Gomez", "12/04/2018", 4, "Masculino", "O+", "0988667243", "Bucay", "Gripe")
med1 = Medicamento("Paracetamol", 1, 170)
med2 = Medicamento("Azitromicina", 1, 150)
med3 = Medicamento("Loratadina", 1, 100)
receta = Receta(medico1, paciente1)
receta.agregarReceta(med1, 10, "Cada 8 horas")
receta.agregarReceta(med2, 10, "1 diaria")
receta.agregarReceta(med3, 10, "Cada 6 horas")
receta.mostrarReceta(sistema.nombre, sistema.direccion, sistema.telefono)