import itertools as it
import re
import random as rdm
from copy import *
from math import ceil
import sys
import numpy as np
sys.setrecursionlimit(2000)
listadd = lambda x, y, c = 1: [x[i] + y[i] * c for i in range(len(x))]

scale = lambda row, y: [row[i] * y for i in range(len(row))]

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

class SizeError(Exception):
    pass

class EigenvaluesError(Exception):
    pass

class ConditionsError(Exception):
    # Occurs if some of the conditions for performing the task were not satisfied #
    pass

def new_round(n): #Округление для вычислений
    eps = 0.001
    if abs(round(n) - n) < eps: return round(n)
    else: return n

def roots_round(n): #Округление для корней
    eps = 0.01
    if abs(round(n) - n) < eps: return round(n)
    else: return n

class Polynomial():

    def __init__(self, order, coeffs): # order - количество коэффициентов, coeffs = [лист из коэффициентов полинома]
        self.order = order
        self.coeffs = coeffs
        self.string = ""
        for i in range(self.order):
            self.string += f"({self.coeffs[i]}) * (x ** {self.order - i - 1}) + " 
        self.string = self.string[:-2]
        self.string = self.string.replace(' * (x ** 0)', '').replace('(x ** 1)', '(x)').replace('(1) * ', '')

    def eval(self, x): # возвращает значение полинома при аргументе х
        return eval(re.sub('x', f'({x})', self.string))

    def __repr__(self):
        return self.string

    def derivative(self, x): # возвращает значение производной при х = х
        dx = 0.0001
        if (self.eval(x + dx) - self.eval(x - dx))/(2 * dx) == 0.0: dx *= 10
        return (self.eval(x + dx) - self.eval(x - dx))/(2 * dx)

    def root(self, p = 1.5): # возвращает один корень полинома
        #if self.order == 3:
        #    d = (self.coeffs[1])** 2 - 4 * (self.coeffs[0]) * (self.coeffs[1])
        #    print(d)
        #    return (- (self.coeffs[1]) + (d) ** (0.5))/(2 * self.coeffs[0])
        delta = 0.000001 #0.000001
        if abs(new_round(self.eval(p) - 0)) < delta: 
            return p#<-----------------------------------------
        else:
            new_p = p - self.eval(p)/self.derivative(p)
            return self.root(p = new_p)

    def div(self, n): # возвращает полином поделенные на (х - n), предусмотрено только целое деление
        res = [self.coeffs[0]]
        for i in range(1, self.order ):
            res.append(n * res[-1] + self.coeffs[i])
        res = list(map(new_round, res))
        return Polynomial(self.order - 1, res[:-1])

    def roots(self): # возвращает лист из корней полинома
        if self.order == 2: return [self.coeffs[-1]]
        res = []
        pol = self
        for i in range(self.order):
            try: 
                
                r = pol.root()
            except RecursionError: return 'Algorithm has failed.'
            res.append(r)
            if pol.order != 2:
                try: 
                    r = pol.root()
                except: raise EigenvaluesError
                pol = pol.div(r)
        res = list(map(new_round, res))
        return res[:-1]

    def new_root(self, p0 = 5, p1 = 10):
        delta = 0.0001
        if abs(p1 - p0) < delta: 
            return new_round(p1)
        else:
            p2 = p1 - (self.eval(p1)*(p1 - p0))/(self.eval(p1) - self.eval(p0))
            return self.new_root(p1, p2)

    def new_roots(self):
        res = []
        pol = self
        for i in range(self.order):
            r = pol.new_root() 
            res.append(r)
            if pol.order != 2: 
                pol = pol.div(r)
        for r in res[:-1]: 
            if abs(self.eval(r) - 0) > 1: return 'Complex Roots'  
        return res[:-1]

