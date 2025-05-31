

def calcular_estadisticas(notas:list[float]) -> dict:
    """Calcula las estadisticas de una lista de notas"""


    try:
        promedio = sum(notas) / len(notas) #formula de promedio, sumas la cantidad de notas y con len recorres esa lista de notas y cuentas cuantas notas hay
        mayor = max(notas)
        menor = min(notas)
        aprobado = [a for a in notas if a >= 4.0]

        resultado = {
            "promedio" : promedio,
            "mayor" : mayor,
            "menor" : menor,
            "aprobado" : aprobado
        }
        return resultado
    except ZeroDivisionError:
       return None
   