import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

def Foo(fx,x):
    aux = 1;
    ret = 0;
    for a in reversed(range(len(fx))):
        ret += aux * fx[a]
        aux *=x
    #print('Foo')
    #print(ret)
    return ret

def GradFoo(fx,x):
    ret = []
    aux = 1
    for a in range(len(fx)):
        ret.append(aux)
        aux *= x
    #print('GradFoo')
    #print(np.array(ret[::-1]))
    return np.array(ret[::-1])
        
def EsseFoo(fx,x,y):
    ret = 0
    for a in range(len(x)):
        ret += (y[a] - Foo(fx,x[a]))**2
    #print('EsseFoo')
    #print(ret)
    return ret

def GradEsseFoo(fx,x,y):
    ret = np.array([0.0,0.0,0.0,0.0])
    for a in range(len(x)):
        aux = y[a] - Foo(fx,x[a])
        ret += aux * GradFoo(fx,x[a])
    return -2*ret 

def Minimize(fx,x,y,learningRate,iterations):
    fxs = []
    esses = []
    fxs.append(np.array(fx))
    esses.append(np.array(EsseFoo(fx,x,y)))
    for i in range(iterations):
        fxs.append(fxs[i] - learningRate*GradEsseFoo(fxs[i],x,y))
        esses.append(np.array(EsseFoo(fxs[i],x,y)))
        
    return (fxs,esses)

def main():
    X = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    Y = [-53.9, -28.5, -20.7, -3.6, -9.8, 5.0, 4.2, 5.1, 11.4, 27.4, 44.0]
    #     a b c d
    fx = [0,0,0,0]
    (fxs,esses) = Minimize(fx,X,Y,1e-5,50)
    plt.plot(esses)
    plt.show()
    
  



main()

    
    