class Matrix():

    def __init__(self, mat): #mat = лист из листов с коэффициентами матрицы
        if mat == [] or [[]]:
            self.rows, self.cols = 1, 1 
            self.mat = [[1]]
        self.rows, self.cols = len(mat), len(mat[0])
        self.mat = mat

    def transpose(self):
        new_mat = []
        for j in range(self.cols):
            row = [self.mat[i][j] for i in range(self.rows)]
            new_mat.append(row)
        if isinstance(self, SquareMatrix): return SquareMatrix(new_mat)
        else: return Matrix(new_mat)

    def __str__(self):
        return re.sub("], ", "]\n ", self.mat.__str__())

    def __repr__(self):
        return '\n' + re.sub("], ", "]\n ", self.mat.__str__())
    
    def __eq__(self, mat2):
        if self.shape() != mat2.shape():
            raise SizeError
        else:
            cnt = 0
            for i in range(self.rows):
                for j in range(self.cols):
                    if mat2.mat[i][j]==self.mat[i][j]:
                        cnt+=1
            if cnt == self.rows*self.cols:
                return True
            else:
                False

    def shape(self):
        return (self.rows, self.cols)

    def interchange(self, i, j): # свап двух колон под номерами i, j внутри матрицы
        temp = self.mat[i]
        self.mat[i] = self.mat[j]
        self.mat[j] = temp

    def make_mat(system): # делает матрицу из системы(лист) векторов, только для векторов класса Matrix
        if system[0].shape()[1] == 1:
            matr = [vect.transpose().mat[0] for vect in system]
        else: 
            matr = [vect.mat[0] for vect in system]
        try: 
            return SquareMatrix(matr)
        except: 
            return Matrix(matr)

    def __add__(self, mat2):
        if self.shape() != mat2.shape():
            raise SizeError
        else:
            new_mat = []
            for j in range(self.shape()[0]):
                row = [self.mat[j][i] + mat2.mat[j][i] for i in range(self.shape()[1])]
                new_mat.append(row)
            try: 
                return SquareMatrix(new_mat)
            except: 
                return Matrix(new_mat)

    def __sub__(self, mat2):
        if self.shape() != mat2.shape():
            return "Sizes are different"
        else:
            new_mat = []
            for j in range(self.rows):
                row = [self.mat[j][i] - mat2.mat[j][i] for i in range(self.cols)]
                new_mat.append(row)
            try: 
                return SquareMatrix(new_mat)
            except: 
                return Matrix(new_mat)

    def __len__(self):
        return (self.rows, self.cols)

    def __iadd__(self):
        pass

    def __rmul__(self, n):
        if isinstance(n, int) or isinstance(n, float): 
            new_mat = []
            for j in range(self.rows):
                row = [self.mat[j][i] * n for i in range(self.cols)]
                new_mat.append(row)
            try: 
                res = SquareMatrix(new_mat)
            except: 
                res = Matrix(new_mat)
            res.trunc_matrix()
            return res

    def __mul__(self, n):

        if isinstance(n, int) or isinstance(n, float): 
            new_mat = []
            for j in range(self.rows):
                row = [self.mat[j][i] * n for i in range(self.cols)]
                new_mat.append(row)
            try: 
                res = SquareMatrix(new_mat)
            except: 
                res = Matrix(new_mat)
            res.trunc_matrix()
            return res

        if isinstance(n, Matrix) or isinstance(n, SquareMatrix):
            if self.shape()[1] != n.shape()[0]: return "Error, sizes are different."
            res = []

            for i in range(self.shape()[0]): #0 - 2
                row = [0 for k in range(n.shape()[1])]
                for j in range(self.shape()[1]):
                    row = listadd(row, scale(n.mat[j], self.mat[i][j]))
                res.append(row)
            try: 
                res = SquareMatrix(res)
            except: 
                res = Matrix(res)
            res.trunc_matrix()
            return res

    def __getitem__(self, sep):
        if type(sep) == type(3):
            return Matrix([self.transpose().mat[sep]]) # <-------- если не пашет, то убрать

        if isinstance(sep, slice):
            start, end, step = sep.start, sep.stop, sep.step
            if start == end == None:
                start, end = 0, self.shape()[1]
            if start == end: return Matrix([[]])
            if start == None and end != None: start = 0
            if start != None and end == None: end = self.shape()[1]
            if end == 0 or start == len(self.mat[0]): return Matrix([[]])
            return Matrix([self[i].mat[0] for i in range(start, end)]).transpose()
        if isinstance(sep, tuple):
            cols_mat = self[sep[0]].transpose()[sep[1]].transpose()
            return cols_mat

    def concat(self, mat, mode = 'right'): # присоединяет одну матрицу к другой, необходимо указать 'mode' - либо справа, либо снизу
        if self.mat == [[]]: 
            return mat
        if mat.mat == [[]]:
            return self
        if mode == 'right' and len(self.mat) == len(mat.mat):
            n_rows = len(self.mat)
            res = []
            for j in range(n_rows):
                if isinstance(mat.mat[j], list): res.append(self.mat[j] + mat.mat[j]) 
                else: res.append(self.mat[j] + [mat.mat[j]])
            try: 
                return SquareMatrix(res)
            except: 
                return Matrix(res)

        if mode == 'bottom' and len(self.mat) == len(mat.mat):
            res = []
            for row in self.mat:
                res.append(row)
            for row in mat.mat:
                res.append(row)
            try: 
                return SquareMatrix(res)
            except: 
                return Matrix(res)

    def trunc_matrix(self): # округляет значения матрицы, необходимо делать при вычислениях
        for i in range(len(self.mat)):
            #self.mat[i] = list(map(approx, list(map(trunc, self.mat[i]))))
            self.mat[i] = list(map(new_round, self.mat[i]))

    def __setitem__(self, key, value): # это fignya
        print(key, value)

    def isnull(self): # Проверка является ли нулевой матрицей
        for row in self.mat:

            for elem in row:
                if elem != 0: return False
        return True

    def REF(self): 
        cef = deepcopy(self)
        pivot_n = 0
        def getPivot(mat, n):
            for i in range(pivot_n, mat.shape()[0]):
                if mat.mat[i][n] != 0: 
                    return (i, n)
            res = getPivot(mat, n + 1)
            return (res[0], res[1])

        finished = False
        while not finished:
            if pivot_n == min(cef.shape()[0]- 1, cef.shape()[1] - 1): 
                finished = True
            pivot_pos = getPivot(cef, pivot_n)
            pivot_col = pivot_pos[1]
            pivot_row = pivot_pos[0]

            

            if pivot_n != pivot_row: 
                cef.interchange(pivot_row, pivot_n)
                pivot_row = pivot_n
            if cef.mat[pivot_row][pivot_col] != 1:
                cef.mat[pivot_row] = scale(cef.mat[pivot_row], (1/cef.mat[pivot_row][pivot_col])) 
                cef.trunc_matrix()
            for i in range(pivot_n + 1, cef.shape()[0]):
                if cef.mat[i][pivot_col] == 0: continue
                else:
                    cef.mat[i] = listadd(cef.mat[i], cef.mat[pivot_row], -cef.mat[i][pivot_col]) 
            pivot_n += 1
        return cef

    def rank(self):
        m = self.REF()
        count = 0
        for i in range(m.shape()[0]):
            for j in range(m.shape()[1]):
                if m.mat[i][j] != 0:
                    count += 1
                    break
        return count

    def defect(self):
        return self.shape()[1] - self.rank()

    def image(self):
        m = self.REF()
        cols = [ ]
        
        for i in range(m.shape()[0]):
            for j in range(m.shape()[1]):
                if m.mat[i][j] != 0:
                    cols.append(j)
                    break
        system = [self[elem].transpose() for elem in cols]
        return system

    def gs_cofficient(u, v):
        cof1 = 0
        cof2 = 0
        for i in range(max(u.shape())):
            cof1 += u.mat[0][i]*v.mat[0][i]
        for j in range(max(u.shape())):
            cof2+= u.mat[0][j]*u.mat[0][j]
        coff = cof1/cof2
        new_vec = u * coff
        return new_vec
    
    def sub_vectors(u, v):
        new_vec = []
        for i in range(len(u)):
            new_vec.append(u[i]-v[i])
        return new_vec
    
    def orthogonalization(system):

        if system[0].shape()[1] == 1:
            system = list(map(Matrix.transpose, system))
        new_vectors = []
        for j in range(len(system)):
            if j==0:  
                new_vectors.append(system[j])
            else:
                k = system[j]
                for u in new_vectors:
                    k = k - Matrix.gs_cofficient(u, system[j])
                k.trunc_matrix()
                new_vectors.append(k)
        return new_vectors

    def normalization_vector(u):
        cnt = 0
        for i in range(max(u.shape())):
            cnt += u.mat[0][i]**2
        cnt = 1/(cnt **(0.5))
        new_vec = u * cnt
        return new_vec

    def normalization_system(system):
        new_system = []
        for j in range(len(system)):
            new_system.append(Matrix.normalization_vector(system[j]))
        return new_system

    def orthonormalization(system):
        orthogonal_system = Matrix.orthogonalization(system)
        orthonormal_system = Matrix.normalization_system(orthogonal_system)
        return orthonormal_system

    def creatediag_svd(l, m, n): #возвращает диагональную матрицу с элементами из листа l по диагонали сайз н на м
        return Matrix([[l[i] if i == j else 0 for j in range(m)] for i in range(n)]) 
    
    def matrix_round(self): #возвращает матрицу с округленим раунд используется внутри СВД
        arr = []
        for i in range(self.rows):
            new = []
            for j in range(self.cols):
                new.append(round(self.mat[i][j]))
            arr.append(new)
        
        T = Matrix(arr)
        return T
                
                        
    
  
    def SVD(self):
        n = self.shape()[0]
        m = self.shape()[1]
        A_adjoint_A = self.transpose()*self
        A_A_adjoint = self * self.transpose()
        
        
        eigenvectors = A_adjoint_A.eigenvectors()
        evalue =[i for i in eigenvectors.keys()]
        evalue.sort()
        evalue.reverse()
        #print(evalue)

        system = []
        for pack in evalue:
            if isinstance(eigenvectors[pack], Matrix): system.append(eigenvectors[pack])
            else:
                if isinstance(eigenvectors[pack], list):
                    for vect in eigenvectors[pack]:
                        system.append(vect)
        
        evectors = Matrix.make_mat(system)
        basis = [Matrix([i]) for i in evectors.mat] 
        new_basis = Matrix.orthonormalization(basis) 
        VT = Matrix.make_mat(new_basis)
        V = VT.transpose()
        D = Matrix.creatediag_svd([eig **(0.5) for eig in evalue], m, n)


        eigenvectors2 = A_A_adjoint.eigenvectors()
        evalue2 =[i for i in eigenvectors2.keys()]
        evalue2.sort()
        evalue2.reverse()
        #print(evalue2)

        system2 = []
        for pack in evalue2:
            if isinstance(eigenvectors2[pack], Matrix): system2.append(eigenvectors2[pack])
            else:
                if isinstance(eigenvectors2[pack], list):
                    for vect in eigenvectors2[pack]:
                        system2.append(vect)
        
        evectors2 = Matrix.make_mat(system2)
        basis2 = [Matrix([i]) for i in evectors2.mat] 
        new_basis2 = Matrix.orthonormalization(basis2) 
        UT = Matrix.make_mat(new_basis2)
        U = UT.transpose()
        ID = SquareMatrix.creatediag([-1 for i in range(U.size)])
        U_min = U*ID
        
        F = (U*D*VT).matrix_round()
        

        if F == self:
            #print(U*D*VT)
            return (U, D, VT)
        else:
            #print(U_min*D*VT)
            return (U_min, D, VT)
        

