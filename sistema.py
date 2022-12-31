class Sistema:
    def __init__(self, nombre="Medical Center", direccion="Av. Garcia Moreno y Colon", telefono="(04)2727354"):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        
if __name__ == '__main__':
    sis = Sistema()
    print("--------------")
    print(sis.nombre)
    print("--------------")
    
