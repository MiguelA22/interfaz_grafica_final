import random

symbol_table = {}  # Diccionario para almacenar los símbolos
tabla_simbolos=[] #tabla de simbolos de forma no secuencial
memory_addresses = set()  # Conjunto global para almacenar direcciones de memoria

def add_symbol(token_type, value):
    if token_type not in symbol_table:
        symbol_table[token_type] = {'valores': []}
    symbol_table[token_type]['valores'].append({'valor': value, 'direccion_memoria': None})

def assign_memory_address():
    for token_type, data in symbol_table.items():
        for entry in data['valores']:
            while True:
                memory_address = hex(random.randint(0, 0xFFFF))
                if memory_address not in memory_addresses:
                    memory_addresses.add(memory_address)
                    break
            entry['direccion_memoria'] = memory_address

            tabla_simbolos.append((f"LexToken {token_type}, {entry['valor']}, {entry['direccion_memoria']}"))