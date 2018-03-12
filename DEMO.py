from VCA import VCA
from MAPS import *
import scipy.io as sio
import matplotlib.pyplot as plt

class DEMO(object):

	algo = None
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	groundtruth = None
	num_gtendm = None

	def __init__(self, argin):
		self.load_data(argin[0])
		self.load_groundtruth(argin[1])
		self.data = self.convert_2D(self.data)
		
		self.p = argin[2]
		
		if argin[3] == 'VCA':
			self.algo = VCA([self.data,self.nRow,self.nCol,self.nBand,
				self.nPixel, self.p]) 

	def load_data(self,data_loc):
		pkg_data = sio.loadmat(data_loc)
		self.data = pkg_data['X']
		self.nRow = self.data.shape[0]
		self.nCol = self.data.shape[1]
		self.nBand = self.data.shape[2]

	def load_groundtruth(self,gt_loc):
		pkg_gt = sio.loadmat(gt_loc)
		self.groundtruth = pkg_gt['Y']
		self.num_gtendm = self.groundtruth.shape[1]

	def convert_2D(self,data):
		self.nPixel = self.nRow*self.nCol
		data_2D = np.asmatrix(data.reshape((self.nRow*self.nCol,self.nBand))).T
		return data_2D

	def convert_3D(self,data):
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def plot_abundance(self, abundances,i):
		plt.matshow(abundances[:,:,i])

	def plot_groundtruth(self):
		plt.matshow(self.groundtruth[:,:])

	def plot_endmember(self,endmembers,i):
		print(endmembers.shape)
		plt.plot(endmembers[:,i])
		plt.title(str(i))
		plt.xlabel('wavelength (µm)')
		plt.ylabel('reflectance (%)')
		plt.tight_layout()

if __name__ == '__main__':
	# data_loc = "./DATA/cuprite_data.mat"
	# data_loc = "./DATA/cuprite_groundtruth.mat"
	data_loc = "./DATA/grss2018_data.mat"
	gt_loc = "./DATA/grss2018_groundtruth.mat"
	num_endm = 20
	d = DEMO([data_loc,gt_loc,num_endm,'VCA'])
	
	d.algo.extract_endmember()
	d.plot_endmember(d.algo.endmembers,1)
	
	a = UCLS([d.data,d.algo.endmembers])
	a.map_abundance()
	a.abundances = d.convert_3D(a.abundances)
	d.plot_abundance(a.abundances,0)
	
	plt.show()