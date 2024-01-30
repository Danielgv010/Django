class Persona:

    mayorEdad = 18 # Atributo de clase

    def __init__(self,nombre,apellidos,edad): # Constructor
        self.nombre = nombre # Atributo de instancia
        self.apellidos = apellidos # Atributo de instancia
        self.edad = edad # Atributo de instancia

    # Método de instancia
    def nombreCompleto(self):
        print(self.nombre+" "+self.apellidos)

    # Método estático
    @staticmethod
    def saludos():
        print("Hola")

    # Método de clase
    @classmethod
    def cambiarMayorEdad(cls,valor):
        cls.mayorEdad = valor
# Fin de la clase Persona

# Crear dos objetos Persona
persona1 = Persona("John","Doe",22)
persona2 = Persona("Johnnah","Doebry",33)

# Obtener valor de un atributo
print(persona1.nombre)
# Ejecutar un método
persona2.nombreCompleto()
# Modificar un atributo
persona1.nombre = "Joe"
print(persona1.nombre)

# Mostrar atributo de clase
print(Persona.mayorEdad)
print(persona1.mayorEdad)

#Llamar a un método estático
Persona.saludos()

#Llamar a un método de clase
Persona.cambiarMayorEdad(21)
print(Persona.mayorEdad)

def suma(a,b): # Parametros -> a, b
    return a + b

print(suma(1,2)) # Argumentos que se pasan a la funcion -> 1, 3

# Funcion de suma de tres parametros
def suma3(a=0,b=0,c=0):
    return a + b + c

print(suma3(b=1,a=2,c=3))
print(suma3(b=1,a=2))

def sumaMuchos(*args):
    print(args)
    res = 0
    for arg in args:
        res+=arg
    print(res)

sumaMuchos(1,2,3,4,5,6,7,8,9)


def sumaMuchos(**kwargs):
    print(kwargs)
    res = 0
    for clave,valor in kwargs.items():
        print(clave,valor)
        res += valor
    print(res)


def sumaTodo(*args, **kwargs):
    print(args)
    print(kwargs)

sumaTodo(1,2,a=1,b=2,c=3)