'''
* Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
* Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

'''

# Operadores aritméticos
num1 = 5
num2 = 3

print ("Operadores aritméticos")

suma = num1 + num2
print ("(+) Suma -> ", num1, "+", num2, "=", suma)
resta = num1 - num2
print ("(-) Resta -> ", num1, "-", num2, "=", resta)
multiplicacion = num1 * num2
print ("(*) Multiplicación -> ", num1, "*", num2, "=", multiplicacion)
division = num1 / num2
print ("(/) División -> ", num1, "/", num2, "=", division)
division_entera = num1 // num2
print ("(//) División entera -> ", num1, "//", num2, "=", division_entera)
resto = num1 % num2
print ("(%) Resto -> ", num1, "%", num2, "=", resto)
exponente = num1 ** num2
print ("(**) Exponenciación -> ", num1, "**", num2, "=", exponente)

# Operadores de comparación
print ("=" * 10)
print ("Operadores de comparación")

mayor_que = num1 > num2
print ("(>) Mayor que -> ", num1, ">", num2, "=", mayor_que)
menor_que = num1 < num2
print ("(<) Menor que -> ", num1, "<", num2, "=", menor_que)
igual_que = num1 == num2
print ("(==) Igual que -> ", num1, "==", num2, "=", igual_que)
mayor_o_igual_que = num1 >= num2
print ("(>) Mayor o igual que -> ", num1, ">=", num2, "=", mayor_o_igual_que)
menor_o_igual_que = num1 <= num2
print ("(<=) Menor o igual que -> ", num1, "<=", num2, "=", menor_o_igual_que)
diferente_que = num1 != num2
print ("(!=) Diferente que -> ", num1, "!=", num2, "=", diferente_que)


# Operadores lógicos
var1T = True
var1F = False
var2T = True
var2F = False
print ("=" * 10)
print ("Operadores lógicos")
print ("(and &) Devuelve True si ambos operandos son True")
print(f"""
{var1T} and {var2T} = {var1T & var2T}
{var1T} and {var2F} = {var1T & var2F}
{var1F} and {var2T} = {var1F and var2T}
{var1F} and {var2F} = {var1F and var2F}
""" )
print ("(or |) Devuelve True si alguno de los operandos es True")
print(f"""
{var1T} or {var2T} = {var1T | var2T}
{var1T} or {var2F} = {var1T | var2F}
{var1F} or {var2T} = {var1F or var2T}
{var1F} or {var2F} = {var1F or var2F}
""" )
print ("(not) Devuelve True si el operando es False")
print(f"""
not {var1T} = {not var1T}
not {var1F} = {not var1F}

""" )

# Operadores de asignación

print ("=" * 10)
print ("Operadores de asignación")
print(f"""
(=)  x = 5 significa que el valor 5 es asignado a la variable x
(+=) x += 5 es equivalente a x = x + 5
(-=) x -= 5 es equivalente a x = x - 5
(*=) x *= 5 es equivalente a x = x * 5
(/=) x /= 5 es equivalente a x = x / 5
(%=) x %= 5 es equivalente a x = x % 5
(//=) x //= 5 es equivalente a x = x // 5   
""" )

# Operadores de pertenencia"
lista = (10,20,30,40)
arreglo = ["uno", "dos", "tres"]
val1 = 10
val2 = 50
val3 = "dos"
val4 = "cuatro"
print ("=" * 10)
print ("Operadores de pertenencia")
print(f"""
(in) devuelve True si el valor especificado se encuentra en la secuencia
{val1} está en la lista {lista} -> {val1 in lista}
{val2} está en la lista {lista} -> {val2 in lista} 

(not in) devuelve True si el valor especificado NO se encuentra en la secuencia
{val3} NO está en el arreglo {arreglo} -> {val3 not in arreglo}
{val4} NO está en el arreglo {arreglo} -> {val4 not in arreglo} 
""" )


# Operadores de identidad
val1 = 10
val2 = 50
val3 = 50
val4 = "cuatro"
print ("=" * 10)
print ("Operadores de identidad")
print(f"""
(is)  devuelve True si los operandos se refieren al mismo objeto
{val1} es {val2} -> {val1 is val2}
{val2} es 50 -> {val1 is 50}

(is not) devuelve True si los operandos no se refieren al mismo objeto
{val1} no es {val2} -> {val1 is not val2}
{val2} no es {val3} -> {val1 is not val3} 
""" )

a = 3
b = 3  
c = 4
print (a is b) # muestra True
print (a is not b) # muestra False
print (a is not c) # muestra True

# Operadores de bits


'''
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...

'''

# Condicional
print ("=" * 10)
print ("Condicionales --> IF")
edad = 45
print(f"La edad es: {edad}")
if edad >= 60:
    print ("Es tercera edad")
elif edad >=18 and edad <60:
    print ("Es una adulto")
elif edad >=12 and edad <18:
    print ("Es un adolescente")
else:
    print ("Es un niño")

# Iterativas
print ("=" * 10)
print ("Ciclos - FOR")
for i in range (1,11):
    print(i) #imprime del 1 al 10

print ("Ciclos - WHILE")
i = 1
while i <=10:
    print(i)
    i += 1

# Excepciones
try:
	# Codigo a ejecutar
    print (100/0)
	# Pero podria haber errores en este bloque
    
except:
	# Haz esto para manejar la excepcion
    print ("ERROR: División entre 0")
	# El bloque except se ejecutara si el bloque try lanza un error
    
finally:
	# Este bloque se ejecutara siempre
    print ("Fin")

# EXTRA
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print ("=" * 10)
print ("EXTRA")
for i in range (10,56):
    if (i % 2) == 0 and i != 16 and (i % 3) != 0 :
        print (i)