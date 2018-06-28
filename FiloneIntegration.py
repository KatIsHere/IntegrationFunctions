from cmath import sin, cos, exp
import numpy as np

def FiloneLinear(xNet, F_func, W):
    """returns integral of oscillating function of type: f(x) = y(x)*exp(1j*w*x)"""
    h = xNet[1] - xNet[0]
    N = len(xNet)
    sum = F_func(xNet[N-1]) * ( 1/(1j * W) + (1 - exp(-1j*W*h))/   \
                        (W**2 * h)) - F_func(xNet[0]) * ( 1/(1j * W) +   \
                        (exp(1j*W*h) - 1)/(W**2 * h) )
    for i in range(1, N-1):
        sum += 4 / (W**2 * h) * (sin(W*h / 2))**2 * F_func(xNet[i])
    return sum