class SquareMatrix(Matrix):

    def __init__(self, mat):
        if len(mat) != len(mat[0]): return "Error"
        super().__init__(mat)
        self.size = len(mat)

    def reflect(self):
        mat = [[self.mat[-i][-j] for j in range(1, self.size + 1)] for i in range(1, self.size + 1)]
        return SquareMatrix(mat)

    def __add__(self, mat2):
        if self.shape() != mat2.shape():
            return "Sizes are different"
        else:
            new_mat = []
            for j in range(self.size):
                row = [self.mat[j][i] + mat2.mat[j][i] for i in range(self.size)]
                new_mat.append(row)
            return SquareMatrix(new_mat)

    def inverse(self):
        if self.det() == 0: return "NotInvertible"
        else:
            O = SquareMatrix.null(self.size)
            for i in range(self.size):

                for j in range(self.size):
                    O.mat[i][j] = (-1) ** (i + j) * self.cofactor(i, j).det()
            O = O.transpose() * (1/self.det())
            return O

    def det(self):
        if not isinstance(self, SquareMatrix): return 'TypeError: has to be a square matrix.'
        if self.shape() == (2, 2): return (self.mat[0][0] * self.mat[1][1]) - (self.mat[0][1] * self.mat[1][0])
        if self.shape() == (1, 1): return self.mat[0][0]
        res = 0
        for i in range(self.size):
            if self.mat[0][i] == 0: continue
            res += (-1) ** (i + 2) * self.mat[0][i] * self.cofactor(0, i).det()
        return res

    def __add__(self, mat2):
        if self.shape() != mat2.shape():
            raise SizeError
        else:
            new_mat = []
            for j in range(self.size):
                row = [self.mat[j][i] + mat2.mat[j][i] for i in range(self.size)]
                new_mat.append(row)
            return SquareMatrix(new_mat)

    def __sub__(self, mat2):
        if self.shape() != mat2.shape():
            return "Sizes are different"
        else:
            new_mat = []
            for j in range(self.size):
                row = [self.mat[j][i] - mat2.mat[j][i] for i in range(self.size)]
                new_mat.append(row)
            return SquareMatrix(new_mat)

    def __pow__(self, n):
        if isinstance(n, int):
            if n == 0: return SquareMatrix.diag(self.size)
            for i in range(n):
                if i == 0: res = self
                else: res *= self
            return res

    def trace(self):
        sum = 0
        for i in range(self.size):
            sum += self.mat[i][i]
        return sum

    def diag(size): # возвращает единичную матрицу размера size
        m = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(1) if i == j else row.append(0)
            m.append(row)
        return SquareMatrix(m)

    def null(size): # возвращает нулевую матрицу размера size
        mat = [[0 for j in range(size)] for i in range(size)]
        return SquareMatrix(mat)

    def cofactor(self, b, a):# Возвращает матрицу кофактор с индексами b, a
        col_excluded = Matrix.concat(self[:a], self[(a+1):]).transpose()
        return SquareMatrix(col_excluded[:b].concat(col_excluded[b+1:]).transpose().mat)

    def charac_polynom(self): # возвращает характеристический полином

        def signs(coeffs):
            if len(coeffs) % 2 == 0: #EnvironmentError
                for i in range(len(coeffs)):
                    if i % 2 == 0: coeffs[i] = -coeffs[i] 
            else:
                for i in range(len(coeffs)):
                    if i % 2 == 1: coeffs[i] = -coeffs[i]

        res = [1]#<----
        for i in range(1, self.size):
            order = self.size - i
            sum = 0
            for tuple in list(it.combinations(range(self.size), order)):
                sum += SquareMatrix(self.principal_minor(tuple).mat).det()
            res.append(sum)#<--------------------------
        res.append(self.det())#<------------
        signs(res)
        return Polynomial(len(res), res)

    def principal_minor(self, tuple): # tuple of indices of rows and columns which to cross (0, 2, 3)
        # Возвращает главный минор, с зачеркнутыми индексами строк в tuple
        if tuple == None: return self
        res1 = Matrix([[]])
        for i in range(len(tuple)):
            if i == 0: 
                res1 = Matrix.concat(res1, self[:tuple[i]])
                continue
            res1 = Matrix.concat(res1, self[tuple[i - 1] + 1:tuple[i]])
        res1 = Matrix.concat(res1, self[tuple[-1] + 1:])
            
        res1 = res1.transpose()
        res2 = Matrix([[]])
        for i in range(len(tuple)):
            if i == 0: 
                res2 = Matrix.concat(res2, res1[:tuple[i]])
                continue
            res2 = Matrix.concat(res2, res1[tuple[i - 1] + 1:tuple[i]])
        res2 = Matrix.concat(res2, res1[tuple[-1] + 1:])
        return res2.transpose()

    def ker(self): # возвращает лист с матрицами(векторами) из кернела 
        I = SquareMatrix.diag(self.size)
        cef = self.concat(I, mode = 'bottom').transpose()
        pivot_n = 0
        def getPivot(mat, n):
            for i in range(pivot_n, mat.shape()[0]):
                
                if mat.mat[i][n] != 0: 
                    return (i, n)
            res = getPivot(mat, n + 1)
            return (res[0], res[1])
        finished = False
        while not finished:
            try: 
                pivot_pos = getPivot(cef[:self.size], pivot_n)
            except: 
                finished = True
                break
            pivot_col = pivot_pos[1]
            pivot_row = pivot_pos[0]
            if pivot_n == min(cef.shape()[0]- 1, cef.shape()[1] - 1): 
                finished = True
                break

            if pivot_n != pivot_row: 
                cef.interchange(pivot_row, pivot_n)
                pivot_row = pivot_n
            if cef.mat[pivot_row][pivot_col] != 1 and cef.mat[pivot_row][pivot_col] != 0:
                cef.mat[pivot_row] = scale(cef.mat[pivot_row], (1/cef.mat[pivot_row][pivot_col])) 
            cef.trunc_matrix()

            for i in range(pivot_n + 1, cef.shape()[0]):
                if cef.mat[i][pivot_col] == 0: continue
                else:
                    cef.mat[i] = listadd(cef.mat[i], cef.mat[pivot_row], (-cef.mat[i][pivot_col])) 
                    cef.trunc_matrix()
            pivot_n += 1
        b = cef.transpose() 
        size = self.size
        basis = []
        for i in range(b.shape()[1]):
            if b[i:i+1,:size].isnull(): 
                basis.append(b[i:i+1, size:])

        return basis

    def eigenvalues(self): # возвращает лист из собственных значений
        #return self.charac_polynom().roots()
        try: 
            return list(map(roots_round, self.charac_polynom().new_roots()))
        except Exception as e: 
            print(e)
            return "Roots are complex or matrix is not diagonalizable."

    def eigenvectors(self): # возвращает мапу, где ключ это собственное значение, а value это лист из айгенвекторов
        eigenvectors = {}
        if not isinstance(self.eigenvalues(), list): raise EigenvaluesError
        for eigenvalue in self.eigenvalues():
            nilp = self + SquareMatrix.diag(self.size)*(-eigenvalue)
            eigenvectors[eigenvalue] = nilp.ker()

        return eigenvectors

    def eigendecomp(self): # диагонализация, возвращает лист из трех матриц [P, D, P^-1]
        try:
            eigenvectors = self.eigenvectors()
            system = []
            for pack in list(eigenvectors.values()):
                 if isinstance(pack, Matrix): system.append(pack)
                 else:
                     if isinstance(pack, list):
                         for vect in pack:
                             system.append(vect)
            if len(system) != self.shape()[0]: return "Matrix isn`t diagonalizable"
            P = Matrix.make_mat(system).transpose()
            D = SquareMatrix.creatediag(self.eigenvalues())
            T = P.inverse()
            return (P, D, T)
        except: raise EigenvaluesError

    def isSelfAdjoint(self):
        if self.transpose().mat == self.mat: return True
        else: return False

    def isPositive(self):
        for eigenvalue in self.eigenvalues():
            if eigenvalue < 0: return False
        return True

    def creatediag(l): #возвращает диагональную матрицу с элементами из листа l по диагонали
        return SquareMatrix([[l[i] if i == j else 0 for j in range(len(l))] for i in range(len(l))])    

    def square_root(self): # возвращает кв. корень 

        ...

        if self.isPositive() and self.isSelfAdjoint():
            P, D, T = self.eigendecomp()
            eigs = self.eigenvalues()
            new_D = SquareMatrix.creatediag([eig **(0.5) for eig in eigs])
            return P*new_D*T    

        else: return "Conditions are not satisfied."

    def LU(self):#returns two matrices lower and upper, valid only for non singular matrix,algorithm is simple just playing with coeff. 
        if self.det()==0:#If singular doesnt have LU form 
            return "No LU decomposition for singular matrix" 
        else: 
            size = self.size 
            L = [[0 for i in range(size)] for j in range(size)] 
            U = deepcopy(self.mat) 
            for i in range(size): 
                for j in range(i,size): 
                    if U[i][i]==0: 
                        L[j][i]=U[j][i] 
                    else: 
                        L[j][i]=U[j][i]/U[i][i] 
            for k in range(1,size): 
                for i in range(k-1,size): 
                    for j in range(i,size): 
                        if U[i][i]!=0: 
                            L[j][i]=U[j][i]/U[i][i] 
                        else: 
                            L[i][j]=U[j][i] 
                for i in range(k,size): 
                    for j in range(k-1,size): 
                        U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j] 
            for i in range(size): 
                for j in range(size): 
                    if i<j: 
                        L[i][j]=0 
            L = SquareMatrix(L) 
            L.trunc_matrix() 
            U = SquareMatrix(U) 
            U.trunc_matrix() 
            M = L * U 
            if M == self.mat: 
                return (L,U) 
            else: 
                print("No LU form for this non-singular matrix,but exists PLU form") 

    def PLU(self):# Mostly used if not exists LU form, L is lower and U is upper, P is matrix of changing rows 
        if self.det()!=0:
            lu = SquareMatrix(self.mat).LU()
            P = SquareMatrix.diag(self.size)
            if len(lu)==2:
                return (lu[0],lu[1],P)
            else:
                C,arr = deepcopy(self.mat),[]
                for i in range(self.size):
                    pivotvalue = 0
                    pivott = -1
                    for row in range(i,self.size):
                        if ((C[row][i])**(2))**(1/2)>pivotvalue:
                            pivotvalue = ((C[row][i])**(2))**(1/2)
                            pivott = row
                    if pivotvalue != 0: 
                        Pp,Pi = P.mat[pivott],P.mat[i]
                        Cp,Ci = C[pivott],C[i]
                        P.mat[i],P.mat[pivott] = Pp,Pi
                        C[i],C[pivott] = Cp,Ci
                        for j in range(i+1,self.size):
                            C[ j ][ i ] = C[j][i]/C[ i ][ i ]
                            for k in range(i+1,self.size): 
                                C[ j ][ k ] =C[j][k] -  C[ j ][ i ] * C[ i ][ k ]
                PA = P * self
                (L,U) = PA.LU()
                p_inverse = P.inverse()
                return (p_inverse,L ,U) 
        else:
            return "No PLU decomposition for singular matrix"

    def QR(self):#Q is orthonormal, R is upper triangular, considered only for square matrix 
        if self.det()!=0: 
            new_mat = self.transpose() 
            basis = [Matrix([i]) for i in new_mat.mat] 
            new_basis = Matrix.orthonormalization(basis) 
            QT = Matrix.make_mat(new_basis) 
            Q = QT.transpose() 
            R = QT * self 
            return (Q, R) 
        else: 
            print("No QR decomposition for singular matrix")

    def polar_decomp(self):
        n = self.shape()[0]
        m = self.shape()[1]
        A_adjoint_A = self.transpose()*self
        A_A_adjoint = self * self.transpose()
        
        
        eigenvectors = A_adjoint_A.eigenvectors()
        evalue =[i for i in eigenvectors.keys()]
        evalue.sort()
        evalue.reverse()
        system = []
        for pack in evalue:
            if isinstance(eigenvectors[pack], Matrix): system.append(eigenvectors[pack])
            else:
                if isinstance(eigenvectors[pack], list):
                    for vect in eigenvectors[pack]:
                        system.append(vect)
        
        evectors = Matrix.make_mat(system)
        basis = [Matrix([i]) for i in evectors.mat] 
        new_basis = Matrix.orthonormalization(basis) 
        VT = Matrix.make_mat(new_basis)
        V = VT.transpose()
        D = Matrix.creatediag_svd([eig **(0.5) for eig in evalue], m, n)


        eigenvectors2 = A_A_adjoint.eigenvectors()
        evalue2 =[i for i in eigenvectors2.keys()]
        evalue2.sort()
        evalue2.reverse()
        

        system2 = []
        for pack in evalue2:
            if isinstance(eigenvectors2[pack], Matrix): system2.append(eigenvectors2[pack])
            else:
                if isinstance(eigenvectors2[pack], list):
                    for vect in eigenvectors2[pack]:
                        system2.append(vect)
        
        evectors2 = Matrix.make_mat(system2)
        basis2 = [Matrix([i]) for i in evectors2.mat] 
        new_basis2 = Matrix.orthonormalization(basis2) 
        WT = Matrix.make_mat(new_basis2)
        W = WT.transpose()
        ID = SquareMatrix.creatediag([-1 for i in range(W.size)])
        W_min = W*ID
        F = (W*D*VT).matrix_round()
        if F == self:
            P = V*D*VT
            U = W*VT
        else:
            P = V*D*VT
            U = W_min*VT

        return (P, U)

    def cholesky(self): 
        if SquareMatrix.isSelfAdjoint(self) and SquareMatrix.isPositive(self): 
            L = [[0 for i in range(self.size)] for j in range(self.size)] 
            for i in range(self.size): 
                for j in range(i+1): 
                    sum = 0 
                    for k in range(j): 
                        sum += L[i][k] * L[j][k] 
                    if (i == j): 
                        L[i][j] = (self.mat[i][i] - sum)**(1/2) 
                    else: 
                        L[i][j] = (1.0 / L[j][j] * (self.mat[i][j] - sum)) 
            L = SquareMatrix(L) 
            L.trunc_matrix() 
            return (L,L.transpose()) 
        else: 
            return "No Cholesky decompositon for this matrix"

    def isDiagonalizable(self):
        try:
            (A, B, C) = self.eigendecomp()
            return True
        except: return False

    def eigenvalues_multiplicities(self):
        try: 
            res = {}
            for elem in list(set(self.eigenvalues())):
                res[elem] = self.eigenvalues().count(elem)
            return res
        except: 
            return None

    def jordandecomp(self):

        def getJ(size, pat):
            list = re.findall('[(]-?\d+_?[)]', pat)
            K = SquareMatrix.null(size)
            for i in range(size):
                eig = re.search('-?\d+', list[i])[0]
                K.mat[i][i] = float(eig)
                if '_' in list[i]: K.mat[i + 1][i] = 1
            return K

        if not self.isDiagonalizable():
            if isinstance(self.eigenvalues(), str): return "Error."
            pattern = ''
            system = []
            I = SquareMatrix.diag(self.size)
            dict = self.eigenvalues_multiplicities()
            for eigenvalue in dict.keys():
                B = self - I * eigenvalue
                all = (B**self.size).ker()
                body = []
                for vect in all:
                    chain = [(((B ** i) * vect).transpose()).mat[0] for i in range(0, self.size + 1)]
                    body.append(chain)
                #print(body)
                Table = JordanTable(body, self.size, dict[eigenvalue])
                Table = Table.reduce()
                for chain in Table.table:
                    for vect in chain:
                        pattern += f'({eigenvalue}_)'
                        system.append(Matrix([vect])) # вектора упорядоченные
                pattern = pattern[:-2] + pattern[-1]
            J = getJ(self.size, pattern)
            A = Matrix.make_mat(system).transpose()
            return (A, J, A.inverse())
        else: return self.eigendecomp()

                    

