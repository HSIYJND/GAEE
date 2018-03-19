import numpy as np
import scipy as sp
from ATGP import *

class FIPPI(object):

	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None
	
	endmembers = None

	maxit = None

	verbose = True

	def __init__(self, argin, verbose):
		self.verbose = verbose
		if (self.verbose):
			print ('---		Initializing FIPPI algorithm')
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

		self.maxit = argin[6]

	def _PCA_transform(self,M, n_components):
		from sklearn.decomposition import PCA
		# M as shape (N x p)
		# scikit.learn expect (N x p)
		pca = PCA(n_components=n_components)
		return pca.fit_transform(M)

	def _rows_union(a, b):
		a_hashable = map(tuple, a)
		b_hashable = map(tuple, b)
		a_set = set(a_hashable)
		b_set = set(b_hashable)
		if a_set.issubset(b_set):
		    # return True if a is subset of b, False otherwise
		    return b, True
		u = a_set.union(b_set)
		return np.array(list(u)), False

	def extract_endmember(self):
		if (self.verbose):
			print('---		Starting endmembers Extracting')

		M = np.asarray(self.data)
		q = self.p

		h = self.nRow
		w = self.nCol
		numBands = self.nBand

		N, p1 = M.shape

		data_pca = self._PCA_transform(M, q)
		N, p = data_pca.shape

		# Initial skewers
		aux_ee = ATGP([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, nSkewers, initSkewers],self.verbose)	
		skewers = ATGP(data_pca, q)

		stop = False # stop condition
		it = 1 # iterations
		idx = [] # indexes of the induced endmembers
		while not stop:
			# Calculate Nppi
			Nppi = np.zeros((N), dtype=np.int32)
			proj = np.dot(data_pca, skewers.T)
			I1 = np.argmin(proj, axis=0)
			I2 = np.argmax(proj, axis=0)
			for j in range(proj.shape[1]):
				Nppi[I1[j]] = Nppi[I1[j]] + 1
				Nppi[I2[j]] = Nppi[I2[j]] + 1
			# Check new skewers
			# A tuple is returned, first part is the array r
			r = np.nonzero(Nppi)[0]
			skewers_r, isSubset = _rows_union(data_pca[r], skewers)
			# if data_pca[r] isSubset of skewers
			if isSubset == True:
				stop = True
				idx = r
			else:
				# new skewers
				skewers = skewers_r
				# Check iterations
				if maxit > 0 and it == maxit:
					stop = True
					idx = r
				else:
					it = it + 1
		# Endmembers
		E = np.zeros((idx.shape[0], p1), dtype=np.float32)
		for j in range(idx.shape[0]):
			E[j] = M[idx[j]]

		print('---		Ending endmembers Extracting')

		self.endmembers = E
		
		return E
