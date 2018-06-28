import numpy as np

def SimpsonElement(F, xOld, xNew):
    """returns element of a sum in Simpsons numerical fourmula
    xOld for x[i-1], xNew for x[i]"""
    h = xNew - xOld
    return (F(xOld) + 4*F(xNew - h / 2) + F(xNew))*h / 6

def SimpsonSum(F, fromA, toB, N = 200):
    """returns integral of F(x) throu the Simpson's numerical formula with given dots"""
    xNet = np.linspace(fromA, toB, N)
    return sum([SimpsonElement(F, xNet[i-1], xNet[i]) for i in range(1,len(xNet))])
