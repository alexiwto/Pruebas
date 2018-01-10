x = (int(raw_input('Introduce el numero limite hasta el que llegara la serie fibonacci: ')))

def fib(n):
        a = 0
        b = 1
        while b < n:
                print b,
                #Los valores de las variables a la derecha del = están asignados antes de hacer la operación.
                a, b = b, a+b
fib(x)