class JordanTable():

    def __init__(self, list_of_lists, sep, need):
        self.table = list_of_lists
        self.sep = sep
        self.need = need
        self.n_of_strings = len(self.table)

    def update(self):
        for i in range(len(self.table)):
            if self.table[i] == []:
                
                del self.table[i]
                self.n_of_strings -= 1

    def __str__(self):
        return self.table.__str__()

    def __getitem__(self, slime):
        if isinstance(slime, int): return self.table[slime]
        if isinstance(slime, slice):
            return self.table[slime.start: slime.stop]
        if isinstance(slime, tuple):
            print(slime)

    def zero_is_present(self):
        null = [0 for i in range(self.sep)]
        for i in range(self.n_of_strings):
            if self.table[i][-1] == null: 
                return True
        return False

    def removezero(self):
        null = [0 for i in range(self.sep)]
        while self.zero_is_present():
            for i in range(self.n_of_strings):
                if self.table[i][-1] == null: 
                    del self.table[i][-1]
                    self.update()


    def getlastblock(self):
        return Matrix([self.table[i][-1] for i in range(self.n_of_strings)])

    def trunc_table(self):
        for i in range(self.n_of_strings):
            for j in range(len(self.table[i])):
                self.table[i][j] = list(map(new_round, self.table[i][j]))

    def scale(self, i, n):
        for j in range(len(self.table[i])):
            self.table[i][j] = scale(self.table[i][j], n)

    def add_and_scale(self, i, j, n):
        for l in range(1, min(len(self.table[i]), len(self.table[j])) + 1):
            self.table[i][-l] = listadd(self.table[i][-l], self.table[j][-l], n)              

    def ladder(self):
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                if len(self.table[i]) > len(self.table[j]):
                    self.interchange(i, j)

    def interchange(self, i, j):
        self.table = swapPositions(self.table, i, j)

    def amount(self):
        cnt = 0
        for string in self.table:
            cnt += len(string)
        return cnt

    def reduce(self):

        def ITER(mat):
            #################################################
            def getPivot(mat, n):
                if n >= mat.cols: return (-1, -1)
                for i in range(pivot_n, mat.shape()[0]):
                    if mat.mat[i][n] != 0: 
                        return (i, n)
                res = getPivot(mat, n + 1)
                return (res[0], res[1])

            finished = False
            pivot_n = 0
            while not finished:
                if pivot_n == min(mat.shape()[0]- 1, mat.shape()[1] - 1): 
                    finished = True
                    break
                pivot_pos = getPivot(mat, pivot_n)
                if pivot_pos == (-1, -1): 
                    finished = True
                    break
                pivot_col = pivot_pos[1]
                pivot_row = pivot_pos[0]

                if pivot_n != pivot_row: 
                    
                    mat.interchange(pivot_row, pivot_n)
                    actual_table.interchange(pivot_row, pivot_n) # <--------
                    pivot_row = pivot_n
                if mat.mat[pivot_row][pivot_col] != 1:
                    actual_table.scale(pivot_row, (1/mat.mat[pivot_row][pivot_col]))
                    actual_table.trunc_table()
                    mat.mat[pivot_row] = scale(mat.mat[pivot_row], (1/mat.mat[pivot_row][pivot_col])) 
                    mat.trunc_matrix()
                for i in range(pivot_n + 1, mat.shape()[0]):
                    if mat.mat[i][pivot_col] == 0: 
                       
                        continue
                    else:
                        actual_table.add_and_scale(i, pivot_row, -mat.mat[i][pivot_col])
                        mat.mat[i] = listadd(mat.mat[i], mat.mat[pivot_row], -mat.mat[i][pivot_col]) 
                        
                pivot_n += 1
            
            #################################################
        actual_table = deepcopy(self)
        actual_table.removezero()
        finished = False
        while actual_table.amount() != self.need:
            actual_table.removezero()
            actual_table.ladder()
            actual_mat = actual_table.getlastblock()
            ITER(actual_mat)
        return actual_table

