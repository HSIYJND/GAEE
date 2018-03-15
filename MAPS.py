import numpy as np
from cvxopt import solvers, matrix
import scipy.optimize as opt

class UCLS(object):
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	endmembers = None
	abundances = None

	def __init__(self, argin):
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

	def convert_3D(self,data):
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def map_abundance(self):

		M = self.data.T
		U = self.endmembers.T
		Uinv = np.linalg.pinv(U.T)

		self.abundances = self.convert_3D(np.dot(Uinv, M[0:,:].T).T)
		return self.abundances

class NNLS(object):
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	endmembers = None
	abundances = None

	def __init__(self, argin):
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

	def convert_3D(self,data):
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def map_abundance(self):

		M = np.asarray(self.data.T)
		U = np.asarray(self.endmembers.T)

		N, p1 = M.shape
		q, p2 = U.shape

		X = np.zeros((N, q), dtype=np.float32)
		MtM = np.dot(U, U.T)
		for n1 in range(N):
			X[n1] = opt.nnls(MtM, np.dot(U, M[n1]))[0]

		self.abundances = self.convert_3D(X)
		return self.abundances

class FCLS(object):
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	endmembers = None
	abundances = None

	def __init__(self, argin):
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

	def convert_3D(self,data):
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def _numpy_None_vstack(self,A1, A2):
		if A1 is None:
			return A2
		else:
			return np.vstack([A1, A2])

	def _numpy_None_concatenate(self,A1, A2):
		if A1 is None:
			return A2
		else:
			return np.concatenate([A1, A2])

	def _numpy_to_cvxopt_matrix(self,A):
		A = np.array(A, dtype=np.float64)
		if A.ndim == 1:
			return matrix(A, (A.shape[0], 1), 'd')
		else:
			return matrix(A, A.shape, 'd')

	def map_abundance(self):

		M = self.data.T
		U = self.endmembers.T

		solvers.options['show_progress'] = False
		N, p1 = M.shape
		nvars, p2 = U.shape

		C = self._numpy_to_cvxopt_matrix(U.T)
		Q = C.T * C

		lb_A = -np.eye(nvars)
		lb = np.repeat(0, nvars)
		A = self._numpy_None_vstack(None, lb_A)
		b = self._numpy_None_concatenate(None, -lb)
		A = self._numpy_to_cvxopt_matrix(A)
		b = self._numpy_to_cvxopt_matrix(b)

		Aeq = self._numpy_to_cvxopt_matrix(np.ones((1,nvars)))
		beq = self._numpy_to_cvxopt_matrix(np.ones(1))

		M = np.array(M, dtype=np.float64)
		X = np.zeros((N, nvars), dtype=np.float32)
		for n1 in range(N):
			d = matrix(M[n1], (p1, 1), 'd')
			q = - d.T * C
			sol = solvers.qp(Q, q.T, A, b, Aeq, beq, None, None)['x']
			X[n1] = np.array(sol).squeeze()
			print(str(N/n1) + '%')

		self.abundances = self.convert_3D(X)
		return self.abundances
