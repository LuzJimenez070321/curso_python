# crear una clase de alumnos con los atributos que usted crea conveniente 
# luego instanciaran a 4 alumnos 

# nombre de mi clase 
class Alumno:
    # atributos
    def _init_(self,nombre,apellido,dni,genero):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.genero=genero
    def mostrar_alumno(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "dni":self.dni,
            "genero":self.dni,
        }    
luz=Alumno("Luz","jimenez",75604355,"mujer")
print(luz.dni)    

jesus=Alumno("Jesus","cabana",60345212,"varon")
print(jesus.genero)

liz=Alumno("Liz","zevallos",45362134,"mujer")
print(liz.nombre)

jorgue=Alumno("Jorgue","mendez",64532916,"varon")
print(jorgue.apellido)
