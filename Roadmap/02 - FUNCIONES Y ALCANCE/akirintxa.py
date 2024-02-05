""" /*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""


def tipo_uno():
    print("tipo_uno: Función sin parámetros ni retorno")


tipo_uno()


def tipo_dos(num1, num2):
    return num1 * num2


tipo2 = tipo_dos(3, 5)
print(
    f"tipo_dos: Recibe dos parámetros y devuelve la multiplicación: 3 * 5 = {tipo2}")

var_global = 10


def tipo_tres(a, b):
    var_global = a + b
    return (var_global)


print(f"La función tipo_tres: {tipo_tres(2, 2)}")
print(f"var_global: {var_global}")


def extra(texto1, texto2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(texto1 + texto2)
        elif number % 3 == 0:
            print(texto1)
        elif number % 5 == 0:
            print(texto2)
        else:
            count += 1
            print(number)

    return count


print(extra("plis", "plas"))
