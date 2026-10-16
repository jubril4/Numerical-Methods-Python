#Python program choleskidecomposition.py finds corresponding x #Software used - Python version 3.8

#IDE used PyCharm Community Edition 2020.2

#numpy package is imported and standard packages

import numpy as np

import math

import sys

import stdio

# choleski function

def choleski(A):

#length is calculated

m =len(A);

#decomposition

for y in range(m):

#sqrt is calculated to find the constant

A[y,y]=math.sqrt(A[y,y] - np.dot(A[y,0:y],A[y,0:y]))

for s in range(y+1,m):

A[s,y]=(A[s,y]- np.dot(A[s,0:y],A[y,0:y]))/A[y,y]

# decomposed values are updated in the same matrix

for y in range(1,m):

A[0:y,y]=0.0

return A;

#To solve Ax=B

def choleskisol(L,B):

#length is calculated

m=len (B)

# Ly=B

for y in range(m):

B[y]=(B[y]-np.dot(L[y,0:y],B[0:y]))/L[y,y]

for y in range(m-1,-1,-1):

B[y]=(B[y]-np.dot(L[y+1:m,y],B[y+1:m]))/L[y,y]

return B

#input coefficient matrix

A =np.array([[1,1,1],

[1,2,2],

[1,2,3]])

B=np.array([1.1,0.0,-2.3])

print(" The given matrix A is: \n",A)

print(" The given matrix B is: \n",B)

Aorig= A.copy()

#decomposition is invoked

L=choleski(A)

print(" The decomposed matrix:\n", L)

#the solution is resolved

X=choleskisol(L,B)

print(" The solution matrix X is:\n")

print("x=", X)

print(" The condition is checked AX=B")

print(" A*x=\n", np.dot(Aorig,X))