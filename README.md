# IntegrationFunctions
Some code for integrating functions, written in python
------------------------------------------------------------------------
Given we have a task of finding: I = integral(f(x)dx), x from a to b

SimpsonIntegration.py encorporates Simpson method for counting integrals

------------------------------------------------------------------------
FiloneIntegration.py finds an integral of the fast oscillating function
of the type:

I = integral(f(x)exp{w*x*i}dx), x from a to b; [i is an imaginary variable]

In more potent words:
I = int(f(x)cos{w*x}dx) + i*int(f(x)sin{w*x}dx)
