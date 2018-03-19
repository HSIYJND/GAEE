import numpy as np
import scipy as sp

class ATGP(object):

	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None
	
	endmembers = None

	verbose = True

	def __init__(self, argin, verbose):
		self.verbose = verbose
		if (self.verbose):
			print ('---		Initializing ATGP algorithm')
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

	def extract_endmember(self):
		if (self.verbose):
			print('---		Starting endmembers Extracting')

		data = np.asarray(self.data)
		print(type(data))
		q = self.p
		nsamples, nvariables = data.shape
		print(nsamples,nvariables)

		# Algorithm initialization
		# the sample with max energy is selected as the initial endmember
		max_energy = -1
		idx = 0
		for i in range(nsamples):
			r = data[i]
			val = np.dot(r, r)
			if val > max_energy:
				max_energy = val
				idx = i
		# Initialization of the set of endmembers and the endmembers index vector
		E = np.zeros((q, nvariables), dtype=np.float32)
		E[0] = data[idx] # the first endmember selected
		# Generate the identity matrix.
		I = np.eye(int(nvariables/5),dtype=np.int)
		IDX = np.zeros(q, dtype=np.int)

		IDX[0] = idx

		for i in range(q-1):
			UC = E[0:i+1]
			# Calculate the orthogonal projection with respect to the pixels at present chosen.
			# This part can be replaced with any other distance
			PU = I - np.dot(UC.T,np.dot(sp.linalg.pinv(np.dot(UC,UC.T)),UC))
			max_energy = -1
			idx = 0
			# Calculate the most different pixel from the already selected ones according to
			# the orthogonal projection (or any other distance selected)
			for j in range(nsamples):
				r = data[j]
				result = np.dot(PU, r)
				val = np.dot(result.T, result)
				if val > max_energy:
					max_energy = val
					idx = j
		# The next chosen pixel is the most different from the already chosen ones
			E[i+1] = data[idx]
			IDX[i+1] = idx

		print('---		Ending endmembers Extracting')

		self.endmembers = E
		
		return E
