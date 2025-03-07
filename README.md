# LABORATORIO 01 

## Descripción General
- El siguiente laboratorio consiste en una serie de ejercicios para el desarrollo de programación en **sintaxis de Python**, además de evaluación de conceptos vistos en clases anteriores.
- El objetivo de este laboratorio está en el uso de la **condicional IF**, **creación de funciones**, recuerde que en cada función que desarrollen agregar los **comentarios** (nombre, parámetros entrada, salida y restricciones).
- Finalizado el laboratorio subir el archivo con el nombre de **Laboratorio01.py**, la entrega cierra a las **3pm del 3 de marzo del 2022** y será a través del Github Classroom



## calcularRenta(monto)
Implemente una función que ayude a calcular el valor a tributar por concepto del **impuesto de renta sobre el salario**. En la imagen adjunta viene el rango de salarios para aplicar el porcentaje correcto de los impuestos

Ilustración 1 Impuesto de renta para asalariados
![image](https://user-images.githubusercontent.com/1167750/156645626-d394119c-ec54-4368-8df4-0d4a09d2b186.png)
Fuente: https://www.hacienda.go.cr/contenido/14448-ejemplos-calculos-impuesto-sobre-la-renta

Cómo se calcula:

-	Si el salario es de 700,000 mensuales, no pago impuesto de renta, ¿por qué?, según la tabla estoy exento ya que este salario está por debajo de los 817,000 colones

-	Si mi salario es de un 1,000,000 de colones, entonces este ingreso está dentro del rango del 817,000 y 1,226,000 entonces el exente de este se le aplica un 10%, es decir: (1,000,000 – 817,000) * 10% = 18,300

-	Ahora, si mi salario es de 2,000,000, aplicaría el 15%, entonces:
  Menor a 817,000 no pago
  (1,226,000 – 817,000) * 10% = 40,900
  (2,000,000 – 1,226,000) * 15% = 116,100
  Entonces el impuesto de renta que tengo que pagar por un salario de 2,000,000 de colones es 157,000, que es el resultado de la suma 40,900 + 116,100

``` python
>>> calcularRenta(700000)
0
>>> calcularRenta(1000000)
18300
>>> calcularRenta(2000000)
157000

``` 

## contadorDigitos(num, digito)
Implemente una función llamada contadorDigitos(num, digito) donde se espera que la salida retorne el número de veces que el dígito aparece en el número. Ejemplo
``` python
>>> contadorDigitos(102039480, 0)
3
>>> contadorDigitos(132033483, 3)
4
``` 
