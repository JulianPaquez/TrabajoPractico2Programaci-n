import os

if resultado == "Ha accedido al sistema":
                opcion1 = input("\n Ingrese una opción del menú: ")
                print("1 - Matricularse a un curso")
                print("2 - Ver curso")
                print("3 - Volver al menú principal")
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