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
    
    def __str__(self) -> str:
        return  f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Email: {self.email} \n Contraseña: ************* \n Legajo: {self.legajo} \n Año: {self.anio}"
    
    """def MatricularCurso(self):
        self.Curso = """
    
    def ValidarIngresoEstudiante(self,emailEstudiante,ContrEstudiante):
        if(self.email == emailEstudiante and self.contrasenia == ContrEstudiante):
            return print("Ha accedido al sistema")
        elif(self.email != emailEstudiante  or self.contrasenia != ContrEstudiante):
            return print("contraseña o mail incorrecta")
        elif(self.email != emailEstudiante  and self.contrasenia != ContrEstudiante):
            return print("Alumno inexistente,debe darse de alta en alumnado")



class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = str(input("Ingrese su título\n"))
        self.anioEgreso = int(input("Ingrese el año de egreso\n"))
        self.mis_cursosProfesor = []
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Email: {self.email} \n Contraseña: ************* \n Legajo: {self.titulo} \n Año: {self.anioEgreso}"

    """ def DictarCurso(self):"""

    def ValidarIngresoProfesor(self):
        if(self.email == emailProfesor and self.contrasenia == ContrProfesor):
            return print("Ha accedido al sistema")
        elif(self.contrasenia != ContrProfesor or self.email != emailProfesor):
            return print("contraseña o mail incorrecta")
        else:
            return print("Profesor inexistente,debe darse de alta en alumnado")
        
    def DictarCurso(self):
        # Generar una contraseña aleatoria para el curso
        contrasena = str(random.randint(10000, 99999))

        # Agregar el curso a la lista de cursos del profesor
        self.mis_cursosProfesor.append(contrasena)

        # Mostrar un mensaje de éxito
        print(f"Curso {contrasena} dado de alta correctamente")
    
    def MenuProfesor(profesor):
     print("1. Dictar curso")
     print("2. Ver curso")
     print("3. Volver al menú principal")
     opcion = input("Ingrese la opción de menú: ")

     if opcion == "1":
        # Dictar un curso
        profesor.DictarCurso()

     elif opcion == "2":
        # Ver cursos
        profesor.VerCursos()

     elif opcion == "3":
        return

     else:
        print("Ingrese una opción válida")




