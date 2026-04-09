from sympy import symbols,Eq, solve

#Deinir as variáveis:
x, y, z, a, b, c = symbols('x y z a b c')

equação = Eq(6*x, 2*x + 16)
resultao = solve(equação,x)
print(resultao)

equaçao = Eq(x**2 - 6*x + 7, 0)
print(solve(equaçao,x))

eq3 = Eq(x**2 + 3*x - 28, 0)
print(solve(eq3,x))

eq4 = Eq(4*x**2 + 8*x + 7, 0)
print(solve(eq4,x))

eq5 = Eq(x**2 + 8*x + 16, 0)
print(solve(eq5,x))

eq6 = Eq(x**3 - 7*x + 6, 0)
print(solve(eq6,x))