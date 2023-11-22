
from common import  errores_lexicos
#from Lexico import evaluarsemantica
def analizar_sintaxis_ip(tokens):
    t_ignore = ' \t\n'
    # Definir la sintaxis de una dirección IP (por ejemplo, IPv4)
    sintaxis_esperada = ["LIMITE", "PUNTO", "LIMITE", "PUNTO", "LIMITE", "PUNTO", "LIMITE"]

    # Verificar si el orden de los tokens coincide con la sintaxis esperada
    for tipo_esperado in sintaxis_esperada:
        if not tokens:
            print("Sintax error: Se esperaba más Octectos.")
            from common import errores_lexicos
            errores_lexicos.append("Sintax error: Se esperaba más Octectos.")
            return False

        tipo_actual, valor = tokens.pop(0)  # Obtener el primer token de la tupla

        if tipo_actual != tipo_esperado:
            print(f"Sintax error: Se esperaba {tipo_esperado} pero se encontró {tipo_actual}.")
            from common import errores_lexicos
            errores_lexicos.append("Sintax error: se esperaba un octecto en vez de punto.")
            #print("lista de errores lexicos :", errores_lexicos)
            return False

    # Verificar si hay tokens adicionales después de la dirección IP
    if tokens:


        print("Error: Hay tokens adicionales después de la dirección IP.")
        from Lexico import errores_lexicos
        errores_lexicos.append("Sintax error: hay octectos de sobra")
        return False
    # La sintaxis de la dirección IP es válida
    print("La sintaxis de la dirección IP es válida.")
    from Semantica import clasificar_direcciones_ip
    #resultados_clasificacion=[]
    #resultados_clasificacion = clasificar_direcciones_ip(evaluarsemantica)
    #print("Resultado clasificacion.",resultados_clasificacion)
    return True
    #resultados_clasificacion
    #str(resultados_clasificacion))