class Vector(Matrix): # этот класс кажется бесполезный, вместо векторов юзал матрицу 1хn, вам тоже рекомендую

    def __init__(self, vect):
        self.mat = vect
        self.length = len(vect)

    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return Vector([self.mat[i] * n for i in range(self.length)])

    def __str__(self):
        return re.sub(' ', '\n ', self.mat.__str__())

    def __add__(self, vector):
        return Vector([self.mat[i] + vector.mat[i] for i in range(self.length)])
    

if __name__ == '__main__':
    T = Matrix([[0, 5], [-2, 3], [1, 1]])
    T1 = Matrix([[0, 5], [-2, 3], [1, 1]])
    
    B = SquareMatrix([[-2, 0], [0, 0]])
    C = SquareMatrix([[2, -1], [2, 2]])
    D = Matrix([[6, -8, -4, 5, -4],[2, 7, -5, -6, 4],[0, -1, -8, 2, 2], [-1, -2, 4, 4, -8]])
    D1 = SquareMatrix([[6, -8, -4, 5],[2, 7, -5, -6],[0, -1, -8, 2], [-1, -2, 4, 4]])
    D = SquareMatrix([[1, 2, 2], [3, 3, 4], [5, 4, 5]])
    D = SquareMatrix([[-1, 2, 2], [2, 2,2], [-3, -6, -6]])
    D = SquareMatrix.creatediag([1, 1, 1]) 
    D = SquareMatrix([[5, 4, 3], [-1, 0, -3], [1, -2 , -1]])
    #D = SquareMatrix([[4, 1, 0, -1], [0, 3, 0, 1], [0, 0, 4, 0], [1, 0, 0, 5]])
    #D = SquareMatrix([[-1, 4, 0, 0, 0], [0, 3, 0, 0, 0], [0, -4, -1, 0, 0], [3, -9, -4, 2, -1], [1, 5, 4, 1, 4]])
    D = SquareMatrix([[2, 2, 11, 18, -11, 3, 28, 21, -8, 4], 
                      [13, 1, -34, -50, 51, -3, -75, -75, 27, 3],
                      [-9, 3, 30, 33, -42, 5, 52, 62, -23, 3],
                      [1, 3, 4, 3, -7, 5, 3, 14, -3, 5],
                      [-9, 2, 21, 19, -30, 2, 31, 43, -15, 1],
                      [-5, 3, 12, 6, -19, 4, 10, 27, -8, 3],
                      [3, -3, -13, -13, 18, -3, -18, -29, 10, -5],
                      [-4, 0, 10, 13, -14, 0, 20, 21, -8, 0],
                      [2, -3, -6, 2, 7, -1, 2, -10, 3, -4],
                      [2, -3, -11, -7, 13, -2, -12, -20, 8, -5]])
    D = SquareMatrix([[4, 1, 0, -1], [0, 3, 0, 1], [0, 0, 4, 0], [1, 0, 0, 5]])
    D = SquareMatrix([[2, 2, 4, 0, 0], [0, 0, 1, 1, 0], [-1, -1, -2, 0, 0], [1, 1, 2, 0, 0], [-1, -1, -3, -1, 0]])
    #(A, B) = D.polar_decomp()
    #print(A*B)
    #print(D.SVD())
    #print(D.polar_decomp())
    #print(D.charac_polynom().coeffs)
    #print(D.eigenvalues())
    #(A, B, C) = D.jordandecomp()
    #print(A* B* C)
    #mtx = SquareMatrix([[4,12,-16],[12,37,-43],[-16,-43,98]])
    #print(B.polar_decomp())
    #print(T.SVD())
    
    # T = Matrix([[0.55, 5.85], [-2.3, 3], [1, 1]])
    # print(T.matrix_round())
    # B = Matrix([[2, 2], [1, 0]])
    # print(B**5)
    # print(D)
    # print(Matrix.orthogonalization(D))
    #T = Matrix([[0, 5], [-2, 3], [1, 1], [1, -1]])
    #C = Matrix([[2, -1], [2, 2]])
    #print(C.REF())
    #print(T, end = '\n\n')
    #print(T.transpose().REF())
    #print(T.REF())
    #B = Matrix([[-2, 0], [0, 0]])
    #C = Matrix([[2, -1], [2, 2]])
    #D = Matrix([[6, -8, -4, 5, -4],[2, 7, -5, -6, 4],[0, -1, -8, 2, 2], [-1, -2, 4, 4, -8]])
    #print(D.SVD())
    #v1 = Matrix([[1, 3, 4]])
    # print(Matrix.normalization_vector(v1))
    #v2 = Matrix([[2, 4, -1]])
    #v3 = Matrix([[3, 1, 7]])
    #print(m1.SVD())
    #print(m1.QR()[0] * m1.QR()[1])
    # t = [[[1, 0, 0, 0], [0, 0, 0, 1], [-1, 1, 0, 1], [0, 0, 0, 0]], 
    #      [[0, 1, 0, 0], [1, -1, 0, 0], [-1, 1, 0 ,1], [0, 0, 0, 0]], 
    #      [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    #      [[0, 0, 0, 1], [-1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    # t2 = [[[-1, 0, 0, 0], [0, 0, 0, -1], [1, -1, 0, -1]], [[0, 0, 1, 0]], 
    #   [[-1, 1, 0, 0], [1, -1, 0, -1], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
    # Table = JordanTable(t, 4)
    # print(Table.reduce())
    #I = SquareMatrix.diag(2)
    #A = SquareMatrix([[2, 0 ,1], [0, 6, 2], [0, 0, 2]])
    #A = SquareMatrix([[-1, 4, 0, 0, 0], [0, 3, 0, 0, 0], [0, -4, -1, 0, 0], [3, -9, -4, 2, -1], [1, 5, 4, 1, 4]])
    #A = SquareMatrix([[4, 1, 0, -1], [0, 3, 0, 1], [0, 0, 4, 0], [1, 0, 0, 5]])
    #A = SquareMatrix([[5, -4], [9, -7]]) # right
    #N = (A + I)
    #print((N ** 2) * Matrix([[0, 1]]).transpose())
    #A = SquareMatrix([[9, 7, 3], [-9, -7, -4], [4, 4, 4]])
    #A = SquareMatrix([[2, 2, -1], [-1, -1, 1], [-1, -2, 2]])
    #A = SquareMatrix([[5, 4, 3], [-1, 0, -3], [1, -2 , -1]])
    #print(A.jordandecomp())
    # p = Polynomial(3, [1, -8.000585029223787, 16.008565334330264])
    # print(p)
    # print(p.root())


    #p = Polynomial(3, [1, -8, 16])
    #print(p)
    #print(p.roots())
    #print(p.derivative(1))
    #print(A.jordandecomp()[0] * A.jordandecomp()[1] * A.jordandecomp()[2])
    #print(A * A.jordandecomp()[0][1].transpose())
    #system = [v1 , v2, v3]
    #print(Matrix.orthonormalization(system))
    # print(Matrix.normalization_system(system))
    # new_system = Matrix.orthogonalization(system)
    # print(new_system)
