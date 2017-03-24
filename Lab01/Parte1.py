import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    fx = fxs[len(fxs)-1]
    plt.plot(esses)
    plt.title('Quadric Error X Steps')
    plt.ylabel('Quadric Error')
    plt.xlabel('Steps')
    plt.savefig('QuadricErrorXSteps.png')
    plt.show()
    
    
    print(fx)
    
    blue_patch = mpatches.Patch(color='blue', label='A')
    orange_patch = mpatches.Patch(color='orange', label='B')
    green_patch = mpatches.Patch(color='green', label='C')
    red_patch = mpatches.Patch(color='red', label='D')
    plt.legend(handles=[blue_patch,orange_patch,green_patch,red_patch],
               bbox_to_anchor=(0.9, 0.8),bbox_transform=plt.gcf().transFigure)
    plt.plot(fxs)
    plt.title('Parameter Values X Steps')
    plt.ylabel('Parameter Value')
    plt.xlabel('Steps')
    plt.savefig('ParameterValuesXSteps.png')
    plt.show()
    
    plt.plot(X,Y,'ro')
    x = np.arange(-5., 5.,0.1)
    plt.plot(x,fx[0]*x**3 + fx[1]*x**2 + fx[2]*x + fx[3])
    plt.title('Fited Curve')
    plt.savefig('FitedCurve.png')
    plt.show()
    
  



main()

    
    