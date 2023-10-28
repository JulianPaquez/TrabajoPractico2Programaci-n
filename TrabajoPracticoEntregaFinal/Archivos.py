
class Archivos():
    def __init__(self,nombre:str,fecha, formato: str):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato
    

    def __str__(self):
        return f"Nombre: {self.__nombre} \t Fecha : {self.__fecha} \t Formato: {self.__formato}"
