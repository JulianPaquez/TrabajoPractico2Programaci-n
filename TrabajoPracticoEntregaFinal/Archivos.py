
class Archivos():
    def __init__(self,nombre:str,fecha, formato: str):
        self.__nombre = str(input("Ingrese el nombre del archivo"))
        self.__fecha = int(input("Ingrese la fecha del archivo"))
        self.__formato = str(input("Ingrese el formato del archivo"))
        listaArchivos = []


    def __str__(self):
        return f"Nombre: {self.__nombre} \t Fecha : {self.__fecha} \t Formato: {self.__formato}"
