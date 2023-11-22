

#ip_prueba = ['192.168.125.30','127.100.50.30']
#from Lexico import evaluarsemantica
#evaluarsemantica

def es_direccion_ip_publica(direccion_ip):
    octetos = [int(octeto) for octeto in direccion_ip.split('.')]
    return 1 <= octetos[0] <= 126 or 128 <= octetos[0] <= 191 or 192 <= octetos[0] <= 223 or 224 <= octetos[0] <= 239 or 240 <= octetos[0] <= 255

def es_direccion_ip_privada(direccion_ip):
    octetos = [int(octeto) for octeto in direccion_ip.split('.')]
    return octetos[0] == 10 or (octetos[0] == 172 and 16 <= octetos[1] <= 31) or (octetos[0] == 192 and octetos[1] == 168)

def es_direccion_ip_reservada(direccion_ip):
    direcciones_reservadas = ['0.0.0.0', '127.0.0.1']
    return direccion_ip in direcciones_reservadas

def clasificar_direcciones_ip(direcciones_ip):
    resultados_clasificacion = []
    for direccion_ip in direcciones_ip:
        if es_direccion_ip_publica(direccion_ip):
            resultados_clasificacion.append(("Pública", direccion_ip))
        elif es_direccion_ip_privada(direccion_ip):
            resultados_clasificacion.append(("Privada", direccion_ip))
        elif es_direccion_ip_reservada(direccion_ip):
            resultados_clasificacion.append(("Reservada", direccion_ip))
        else:
            resultados_clasificacion.append(("Desconocida", direccion_ip))
    return str(resultados_clasificacion)


# No es necesario asignar ip_prueba a direccion_ip, puedes pasarla directamente a la función
#resultados = clasificar_direcciones_ip(ip_prueba)

# Imprimir los resultados
#for resultado in resultados:
    #print(resultado)
    #imprime bien los resultados cuando se asigna cadena con las ip como caracteres