#    A = SquareMatrix([[1, 2, 1, 0, 0], [2, 1, 2, 0, 0], [1, 1, 2, 0 ,0], [0, 0, 0, 0, 2], [0, 0, 0, 2, 0]])
#    B = Matrix([[-3, 6, -1, 1, -7], [1, -2,2, 3, -1], [2, -4, 5, 8, -4]])
#    T = Matrix([[-2, -5, 8, 0, -17], [1, 3, -5, 1, 5], [3, 11, -19, 7, 1], [1, 7, -13, 5, -3]])
#    G = SquareMatrix([[9, -4, -2, -4], [-56, 32 ,-28, 44], [-14, -14, 6, -14], [42, -33, 21, -45]])
#    print(T.eigenvalues())
    #  C = SquareMatrix([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    #  print(C.LU()[0] * C.LU()[1])
#    C = SquareMatrix([[1, 2, 3], [-1, 3, 4], [2, 0, 1]])
#   B = [[2, 2], [1, 0], [0, 0]]

#    D = SquareMatrix([[0.9, 0.4], [0.1, 0.6]])
#    P = SquareMatrix([[1, 2, -3],[2, 5, -2], [1, 3, 1]])
#    F = SquareMatrix([[1, 2 ,3 ,4, 5], [4, 6, 1, -9, 8], [12, 10,2, 7, 0], [4, 6, 1, -9, 8], [1, 5, 2, 4, 3]])
#    G = SquareMatrix([[1, 2, 3, 4], [4, 6, 1, -9], [12, 1, 2, 7], [4, 6, 1, -9]])
#    T = Matrix([[0, 5], [-2, 3], [1, 1]])
#    P = SquareMatrix([[1, -2],[-1, 2]])
#    M = Matrix([[1, -1 ], [5, -4], [7, -6 ]])
#    I = SquareMatrix.diag(3)
#    A1 = Matrix([[1, 2, 3], [3, 0, 4]])
#    A2 = SquareMatrix([[1, 6, -2], [-3, 2, 0], [0, 3, -4]])
#    A3 = SquareMatrix([[2, 2],[1, 3]])
#    K = SquareMatrix([[1, 3, 5], [3, 2, 1], [5, 1, 3]])
#    C = SquareMatrix([[2, 1, 1], [1, 2, 1], [1, 1, 2]])