class Curso(Estudiante):
    def __init__(self, nombre,contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.mis_cursosEstudiante = []
        
    def Matricular(self,curso,contraseniaMateria):
        if curso in self.mis_cursosEstudiante:
            print("El curso ya está matriculado")
            return
        if contraseniaMateria != self.contrasenia["contraseña"]:
            print("Contraseña incorrecta.")
            return
        self.mis_cursosEstudiante.append(curso)
        print("El curso se ha matriculado correctamente")
        
          


cursos = {
     "Programación I": {"contraseña": "11111"},
     "Programación II": {"contraseña": "22222"},
     "Laboratorio II": {"contraseña": "33333"},
     "Inglés I": {"contraseña": "44444"},
     "Inglés II": {"contraseña": "66666"},
     }

Personas = []
Estudiante1 = Estudiante("Lucas", "Gonzales", "lucasGonzales@gmail.com", 1234)
Personas.append(Estudiante1)
print(Estudiante1.__str__())
Profesor1 = Profesor("Victor" , "Cuesta", "Victor1234@gmail.com", "HolaUTN",)
Personas.append(Profesor1)
print(Profesor1.__str__())

def Materia():
    print("Materia: InglesI \t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: InglesII \t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioI \t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: LaboratorioII \t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónI \t Carrera: Tecnicatura Universitaria en Programación")
    print("Materia: ProgramaciónII \t Carrera: Tecnicatura Universitaria en Programación")


import os

print("Bienvenido!")
respuesta = ''
        
def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            emailEstudiante = str(input("Ingrese el mail\n"))
            ContrEstudiante = input("Ingrese la contraseña\n")
            resultado = Estudiante1.ValidarIngresoEstudiante(emailEstudiante,ContrEstudiante)
            print(resultado) #arreglar IF
            if resultado == "Ha accedido al sistema":
             opcion1 = input("\n Ingrese una opción del menú: ")
             print("1 - Matricularse a un curso")
             print("2 - Ver curso")
             print("3 - Volver al menú principal")
             os.system ("cls") #Limpiar pantalla
             if opcion1.isnumeric():
                if(opcion1 == 1):
                 optMateria = int(input("Ingrese una opcion para seleccionar una materia"))
                 if int(optMateria) == 1:
                    print("Programación I")
                    devolucion = Estudiante1.Matricular("Programación I",cursos["Programación I"]["contraseña"]) 
                 elif int(optMateria) == 2:
                    print("Programación II")
                    devolucion = Estudiante1.Matricular("Programación I",cursos["Programación II"]["contraseña"]) 
                 elif int(optMateria) == 3:
                    print("Laboratorio II")
                    devolucion = Estudiante1.Matricular("Programación I",cursos["Laboratorio II"]["contraseña"]) 
                 elif int (optMateria) == 4:
                    print(" Ingles I")
                    devolucion = Estudiante1.Matricular("Programación I",cursos["Inglés I"]["contraseña"]) 
                 elif int (optMateria) == 5:
                    print("InglesII")
                    devolucion = Estudiante1.Matricular("Programación I",cursos["Inglés II"]["contraseña"]) 
            else:
                print("Opcion incorrecta")
        elif int(opt) == 2:
            emailProfesor = str(input("Ingrese el mail\n"))
            ContrProfesor = input("Ingrese la contraseña\n")
            profesorCurso = Profesor(emailProfesor, ContrProfesor)
            profesorCurso.ValidarIngresoProfesor()
            #MenuProfesor.ProfesorCurso no se pq no funciona

            
        elif int(opt) == 3:
            Materia()
            
        elif int(opt) == 4:
            respuesta = "salir"
            print("Usted ha salido del programa")
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")












"""class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Gimnasio:
    def _init_(self):
        self.personas = []

    def alta_persona(self):
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        if edad >= 18:
            persona = Persona(nombre, edad)
            self.personas.append(persona)
            print("Persona agregada correctamente.")
        else:
            print("La persona debe ser mayor de edad para ingresar al gimnasio.")

    def baja_persona(self):
        nombre = input("Ingrese el nombre de la persona a dar de baja: ")

        for persona in self.personas:
            if persona.nombre == nombre:
                self.personas.remove(persona)
                print("Persona eliminada correctamente.")
                return

        print("No se encontró a la persona en el gimnasio.")

    def modificar_persona(self):
        nombre = input("Ingrese el nombre de la persona a modificar: ")

        for persona in self.personas:
            if persona.nombre == nombre:
                nueva_edad = int(input("Ingrese la nueva edad: "))

                if nueva_edad >= 18:
                    persona.edad = nueva_edad
                    print("Edad modificada correctamente.")
                else:
                    print("La persona debe ser mayor de edad para ingresar al gimnasio.")

                return

        print("No se encontró a la persona en el gimnasio.")

    def mostrar_personas(self):
        for persona in self.personas:
            print(f"Nombre: {persona.nombre}, Edad: {persona.edad}")

gimnasio = Gimnasio()

while True:
    print("\n--- MENÚ ---")
    print("1. Alta de persona")
    print("2. Baja de persona")
    print("3. Modificar edad de persona")
    print("4. Mostrar personas")
    print("5. Salir") 
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        gimnasio.alta_persona()
    elif opcion == 2:
        gimnasio.baja_persona()
    elif opcion == 3:
        gimnasio.modificar_persona()
    elif opcion == 4:
        gimnasio.mostrar_personas()
    elif opcion == 5:
        break
    else:
        print("Opción inválida.")"""