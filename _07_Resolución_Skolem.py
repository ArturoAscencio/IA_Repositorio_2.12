from sympy import symbols, Or, And, Not, to_cnf
from sympy.logic.inference import resolution

# Definir variables
x, y = symbols('x y')

# Crear cláusulas
clausula1 = Or(And(x, y), And(x, Not(y)))
clausula2 = Or(Not(x), y)

# Convertir a la forma normal conjuntiva (CNF)
clausula1_cnf = to_cnf(clausula1, True)
clausula2_cnf = to_cnf(clausula2, True)

# Realizar resolución de Skolem
resultado = resolution(clausula1_cnf, clausula2_cnf)

# Imprimir el resultado
if resultado:
    print("Las cláusulas son resolubles")
else:
    print("Las cláusulas no son resolubles")
