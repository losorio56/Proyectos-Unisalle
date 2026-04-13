# Crear clase con método constructor y atributos

class Usuario:
    def __init__(self, nombre_completo: str, email:str, dni:int) -> None: # se definen los atributos
        self.nombre = nombre_completo
        self._email = email # Atributo protegido
        self.__dni = dni # Atributo privado

    def mostrar_informacion(self) -> str:
        return f"Nombre del usuario: {self.nombre}, EMAIL: {self._email}, DNI: {self.__dni}" # la f es para darle formato
    
usuario1 = Usuario()