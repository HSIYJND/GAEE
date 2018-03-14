from VCA import *
from GAEE import *
from MAPS import *
import scipy.io as sio
import matplotlib.pyplot as plt

class DEMO(object):

	ee = None
	am = None
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	groundtruth = None
	num_gtendm = None

	endmembers = None
	abundances = None

	def __init__(self, argin):
		print('... Initializing DEMO')
		self.load_data(argin[0])
		self.load_groundtruth(argin[1])
		self.data = self.convert_2D(self.data)
		
		self.p = argin[2]
		
		if argin[3] == 'VCA':
			print('... Selecting VCA endmember extractor')
			self.ee = VCA([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p])
		if argin[3] == 'GAEE':
			self.npop = argin[4]
			self.ngen = argin[5]
			self.cxpb = argin[6]
			self.mutpb = argin[7]
			print('... Selecting GAEE endmember extractor')
			self.ee = GAEE([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, self.npop,
				self.ngen,self.cxpb,self.mutpb])

		print('... Selecting UCLS abundance mapper')
		self.am = UCLS([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p])

	def extract_endmember(self):
		print('... Extracting endmembers')
		self.endmembers = self.ee.extract_endmember()

	def map_abundance(self):
		print('... Mapping abundances')
		self.am.endmembers = self.endmembers
		self.abundances = self.am.map_abundance()

	def load_data(self,data_loc):
		print('... Loading data')
		pkg_data = sio.loadmat(data_loc)
		self.data = pkg_data['X']
		self.nRow = self.data.shape[0]
		self.nCol = self.data.shape[1]
		self.nBand = self.data.shape[2]

	def load_groundtruth(self,gt_loc):
		print('... Loading groundtruth')
		pkg_gt = sio.loadmat(gt_loc)
		self.groundtruth = pkg_gt['Y']
		self.num_gtendm = self.groundtruth.shape[1]

	def convert_2D(self,data):
		print('... Converting 3D data to 2D')
		self.nPixel = self.nRow*self.nCol
		data_2D = np.asmatrix(data.reshape((self.nRow*self.nCol,self.nBand))).T
		return data_2D

	def convert_3D(self,data):
		print('... Converting 2D data to 3D')
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def plot_abundance(self,i):
		print('... Plotting abundance')
		plt.matshow(self.abundances[:,:,i])

	def plot_groundtruth(self):
		print('... Plotting groundtruth')
		plt.matshow(self.groundtruth[:,:])

	def plot_endmember(self,i):
		print('... Plotting endmember')
		plt.plot(self.endmembers[:,i])
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
	algo = 'VCA'

	vca = DEMO([data_loc,gt_loc,num_endm,algo])
	vca.extract_endmember()
	vca.map_abundance()
	vca.plot_endmember(0)
	vca.plot_abundance(0)
	plt.show()

	npop = 100
	ngen = 100
	cxpb = 0.3
	mutpb = 0.5
	algo = 'GAEE'
	
	gaee = DEMO([data_loc,gt_loc,num_endm,algo,npop,ngen,cxpb,mutpb])
	gaee.extract_endmember()
	gaee.map_abundance()
	gaee.plot_endmember(0)
	gaee.plot_abundance(0)
	plt.show()
