
def ingresar_notas() -> list[float]:
    """
    Solicita al usuario el ingreso de notas separadas por espacio, se separan y se transforman en una lista de flotantes
    """

    n = input("ingresa las notas(las notas deben estar separadas por espacio): ")
    n = n.split(" ")
    notas = [float(nota) for nota in n]
    return notas