#    R = SquareMatrix([[1 for i in range(4)] for i in range(4)])
#    O = SquareMatrix.null(5)
#    I = SquareMatrix.creatediag([1, 1, 1])
#    D = SquareMatrix([[1, 2, 2], [3, 3, 4], [5, 4, 5]])
#    D = SquareMatrix([[1, 1], [1, 1]])
#    K = SquareMatrix([[-1, 2, 2], [2, 2,2], [-3, -6, -6]])
    
#    K = SquareMatrix([[1, 1, 1], [0, 0,1], [0, 0, 1]])
#    K = SquareMatrix([[3, 4, -2], [1, 4,-1], [2, 6, -1]])
#    K = SquareMatrix([[7, -4, 0], [8, -5,0], [6, -6, 3]])
#    K = SquareMatrix([[3, 4, 0.000000000001], [2.00000001, -1, 0.999999999], [0, 0, 6]])
#    D = SquareMatrix([[1, 2, 2], [3, 3, 4], [5, 4, 5]])
#    v1 = Matrix([[1, 2, 3]])
#    v2 = Matrix([[-1, 0, 5]])
#    l = [v1.transpose(), v2.transpose()]
#    print(Matrix.make_mat(l))
#    print(K[1].shape())
#    print(K[1].transpose())
#    m1 = SquareMatrix([[1,3,4],[2,4,-1],[3,1,7]])
#    for i in m1.LU():
#        print(i)
    