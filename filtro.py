import sys 

precios = { 
    'Notebook' : 700000,
    'Teclado' : 25000,
    'Mouse' : 12000,
    'Monitor' : 250000,
    'Escritorio' : 1350000,
    'Tarjeta de video' : 1500000
}

def filtrar_productos(umbral,condicion='mayor'):
    if condicion == 'mayor':
        filtrados = {k: v for k,v in precios.items() if v > umbral}
    elif condicion == 'menor': 
        filtrados = {k: v for k, v in precios.items() if v < umbral}
    else : 
        return "Lo sentimos, no es una operacion valida"
    
    return filtrados

if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    resultado = filtrar_productos(umbral)
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    condicion = sys.argv[2]
    resultado = filtrar_productos(umbral,condicion)
else: 
    print("Lo sentimos , los argunmentos no son validos.")
    sys.exit(1)

if isinstance(resultado,dict):
    productos = ', '.join(resultado.keys())
    if condicion == 'menor':
        print(f"los productos menores al umbral son: {productos}")
    else:
        print(f"los productos mayores al umbral son: {productos}")
else:
    print(resultado)
    
