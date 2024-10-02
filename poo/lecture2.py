class Personaje:
    #atributos
    def _init_(self,nombre,edad,usuario,bando,raza):
     self.nombre=nombre
     self.edad=edad
     self.usuario=usuario
     self.bando=bando
     self.raza=raza
    def mostrar_personaje(self):
       return {
          "nombre":self.nombre,
          "edad":self.edad,
          "usuario":self.usuario,
          "bando":self.bando,
          "raza":self.raza,
       } 

luffy=Personaje("Luffy",18,"gomu gomu no mi","pirata","humano") 
print(luffy.nombre)

cobby=Personaje("cobby",15,"no","sword","humano")
print(cobby.edad)

King=Personaje("King",40,"zoan mitologica","pirata","lunaria")
print(King.raza)
     