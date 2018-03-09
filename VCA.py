import numpy as np
import scipy.io as sio
import numpy.linalg as la
import matplotlib.pyplot as plt
from cvxopt import solvers, matrix

class VCA(object):

	p = None
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None

	endmembers = None

	def __init__(self, argin):
		if type(argin[0]) == type(''):
			data_loc = argin[0]
			self.load_data(data_loc)
		else:
			self.data = argin[0]
		self.p = argin[1]
		
	def load_data(self,data_loc):
		pkg_data = sio.loadmat(data_loc)
		self.data = pkg_data['X']
		self.nRow = self.data.shape[0]
		self.nCol = self.data.shape[1]
		self.nBand = self.data.shape[2]
	
	def convert_2D(self,data):
		self.nPixel = self.nRow*self.nCol
		data_2D = np.asmatrix(data.reshape((self.nRow*self.nCol,self.nBand))).T
		return data_2D

	def convert_3D(self,data):
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def extract_endmember(self):
		R = self.convert_2D(self.data)
		L, N = R.shape
		SNR_th = 15 + 10*np.log10(self.p)
		r_m = R.mean(1)  # mean
		R_m = np.matlib.repmat(r_m,1,N) # mean of each band
		R_o = R-R_m # data with zero-mean
		[Ud, Sd, Vd] = la.svd(R_o*R_o.T/N)
		Ud = Ud[:,:self.p]
		Sd = Sd[:self.p]
		Vd = Vd[:self.p,:]
		x_p = Ud.T*R_o
		P_y = (np.power(R,2)/N).sum()
		P_x = np.asscalar((np.power(x_p,2)/N).sum() + (r_m.T*r_m))
		SNR = np.asscalar(10*np.log10(np.abs([(P_x - self.p/L*P_y)/(P_y-P_x)])))
		print(SNR)
		print(SNR_th)
		if SNR < SNR_th:
			d = self.p-1
			Ud = Ud[:,:d] 
			R_p = Ud*x_p[:d,:] + R_m
			x = x_p[:d,:]
			c = np.sqrt((np.power(x,2).sum(0)).max())
			y = np.concatenate((x,c*np.matrix(np.ones(N))),axis=0)
		else:
			d = self.p
			[Ud, Sd, Vd] = la.svd((R*R.T)/N)
			Ud = Ud[:,:d]
			Sd = Sd[:d]
			Vd = Vd[:d,:]
			x_p = Ud.T*R
			R_p = Ud*x_p[:d,:]
			x = x_p
			u = x.mean(1)
			aux1 = np.matlib.repmat(u,1,N).T
			aux2 = (x * np.matlib.repmat(u,1,N).T).sum()
			y = x / np.matlib.repmat( (x * np.matlib.repmat(u,1,N).T).sum() ,d,1)
		indice = np.zeros(self.p)
		S = np.matrix(np.zeros((self.p,self.p)))
		S[self.p-1,0] = 1
		for i in range(0,self.p):
			w = np.random.rand(self.p,1)
			aux = S*la.pinv(S)
			f = w - (aux*w)
			aux = np.sqrt(np.sum(np.power(f,2)))
			f = f / aux
			v = f.T*y
			aux = np.abs(v)
			v_max = np.max(aux)
			indice = indice.astype(int)
			indice[i] = np.asscalar(np.argmax(aux))
			S[:,i] = y[:,indice[i]]
		self.y = R_p
		self.endmembers = R_p[:,indice]










