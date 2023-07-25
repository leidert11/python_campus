from paquete.espacio_acceso import  espacios_acceso_campers
from no_clase import no_hay_horario_clases
from no_entrar import no_estudiar_nunca
from promedio_clases import promedio_espacios_clase

def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar a cuales espacios tienen acceso los campers")
        print("2. Mostrar como camper donde puedo estar, si NO es horario de clases")
        print("3. Mostrar donde no puedo sentarme a estudiar nunca como camper")
        print("4. Mostrar el promedio de la capacidad de los espacios destinados a clase")
        print("5. Salir")
        try:
            opcion = int(input("Ingrese la opción deseada: "))

            if opcion == 1:
                espacios_acceso_campers()
            elif opcion == 2:
               no_hay_horario_clases()
            elif opcion == 3:
                no_estudiar_nunca()
            elif opcion == 4:
                promedio_espacios_clase()
            elif opcion == 5:
                print("Saliendo del programa...")
                break

        except ValueError:
            print("Opción no válida, intente nuevamente.")
            
    return opcion


menu()