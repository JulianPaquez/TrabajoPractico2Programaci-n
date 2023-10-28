import os
import random
import Archivos
import Carrera
class Usuario():
    def __init__(self,nombre,apellido,email,contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Email: {self.email} \n Contraseña: *************"
    
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,legajo,anioIngreso):
        super().__init__(nombre, apellido, email, contrasenia)
        #self.legajo = int(input("Ingrese su legajo\n"))
        #self.anio = int(input("Ingrese el año que ingresó a la carrera\n"))
        self.legajo = legajo
        self.anioIngreso = anioIngreso
        self.mis_cursosEstudiante = []
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Email: {self.email},Contraseña: {self.contrasenia} Legajo: {self.legajo}, Año de ingreso: {self.anioIngreso}"
    
   
    def ValidarIngresoEstudiante(self):
        emailEstudiante = input("Ingrese su correo: ")
        ContrEstudiante = input("Ingrese su contraseña: ")
        
        if emailEstudiante == "lucasgonzalez@gmail.com" or emailEstudiante == "pedroperez@gmail.com" or emailEstudiante == "juliangomez@gmail.com" or emailEstudiante == "mateolopez@gmail.com" and ContrEstudiante == "123" or ContrEstudiante == "234" or ContrEstudiante == "345" or ContrEstudiante == "456":
                    return "Ha accedido al sistema"
        elif emailEstudiante != "lucasgonzalez@gmail.com" or emailEstudiante != "pedroperez@gmail.com" or emailEstudiante != "juliangomez@gmail.com" or emailEstudiante != "mateolopez@gmail.com":
                    print ("El email ingresado es incorrecto. ")
        elif ContrEstudiante != "123" or ContrEstudiante != "234" or ContrEstudiante != "345" or ContrEstudiante != "456":
                    print ("La contraseña ingresada es incorrecta. ")
        elif ( emailEstudiante != "lucasgonzalez@gmail.com" or emailEstudiante != "pedroperez@gmail.com" or emailEstudiante != "juliangomez@gmail.com" or emailEstudiante != "mateolopez@gmail.com" and ContrEstudiante != "123" or ContrEstudiante != "234" or ContrEstudiante != "345" or ContrEstudiante != "456"):
                    print ("Email y contraseña incorrectos.El alumno debe darse de alta en alumnado ")
        
        

    def Matricular(self, curso, contraseniaMateria):
        if curso in self.mis_cursosEstudiante:
            return "Ya estás matriculado en este curso"
        if contraseniaMateria != cursos[curso]["contraseña"]:
            return "Contraseña incorrecta"
        self.mis_cursosEstudiante.append(curso)
        return f"Te has matriculado en el curso {curso}\n "#Archivos:\n tpi.pdf\n practica1.pdf"



class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,titulo,anioEgreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anioEgreso = anioEgreso
        self.mis_cursosProfesor = []
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} \t Apellido: {self.apellido} \t Email: {self.email} \t Contraseña: {self.contrasenia} \t Legajo: {self.titulo} \t Año: {self.anioEgreso}"

    def DictarCurso(self):
        for materia in cursos: 
            print (materia)    
        OptCurso = int(input("Ingrese el curso en el que desea dar clases\n"))
        if 1 <= OptCurso <= len(cursos):
            materia = list(cursos.keys())[OptCurso - 1]
            contrasena = str(random.randint(10000, 99999))
            self.mis_cursosProfesor.append(materia)
        else:
            print("Opción inválida")
        return f"Curso {materia}\t Contraseña: {contrasena} dado de alta correctamente"

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
            return "Inexistente.El profesor debe darse de alta en alumnado"
        
class Curso(Estudiante):
    def __str__():
        print("Materia: InglesI \t\t Carrera: Tecnicatura Universitaria en Programación")
        print("Materia: InglesII \t\t Carrera: Tecnicatura Universitaria en Programación")
        print("Materia: LaboratorioI \t\t Carrera: Tecnicatura Universitaria en Programación")
        print("Materia: LaboratorioII \t\t Carrera: Tecnicatura Universitaria en Programación")
        print("Materia: ProgramaciónI \t\t Carrera: Tecnicatura Universitaria en Programación")
        print("Materia: ProgramaciónII \t Carrera: Tecnicatura Universitaria en Programación")    

class CursoProf(Profesor) :
    def __str__():
        print("Materia: InglesI ")
        print("Materia: InglesII")
        print("Materia: LaboratorioI ")
        print("Materia: LaboratorioII ")
        print("Materia: ProgramaciónI ")
        print("Materia: ProgramaciónII ")            



cursos = {
    "Programación I": {"contraseña": "11111"},
    "Programación II": {"contraseña": "22222"},
    "Laboratorio II": {"contraseña": "33333"},
    "Inglés I": {"contraseña": "44444"},
    "Inglés II": {"contraseña": "66666"},
}



