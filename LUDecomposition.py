# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [1, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A)

print "A:"
pprint.pprint(A)

print "P:"
pprint.pprint(P)

print "L:"
pprint.pprint(L)

print "U:"
pprint.pprint(U)

# <codecell>

import pprint

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    # Converts N into a list of tuples of columns                                                                                                                                                                                                      
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication                                                                                                                                                                                     
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values                                                                                                                                                                                            
    id_mat = [[float(i ==j) for i in xrange(m)] for j in xrange(m)]

    # Rearrange the identity matrix such that the largest element of                                                                                                                                                                                   
    # each column of M is placed on the diagonal of of M                                                                                                                                                                                               
    for j in xrange(m):
        row = max(xrange(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows                                                                                                                                                                                                                            
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)                                                                                                                                                                                        
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U                                                                                                                                                                                                                 
    L = [[0.0] * n for i in xrange(n)]
    U = [[0.0] * n for i in xrange(n)]

    # Create the pivot matrix P and the multipled matrix PA                                                                                                                                                                                            
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)

    # Perform the LU Decomposition                                                                                                                                                                                                                     
    for j in xrange(n):
        # All diagonal entries of L are set to unity                                                                                                                                                                                                   
        L[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}                                                                                                                                                                                      
        for i in xrange(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in xrange(i))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )                                                                                                                                                                  
        for i in xrange(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in xrange(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)


A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]
P, L, U = lu_decomposition(A)

print "A:"
pprint.pprint(A)

print "P:"
pprint.pprint(P)

print "L:"
pprint.pprint(L)

print "U:"
pprint.pprint(U)

# <codecell>

from fractions import Fraction

#	Show Matrix
def show(header, mtrx):
	print header, "-------"
	for i in range(0, len(mtrx)):
		for j in range(0, len(mtrx)):
			if mtrx[i][j] == int(mtrx[i][j]):
				print "{0:8d}".format(int(mtrx[i][j])),
			else:
				tmp = Fraction.from_float(mtrx[i][j]).limit_denominator()
				print " "*(7-len(str(tmp))),
				print tmp,
		print ""
	print ""

#	LU decomposition by Crout algorithm [usage: L, U = ludec(A)]
def ludec(A):
	L = [[0.0 for i in range(len(A))] for j in range(len(A))]
	U = [[0.0 for i in range(len(A))] for j in range(len(A))]
	try:
		for i in range(0, len(A)):
			L[i][0] = A[i][0]			#	L:deside 1 column.
			U[0][i] = A[0][i]/A[0][0]	#	U:deside 1 row.
		for k in range(1, len(A)):
			for i in range(0, k):
				L[i][k] = U[k][i] = 0.0	#	initialize the element to be updated.
			for i in range(k, len(A)):
				L[i][k] = A[i][k]
				for m in range(0, k):
					L[i][k] -= L[i][m] * U[m][k]
			U[k][k] = 1.0				#	U:diagonal element is 1
			for i in range(k + 1, len(A)):
				U[k][i] = A[k][i]
				for m in range(0, k):
					U[k][i] -= L[k][m] * U[m][i]
				U[k][i] /= L[k][k]
	except ZeroDivisionError:
		print "This matrix can't do LU Decomposition."
	return L, U

A = [
	[, 16.0, 24.0, 20.0],
	[2.0, 7.0, 12.0, 17.0],
	[6.0, 17.0, 32.0, 59.0],
	[7.0, 22.0, 46.0, 105.0]
]

show("Original Matrix", A)
L, U = ludec(A)
show("L", L)
show("U", U)

# <codecell>


# <codecell>


