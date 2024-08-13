def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def calcular_productoria(lista):
    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def calcular(**kwargs):
    resultados = []
    
    for key, value in kwargs.items():
        if 'fact_' in key:
            resultado = calcular_factorial(value)
            resultados.append(f"El factorial de {value} es {resultado}")
        elif 'prod_' in key:
            resultado = calcular_productoria(value)
            resultados.append(f"La productoria de {value} es {resultado}")
        else:
            resultados.append(f"No se reconoce la operación para {key}")

    for resultado in resultados:
        print(resultado)

    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
    calcular(prod_2=[4, 6, 7, 4, 3], fact_3=4)