estudiante1 = Estudiante("Lucas", "Gonzales", "lucasgonzalez@gmail.com", "123", "98765", "2020")
estudiante2 = Estudiante("Pedro", "Perez", "pedroperez@gmail.com", "234", "12345", "2021")
estudiante3 = Estudiante("Julian", "Gomez", "juliangomez@gmail.com", "345", "56565", "2023")
estudiante4 = Estudiante("Mateo", "Lopez", "mateolopez@gmail.com", "456", "10101", "2022")

'''EmailsEstudiantes = [
    "lucasgonzalez@gmail.com",
    "pedroperez@gmail.com",
    "juliangomez@gmail.com",
    "mateolopez@gmail.com"
]

ContraseniasEstudiantes = [
    "123",
    "234",
    "345",
    "456"
]'''

Estudiantes = [ estudiante1,estudiante2,estudiante3,estudiante4 ]


profesor1 = Profesor("Victor", "Cuesta", "Victor1234@gmail.com", "777", "Ingeniero en Sistemas", "2010")
profesor2 = Profesor("Ruben", "Perez", "rubenperez@gmail.com", "888", "Ingeniero Industrial", "2009")
profesor3 = Profesor("Jose", "Gomez", "josegomez@gmail.com", "999", "Tecnico en Programacion", "2021")
profesor4 = Profesor("Juan", "Lopez", "juanlopez@gmail.com", "1010", "Profesorado en Matematica", "2001")

Profesores = [profesor1,profesor2,profesor3,profesor4]




"""def Materia():
    print("Materia: InglesI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: InglesII \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioII \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónI \t\t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónII \t Carrera: Tecnicatura Universitaria en Programación")"""

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
            for estudiante in Estudiantes:
                print(estudiante)

            emailEstudiante = input("Ingrese su correo: ")
            ContrEstudiante = input("Ingrese su contraseña: ")
            
            estudiante_inscripto = None
            for estudiante in Estudiantes:
                if estudiante.email == emailEstudiante and estudiante.contrasenia == ContrEstudiante:
                    estudiante_inscripto = estudiante
                    break
            if estudiante_inscripto:
                print(f"Usted accedió correctamente al sistema, {estudiante_inscripto.nombre}!")
                opcion1 = None#Esto lo ponemos para que no se repita el "Opcion inválida"
                print("1 - Matricularse a un curso")
                print("2 - Ver curso")
                print("3 - Volver al menú principal")
                opcion1 = input("\n Ingrese una opción del menú: ")               
                os.system("cls")  # Limpiar pantalla
                if opcion1.isnumeric():
                        if int(opcion1) == 1:
                            print("Materias disponibles:")
                            for materia in cursos:
                                print(materia)
                            optMateria = int(input("Ingrese el número de la materia para matricularse: "))
                            if 1 <= optMateria <= len(cursos):
                                materia = list(cursos.keys())[optMateria - 1]
                                contrasenia = input(f"Ingrese la contraseña para {materia}: ")
                                devolucion = estudiante.Matricular(materia, contrasenia)
                                print(devolucion)
                            else:
                                print("Opción inválida")
                        elif int(opcion1) == 2:
                                cursos_matriculados = estudiante_inscripto.mis_cursosEstudiante
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
                print("Opción inválida.Contraseña o mail Incorrectos")
            

        elif int(opt) == 2:
            for profesor in Profesores:
                print(profesor)

            emailProfesor = input("Ingrese su correo: ")
            ContrProfesor = input("Ingrese su contraseña: ")

            profesor_inscripto = None
            for profesor in Profesores:
                if profesor.email == emailProfesor and profesor.contrasenia == ContrProfesor:
                    profesor_inscripto = profesor
                    break
                else:
                    print("El profesor no esta inscripto")
                    Codigo_admin = input("Ingrese el codigo 'admin' para darse de alta como profesor")

                    if Codigo_admin == "admin":
                        print("Profesor agregado con éxito")
                        Profesores.append("""Agregar profesor""") #agregar un profesor
                    else:
                        print("Código incorrecto")

            if profesor_inscripto:
                print(f"Usted accedió correctamente al sistema, {profesor_inscripto.nombre}!")
                opcion2 = None
                print("1 - Dictar curso")
                print("2 - Ver curso")
                print("3 - Volver al menú principal")
                opcion2 = input("\n Ingrese una opción del menú: ") 
                if opcion2 == "1":
                    devolucion = profesor.DictarCurso()
                    print(devolucion)
                elif opcion2 == "2":
                    cursos_inscriptos = profesor_inscripto.VerCursos()
                    if cursos_inscriptos:
                        print("Cursos donde dará clases:")
                        for curso in cursos_inscriptos:
                            print("Materia y Contraseña",curso)
                    else:
                        print("No estás inscripto en ningún curso.")
                elif opcion2 == "3":
                    pass
                else:
                    print("Opción incorrecta")
            else:
                 print("Opcion Inválida.El mail o contraseña es incorrecto")
        elif int(opt) == 3:
            Curso.__str__()
        elif int(opt) == 4:
            respuesta = "salir"
            print("Usted ha salido del programa")
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!")