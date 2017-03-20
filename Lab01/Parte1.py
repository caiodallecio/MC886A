x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [-53.9, -28.5, -20.7, -3.6, -9.8, 5.0, 4.2, 5.1, 11.4, 27.4, 44.0]
#     a b c d
fx = [1,1,1,1]

def Foo(fx,x):
    aux = 1;
    ret = 0;
    for a in reversed(range(fx)):
        ret += aux * fx(a)
        aux *=x
    return ret

def GradFoo(x):
    ret = []
    aux = 1
    for a in reversed(range(fx)):
        ret(a) = aux
        aux *= x
    return ret
        