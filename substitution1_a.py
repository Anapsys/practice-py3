#imports
from sympy import *
from sympy import symbols
init_printing()
# SYMPY NOTES:
#   https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html
#   -cannot write as xy, must include *. x*y.
#   -a + b = c written as Eq(a + b, c)
#   -expr = expr.subs(x,3) to substitute variables in equations.
#   -solve(eq, vars) 
#       or solveset(eq, vars,domain=s.reals)
#       RETURNS A LIST, use [0] if only expecting one solution
#   -EXPONENTS: ** symbol, NOT ^.

def solve_subs(xyTotal, numX, numY, valTotal):
    #var declarations
    DEBUG = false
    a,x,b,y,c,d = symbols('a x b y c d')

    #equation declarations
    expr_c = Eq(c, x + y)
    expr_y = Eq(y, c - x)
    expr_d = Eq(d, a*x + b*y)
    expr_dx = Eq(d, a*x + b*c - b*x)
    expr_dy = Eq(d, a*x + b*y)

    #step 1: get the equation to find y
    #           results: val d, equation for y
    expr_y = expr_y.subs(c, xyTotal)
    print('y=')
    pprint(solve(expr_y,y))
    print('')

    #step 2: get the total, and quantities
    #           results: vals a, b, d, eq d
    expr_d = expr_d.subs([(a, numX),(b,numY),(d,valTotal)])
    print('eq so far: ')
    pprint(expr_d)
    #pprint(solve(expr_d,x))
    print('')

    #step 3: subsitute y
    #           results: val x
    expr_dx = expr_dx.subs([(a, numX),(b,numY),(c,xyTotal),(d,valTotal)])
    pprint(expr_dx)
    newX = solve(expr_dx,x)[0]
    print(newX)
    print('')

    #step 4: substitute x
    #           results: val y
    expr_dy = expr_dy.subs([(a, numX),(b,numY),(c,xyTotal),(d,valTotal),(x,newX)])
    pprint(expr_dy)
    newY = solve(expr_dy,y)[0]
    print(newY)
    print('')

    #step 5: solution
    print('SOLUTION: x='+str(newX)+',y='+str(newY))

if __name__ == '__main__':
    xyTotal = input('Input the sum of x and y: ')
    numX = input('How many x?: ')
    numY = input('How many y?: ')
    valTotal = input('Totalling to...?: ')
    solve_subs(xyTotal, numX, numY, valTotal)