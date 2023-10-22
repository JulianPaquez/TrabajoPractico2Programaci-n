import os
import random

class Usuario():
    def __init__(self,nombre,apellido,email,contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Email: {self.email} \n Contraseña: *************"
    
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = int(input("Ingrese su legajo\n"))
        self.anio = int(input("Ingrese el año que ingresó a la carrera\n"))
        self.mis_cursosEstudiante = []
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Email: {self.email}, Legajo: {self.legajo}"
    

    def ValidarIngresoEstudiante(self):
        emailEstudiante = input("Ingrese su correo: ")
        ContrEstudiante = input("Ingrese su contraseña: ")
        
        if emailEstudiante == "lucasgonzalez@gmail.com" and ContrEstudiante == "1234":
            return "Ha accedido al sistema"
        elif emailEstudiante != "lucasgonzalez@gmail.com":
            print ("El email ingresado es incorrecto. ")
        elif ContrEstudiante != "1234":
            print ("La contraseña ingresada es incorrecta. ")
        elif(emailEstudiante != "lucasgonzalez@gmail.com" and ContrEstudiante != "1234"):
            print ("Email y contraseña incorrectos. ")
        
        

    def Matricular(self, curso, contraseniaMateria):
        if curso in self.mis_cursosEstudiante:
            return "Ya estás matriculado en este curso"
        if contraseniaMateria != cursos[curso]["contraseña"]:
            return "Contraseña incorrecta"
        self.mis_cursosEstudiante.append(curso)
        return f"Te has matriculado en el curso {curso}"



class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = str(input("Ingrese su título\n"))
        self.anioEgreso = int(input("Ingrese el año de egreso\n"))
        self.mis_cursosProfesor = []
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Email: {self.email} \n Contraseña: ************* \n Legajo: {self.titulo} \n Año: {self.anioEgreso}"

    def DictarCurso(self):
        contrasena = str(random.randint(10000, 99999))
        self.mis_cursosProfesor.append(contrasena)
        return f"Curso {contrasena} dado de alta correctamente"

    def VerCursos(self):
        return self.mis_cursosProfesor

    def ValidarIngresoProfesor(self):
        emailProfesor = input("Ingrese su correo: ")
        ContrProfesor = input("Ingrese su contraseña: ")
        
        if emailProfesor == "Victor1234@gmail.com" and ContrProfesor == "777":
            return "Ha accedido al sistema"
        elif emailProfesor != "Victor1234@gmail.com":
            print ("El email ingresado es incorrecto. ")
        elif ContrProfesor != "777":
            print ("La contraseña ingresada es incorrecta. ")
        elif(emailProfesor != "Victor1234@gmail.com" and ContrProfesor != "777"):
            return "Inexistente."
        
    
    



cursos = {
    "Programación I": {"contraseña": "11111"},
    "Programación II": {"contraseña": "22222"},
    "Laboratorio II": {"contraseña": "33333"},
    "Inglés I": {"contraseña": "44444"},
    "Inglés II": {"contraseña": "66666"},
}



Personas = []
Estudiante1 = Estudiante("Lucas", "Gonzales", "lucasGonzales@gmail.com", "1234")
Personas.append(Estudiante1)
print(Estudiante1.__str__())
Profesor1 = Profesor("Victor" , "Cuesta", "Victor1234@gmail.com", "HolaUTN",)
Personas.append(Profesor1)
print(Profesor1.__str__())

def Materia():
    print("Materia: InglesI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: InglesII \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioII \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónII \t Carrera: Tecnicatura Universitaria en Programación")

print("Bienvenido!")
respuesta = ""

def menu():
    print ("\t\t")
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla

    if opt.isnumeric():
        if int(opt) == 1:
            resultado = Estudiante1.ValidarIngresoEstudiante()           
            if resultado == "Ha accedido al sistema":
                print ("Usted accedio correctamente al sistema. \t\t")
                print("1 - Matricularse a un curso")
                print("2 - Ver curso")
                print("3 - Volver al menú principal")
                opcion1 = input("\n Ingrese una opción del menú: ")               
                os.system("cls")  # Limpiar pantalla
                if opcion1.isnumeric():
                    if int(opcion1) == 1:
                        print("Materias disponibles:")
                        for idx, (materia, _) in enumerate(cursos.items(), start=1):
                            print(f"{idx}. {materia}")
                        optMateria = int(input("Ingrese el número de la materia para matricularse: "))
                        if 1 <= optMateria <= len(cursos):
                            materia = list(cursos.keys())[optMateria - 1]
                            contrasenia = input(f"Ingrese la contraseña para {materia}: ")
                            devolucion = Estudiante1.Matricular(materia, contrasenia)
                            print(devolucion)
                        else:
                            print("Opción inválida")
                    elif int(opcion1) == 2:
                        cursos_matriculados = Estudiante1.mis_cursosEstudiante
                        if cursos_matriculados:
                            print("Cursos matriculados:")
                            for curso in cursos_matriculados:
                                print(curso)
                        else:
                            print("No estás matriculado en ningún curso.")
                    elif int(opcion1) == 3:
                        pass
                    else:
                        print("Opción inválida")
                else:
                    print("Opción inválida")
            

        elif int(opt) == 2:
            resultadoB = Profesor1.ValidarIngresoProfesor
            if resultadoB == "Ha accedido al sistema":
                opcion2 = input("\n Ingrese una opción del menú: ")
                if opcion2 == "1":
                    devolucion = Profesor1.DictarCurso()
                    print(devolucion)
                elif opcion2 == "2":
                    cursos_impartidos = Profesor1.VerCursos()
                    if cursos_impartidos:
                        print("Cursos impartidos:")
                        for curso in cursos_impartidos:
                            print(curso)
                    else:
                        print("No estás impartiendo ningún curso.")
                elif opcion2 == "3":
                    pass
                else:
                    print("Opción incorrecta")
        elif int(opt) == 3:
            Materia()
        elif int(opt) == 4:
            respuesta = "salir"
            print("Usted ha salido del programa")
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!")