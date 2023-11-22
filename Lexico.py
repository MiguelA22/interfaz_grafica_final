import ply.lex as lex
import Sintatico
import Semantica
from Sintatico import analizar_sintaxis_ip
from common import errores_lexicos
from tabla_de_simbolos import add_symbol, symbol_table, assign_memory_address, tabla_simbolos

# Listas para almacenar los tokens y errores léxicos
tokens_validos = []


cadena_entrada = []  # Lista para almacenar la cadena de entrada

# Definición de tokens
tokens = ['LIMITE_A', 'LIMITE_B', 'LIMITE_C', 'LIMITE_D', 'LIMITE_E', 'PUNTO']

# Reglas para los tokens
def t_LIMITE_E(t):
    r'(240|24[1-9]|25[0-5])'
    t.value = int(t.value)
    tokens_validos.append(('LIMITE',t.value))
    add_symbol('LIMITE_E', t.value)
    print(f"LexToken válido LIMITE_E: {t.value}")
    return t

def t_LIMITE_D(t):
    r'224|22[5-9]|23[0-9]'
    t.value = int(t.value)
    tokens_validos.append(('LIMITE',t.value))
    add_symbol('LIMITE_D', t.value)
    print(f"LexToken válido LIMITE_D: {t.value}")
    return t

def t_LIMITE_C(t):
    r'19[2-9]|20[0-9]|21[0-9]|22[0-3]'
    t.value = int(t.value)
    tokens_validos.append(('LIMITE',t.value))
    add_symbol('LIMITE_C', t.value)
    print(f"LexToken válido LIMITE_C: {t.value}")
    return t

def t_LIMITE_B(t):
    r'19[0-1]|1[3-8][0-9]|12[8-9]'
    t.value = int(t.value)
    tokens_validos.append(('LIMITE',t.value))
    add_symbol('LIMITE_B', t.value)
    print(f"LexToken válido LIMITE_B: {t.value}")
    return t

def t_LIMITE_A(t):
    r'(?:-?)(?:(?:12[0-7]|1[0-1][0-9]|[0-9]{1,3})|(?!0)\d+)'  # Modificación aquí
    t.value = int(t.value)
    if t.value > 127 or t.value < 0:  # Modificación aquí
        errores_lexicos.append("Token invalido :Número fuera de rango en la línea {:2} valor {:4} posición {:2}".format(str(t.lineno), str(t.value), str(t.lexpos)))
        t.lexer.skip(1)
    else:
        tokens_validos.append(('LIMITE',t.value))
        add_symbol('LIMITE_A', t.value)
        print(f"LexToken válido LIMITE_A: {t.value}")
    return t

def t_PUNTO(t):
    r'\.'
    tokens_validos.append(('PUNTO',t.value))
    add_symbol('PUNTO', t.value)
    print(f"LexToken válido PUNTO: {t.value}")
    return t
# terminan las reglas del tokennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
t_ignore = ' \t\n'
def t_error(t):
    global errores_lexicos
    if '-' in t.value:
        # Eliminar el token actual y avanzar hasta el siguiente espacio en blanco
        t.lexer.lexpos = t.lexer.lexpos + len(t.value)
        errores_lexicos.append("** Token invalidado en la línea {:2} valor {:4} posición {:2} ".format(str(t.lineno), str(t.value), str(t.lexpos)))
    elif any(char.isalpha() for char in t.value):
        # Verificar si el token contiene letras
        error_message = "** Error léxico: Token contiene letras en la línea {:2} valor {} posición {:2} ".format(str(t.lineno), repr(t.value), str(t.lexpos))
        errores_lexicos.append(error_message)
        t.lexer.skip(3)
    else:
        errores_lexicos.append("** Token no válido en la línea {:2} valor {:4} posición {:2} ".format(str(t.lineno), str(t.value), str(t.lexpos)))
    t.lexer.skip(1)
# Función para analizar la información ingresada
def analizar_ip(datos_ingresados):
    global errores_lexicos, tokens_validos
    analizador.input(datos_ingresados)
    errores_lexicos.clear()
    tokens_validos.clear()
    symbol_table.clear()
    tabla_simbolos.clear()
    for token in analizador:
        pass
    #evaluarsemantica = ['192.168.125.32', '195.170.125.102']
    assign_memory_address()
    if errores_lexicos:
        print("Errores léxicos encontrados:")
        for error in errores_lexicos:
            print(error)
            print("tokens validos:", tokens_validos)
            #print(print_symbol_table)

        return str(tabla_simbolos),str(errores_lexicos)
    else:
        print("Tokens de cadena válidos, Procesando en el analizador Sintáctico.")
        analizar_sintaxis_ip(tokens_validos)
        return str(tabla_simbolos),str(errores_lexicos)
# Crear el analizador léxico fuera de la función
analizador = lex.lex()

