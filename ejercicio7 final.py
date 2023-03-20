class titular :
    def __init__(self, apellido, nombre, dni, saldo):
        self._apellido=apellido
        self._nombre=nombre
        self._dni=dni
        self._saldo=saldo
        
 
    @property
    #devuelve variable interna
    def nombre(self):
        print(f"Ingrese su nombre por favor:")
        self.nombre=input()
    
    #para verificar que sea tipo texto
    @nombre.setter
    def nombre(self,nNombre):
        if nNombre!="" and  type(nNombre)==str:
            self._nombre=nNombre
        else:
            print("Ingrese su nombre nuevamente")
    
    @property
    def apellido(self):
        print(f"Ingrese su apellido por favor: ")
        self.apellido=input()
    
    @apellido.setter
    def apellido(self,nApellido):
        if nApellido!="" and  type(nApellido)==str:
            self._nombre=nApellido
        else:
            print("Ingrese su apellido nuevamente")
        
    @property
    def dni(self):
        print(f"Ingrese su DNI por favor: ")
        self.dni=input()
    
    @dni.setter
    def dni(self,nDni):
        if type(nDni)!=str and type(nDni)!=float and nDni>0:
            self._dni=nDni
        else:
            print("ingrese su DNI nuevamente")
   
   
@property
     
def ingresar(self,cantidadIngresada):
        if cantidadIngresada<0:
            print("Debe ingresar un monto")
            self.cantidadIngresada= cantidadIngresada
        else:
            self._saldo+=cantidadIngresada
            print(f"Nuevo saldo de la Cuenta:$",  self._saldo)
    
def retirar(self,retiro):
        if retiro<0:
            retiro*-1
            self._saldo-=retiro
            print(f"Nuevo saldo de la Cuenta:$",  self._saldo)
        else:
            self._saldo-=retiro
            print(f"Estado de Cuenta:$", self._saldo)
            
def mostrar(self):
        print(f"Datos del titular de la cuenta: {self._titular}, {self._cantidad} DIN n° {self._dni}");
        
titular1=titular(apellido="", nombre="", dni="", saldo="");
titular1 . ingresar()
titular1 . retitar()      
titular1 . mostrar()