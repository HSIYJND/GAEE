import numpy as np
from cvxopt import solvers, matrix

class FCLS(object):

	
	data_loc = None
	endmembers_loc = None
	
	data = None
	endmembers = None

	abundances = None

	def __init__(self, data_loc, endmembers_loc):
		self.data = m
		self.endmembers = n

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

	def map_abundace(self):

		M = self.convert_2D(self.data).T
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

		self.abundances = X

if __name__ == '__main__':
	# data_loc = "./DATA/cuprite_data.mat"
	# data_loc = "./DATA/cuprite_groundtruth.mat"
	data_loc = "./TEMP/M.mat"
	gt_loc = "./TEMP/U.mat"
	num_endm = 20
	algo = VCA(data_loc,num_endm)
	algo.load_groundtruth(gt_loc)
	algo.extract_endmember()
	# vca.map_abundace()
	algo.FCLS()
	# vca.plot_abundance(1)	
	algo.plot_groundtruth()
	plt.show()