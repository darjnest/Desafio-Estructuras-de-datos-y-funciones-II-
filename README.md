# Desafio-Estructuras-de-datos-y-funciones-II-

## Descripción
La empresa de desarrollo de software DESARROLLA se encuentra actualmente trabajando
en muchos proyectos distintos. Es tanta la demanda que te solicita trabajar en 3 soluciones
que tienen pendientes. Para ello, te entregarán los requerimientos de cada tarea y deberás
implementar una función que entregue la solución a cada problema.

## Requerimientos
1. Filtrado Relevante
(3 Puntos)
La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
problema. Dada una muestra de los productos que actualmente se encuentran disponibles
en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
siguiente:
- ● Un diccionario con los productos que cumplen una cierta condición dado un umbral
- ● La función debe permitir mostrar los valores mayor que o menor que un umbral
(siempre estrictos).
- ● Por defecto la función debe siempre mostrar los valores mayor que el umbral a
menos que se indique lo contrario.
Para desarrollar la funcionalidad se le entrega a usted un diccionario de prueba para verificar
sus resultados.
![image](https://user-images.githubusercontent.com/36016296/168395504-daefdf6c-e490-4695-b713-ce8cf2e508ff.png)

Se espera ejecutar el programa de la siguiente manera:
- ● Si se especifica un argumento, este debe ser el umbral y por defecto debe calcular
los que son estrictamente mayores al umbral.

![image](https://user-images.githubusercontent.com/36016296/168395536-b804f550-8743-4e9e-9a75-7aa5b772f777.png)

- ● En caso de que se ingresen dos valores, el primero seguirá siendo el umbral,
mientras el segundo podrá tomar los valores mayor o menor. Por ejemplo, el
siguiente código calculará los que son estrictamente menores.

![image](https://user-images.githubusercontent.com/36016296/168395591-21da3caa-a88b-40c1-844a-5e58bd3aa316.png)

 ● En caso que otro elemento se utilice se debe devolver lo siguiente:
 
 ![image](https://user-images.githubusercontent.com/36016296/168395663-eea970c5-6ca0-4bbe-8c2d-6215d6ee13fb.png)


2. Alertas Telemáticas
(3 Puntos)
Otra solución que se encuentra pendiente es la encargada por una empresa de flotas que
debe medir mediante telemetría las velocidades de cada una de sus correas
transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que,
para poder entregar energía a las correas más lentas, es necesario ralentizar las más
rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se
requiere levantar una alerta de la posición de las correas transportadoras que están por
sobre el promedio.
- ● Para ello se pide determinar una funcionalidad que calcule el promedio de una lista
de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta
con mucha capacidad por lo que se pide no depender de librerías externas.
- ● Listar las posiciones de todas las correas transportadoras que están sobre el
promedio.
- ● Implementar la solución mediante una función en un archivo llamado velocidad.py.
Se entrega la siguiente lista con una muestra de velocidades para probar las
funcionalidades.

![image](https://user-images.githubusercontent.com/36016296/168395748-f49a90c9-85a8-4f6b-9593-35494d0a7455.png)

3. Apoyo Matemático
(4 Puntos)
Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda
escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos
operaciones conocidas como el factorial y la productoria y se requiere que usted prepare
una script que implemente esto.

El factorial se define de la siguiente forma:
𝑛! = 𝑛 * 𝑛 − 1 * 𝑛 − 2 * ... * 2 * 1

En un ejemplo práctico, el factorial de 5 (5!) se calculará como:
5! = 5 * 4 * 3 * 2 * 1 = 120

Por otro lado la productoria se define como la multiplicación de elementos.
𝐴 = [3, 6, 4, 2, 8]

∏ 𝐴
𝑖 = 3 * 6 * 4 * 2 * 8

Para resolver este programa se solicita lo siguiente:
- ● Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. Esta función se debe invocar
de la siguiente manera:

![image](https://user-images.githubusercontent.com/36016296/168395856-18959ee2-362b-4465-929f-59382eeada7d.png)

Se ingresarán un valor numérico como argumento con el nombre fact_i cuando se requiera
calcular un factorial, y una lista como argumento prod_i cuando se requiera calcular una
productoria. Cabe destacar que la función debe permitir ingresar estos argumentos en
cualquier orden y en cualquier cantidad. El resultado de la función se debe imprimir en
pantalla de la siguiente forma:

![image](https://user-images.githubusercontent.com/36016296/168395905-6ce40ad4-e72c-45fd-b10b-92fb176022fe.png)

![image](https://user-images.githubusercontent.com/36016296/168395925-a423989e-369b-42cd-9eef-dc54c67b667b.png)





