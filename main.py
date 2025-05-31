import sys
from notas.menu import menu
from notas.ingresar_nota import ingresar_notas
from notas.calculos import calcular_estadisticas

def main():
    notas = []

    while True:
        menu()
        opcion = (input("Ingrese una opción : "))

        if opcion  == "1":
           ingresar_notas()
           print(f"notas ingresadas son : {notas}")

        elif opcion == "2":
            if calcular_estadisticas(notas) == None:
                print("No se agregaron notas por favor agregalas")
                notas = ingresar_notas()
            
            estadisticas = calcular_estadisticas(notas)


        elif opcion == "3":
            print(estadisticas)
            
        else:
            print("Terminado")
            break
            
if __name__ == "__main__":
main()
