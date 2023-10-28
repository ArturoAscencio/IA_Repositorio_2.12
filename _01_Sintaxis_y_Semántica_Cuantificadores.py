from sympy import symbols, ForAll, Exists

# Definir variables
x, y, z = symbols('x y z')

# Cuantificador "para todo" (?)
expresion_universal = ForAll(x, x % 2 == 0)  # Para todo x, x es par

# Cuantificador "existe" (?)
expresion_existencial = Exists(y, y > 10)  # Existe algún y mayor que 10

# Evaluar las expresiones
resultado_universal = expresion_universal.simplify()
resultado_existencial = expresion_existencial.simplify()

print("Resultado del cuantificador universal:", resultado_universal)
print("Resultado del cuantificador existencial:", resultado_existencial)
