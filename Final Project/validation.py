from origin15 import *

mtx1 = SquareMatrix([[1,2,3],[3,2,1],[-2,4,5]])
mtx2 = SquareMatrix([[34,-12,24,43],[12,23,-92,21],[6,-32,44,65],[0,1,9,13]])
mtx3 = SquareMatrix([[1,2,3,56,82],[-12,3,2,41,14],[14,34,21,4,-93],[13,34,23,13,-100],[23,-13,11,4,5,6]])
mtx4 = SquareMatrix([[0,41,93],[-12,0,32],[12,34,0]])
mtx5 = SquareMatrix([[0,-12,24,43],[6,0,-2,13],[6,-12,0,29],[0,1,9,19]])
mtx6 = SquareMatrix([[2,-1,0],[-1,2,-1],[0,-1,2]])
mtx7 = SquareMatrix([[1,-1,-1,-1],[-1,2,2,2],[-1,2,3,1],[-1,2,1,4]])
mtx8 = Matrix([[1, 2, 0, 7], [0, 1, -1, 4], [1, 3, 3, -8]])
mtx9 = Matrix([[132423, 4934, -123, 5486, 7], [34589, 3456, 3454, 9656, 7], [3453, -586, 24244, 111, 7], [1, 1, -1, -1, 7]])
mtx10 = SquareMatrix([[2, 2, 4, 0, 0], [0, 0, 1, 1, 0], [-1, -1, -2, 0, 0], [1, 1, 2, 0, 0], [-1, -1, -3, -1, 0]])
mtx11 = SquareMatrix([[9, 7, 3], [-9, -7, -4], [4, 4, 4]])
mtx12 = SquareMatrix([[0.9, 0.4], [0.1, 0.6]])
mtx13 = SquareMatrix([[9, -4, -2, -4], [-56, 32 ,-28, 44], [-14, -14, 6, -14], [42, -33, 21, -45]])
mtx14 = SquareMatrix([[1, 1, 2, 0 ,1], [0, 2, 1, 1, 0], [0, 0, 1, 1, 2], [0, 0, 0, 0, 1], [0, 0, 0, 0, 2]])
mtx15 = SquareMatrix([[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0], [1, 1, -1, 2]])
mtx16 = SquareMatrix([[4, 1, 0, -1], [0, 3, 0, 1], [0, 0, 4, 0], [1, 0, 0, 5]])
mtx21 = Matrix([[0, 5], [-2, 3], [1, 1]])
mtx17 = SquareMatrix([[-2, 0], [0, 0]])
mtx18 = SquareMatrix([[2, -1], [2, 2]])
mtx19 = Matrix([[6, -8, -4, 5, -4],[2, 7, -5, -6, 4],[0, -1, -8, 2, 2], [-1, -2, 4, 4, -8]])
mtx20 = Matrix([[1, 0, 1, 2], [-1, 0, -3, 0], [0, 1, -2 , -1]])
I = SquareMatrix.diag(4)


"""MATRIX SIMPLE FUNCTIONS"""
#print(I)
#print(mtx9)
#print(mtx9.rank())
#print(mtx8[0] + mtx8[1])
#print(mtx4.REF())
#print(mtx8.shape())
#print(mtx1)
#print(mtx1 ** 3)
#print(mtx1 * 3 * mtx4)
#print(mtx4 * mtx1)
#print(3 * mtx1 + mtx4)
#print(mtx3 - 3 * I)
#print(mtx1.rank())
#print(mtx8)
#for vec in mtx8.image(): print(vec.transpose())
#print(mtx8.transpose())
#print(mtx3.concat(I * 3))
"""EIGENVALUES, DIAGONALIZATION, JORDAN DECOMPOSITION, CHARACTERISTIC POLYNOMIAL"""
#print(mtx7)
#print(mtx7.eigenvalues())
#print(mtx6.eigenvalues())
#print(mtx5.charac_polynom())
#print(mtx3.det())

#print(mtx6)
#a, b, c = mtx6.eigendecomp()
#print(a)
#print(b)
#print(c)
#print(a*b*c)

#print(mtx7)
#A, B, C = mtx7.eigendecomp()
#print(A)
#print(B)
#print(C)
#print(A*B*C)

#print(mtx12)
#A, B, C = mtx12.eigendecomp()
#print(A)
#print(B)
#print(C)
#print(A*B*C)


#print(mtx14)
#A, B, C = mtx14.jordandecomp()
#print(A)
#print(B)
#print(C)
#print(A*B*C)

#print(mtx15)
#a, b, c = mtx15.jordandecomp()
#print(a)
#print(b)
#print(c)
#print(a*b*c)

#print(mtx16)
#a, b, c = mtx16.jordandecomp()
#print(a)
#print(b)
#print(c)
#print(a*b*c)

"""LU, PLU, CHOLESKY DECOMPOSITIONS"""
#print("LU(mtx1) = ", mtx1.LU())
#print("LU(mtx2) = ", mtx2.LU())
#print("LU(mtx3) = ", mtx3.LU())
#print("QR(mtx1) = ", mtx1.QR())
#print("QR(mtx2) = ", mtx2.QR())
#print("QR(mtx3) = ", mtx3.QR())

#print("LU(mtx4) = ", mtx4.LU())
#print("PLU(mtx4) = ", mtx4.PLU())

#print("LU(mtx5) = ", mtx5.LU())
#print("PLU(mtx5) = ", mtx5.PLU())

#print("Cholesky(mtx6) = ", mtx6.cholesky())
#print("Cholesky(mtx7) = ", mtx7.cholesky())

"""SVD, Polar, orthonormolization"""
# U, D, V = mtx21.SVD()
# print(U)
# print(D)
# print(V)
# print(U*D*V)

# U, D, V = mtx17.SVD()
# print(U)
# print(D)
# print(V)
# print(U*D*V)

# U, D, V = mtx18.SVD()
# print(U)
# print(D)
# print(V)
# print(U*D*V)


# U, D, V = mtx20.SVD()
# print(U)
# print(D)
# print(V)
# print(U*D*V)

# U, P = mtx7.polar_decomp()
# print(U)
# print(P)
# print(U*P)


# U, P = mtx6.polar_decomp()
# print(U)
# print(P)
# print(U*P)


# basis = [Matrix([i]) for i in mtx20.mat] 
# new_basis = Matrix.orthonormalization(basis) 
# print(new_basis)

# basis = [Matrix([i]) for i in mtx19.mat] 
# new_basis = Matrix.orthonormalization(basis)
# print(new_basis)


